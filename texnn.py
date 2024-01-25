"""

texnn (pronounced like "Texan") is a Python script that generates LaTex (
tex) that draws a Neural Net (nn) as a causal DAG (Bayesian Network).

texnn is capable of reproducing with ease most of the xy-pic generated bnets
(Bayesian Networks) displayed in my book

[Bayesuvius](https://github.com/rrtucci/Bayesuvius)

texnn is a stand-alone app. I wrote it specifically to aid me in writing a
chapter on transformer architectures (see directory "vanilla_transformer")
for my free, open source book Bayesuvius. But I soon realized that it could
be easily converted into a general tool that is independent of the transformer
topic and of Bayesuvius.

texnn uses the LaTex package xy-pic for drawing. In broad terms, texnn can
be described as a Python wrapper for the LaTeX package xy-pic.

texnn takes as input a bunch of strings with info for each node of a Neural 
Net (NN).

The function DAG.get_figure_str() outputs a LaTex str for drawing via xy-pic 
a bnet that represents the NN.

The function DAG.get_equations_str() outputs a LaTex str for writing the 
structural equations for a bnet that represents the NN.

"""
import numpy as np
from globals import *


def replace_none(x):
    if x:
        return x
    else:
        return ""


class Node:
    """
    This class just stores a bunch of strings with info about a node.
    
    Attributes
    ----------
    color: str | None
        color of the node
    full_right_side_of_eq: str | None
        if this is not None, it will be used as full right side of structure
        equation. All other strings that could influence the right side of
        the equation will be ignored.
    fun_args_str: str | None
        the string of function arguments
    fun_name: str | None
        the name of the function
    name: str
        a name that identifies the node uniquely.

        LaTex commands are allowed in the node name, but backslashes must be
        escaped with double backslash.

        We recommend that you input all node names in double quotes and all
        tile_ch in single quotes. That way, if you want to replace the name
        of a node from "A" to "B", and the tile_ch='A', you can do a replace
        of "A"  without changing the tile_ch.

    params_str: str | None
        a string containing parameter names and their values
    parent_names: list[str]
        a list of the names of the parents of the node.
    post_eq_comment: str | None
        Comment that you wish to appear in Roman font after the structure
        equation for this node.
    slice_str: str | None
        a string indicating slice of the node array. To be added as a
        superscript. For example, "3,[5]", "[3],[5]", "3,[n]", "3, [4:7]",
        r"\alpha,[n]". Must use raw string if using backslashes. [n]=[0:n]
    tile_ch: str
        tile character, a character that identifies the node uniquely
    """

    def __init__(self,
                 name,
                 tile_ch,
                 parent_names,
                 slice_str=None,
                 fun_name=None,
                 fun_args_str=None,
                 params_str=None,
                 color=None,
                 style_name="plain",
                 post_eq_comment=None,
                 full_right_side_of_eq=None):
        """
        Constructor
        
        Parameters
        ----------
        name: str
        tile_ch: str
        parent_names: list[str]
        slice_str: str | None
        fun_name: str | None
        fun_args_str: str | None
        params_str: str | None
        color: str | None
        style_name: str | None
        post_eq_comment: str | None
        full_right_side_of_eq: str | None
        """
        self.name = name
        self.style_name = style_name
        assert len(tile_ch) == 1, \
            f"tile_ch has length > 1. {tile_ch}"
        self.tile_ch = tile_ch
        self.parent_names = parent_names
        self.post_eq_comment = post_eq_comment
        self.full_right_side_of_eq = full_right_side_of_eq

        def rm_str(str0):
            if str0:
                return r"\text{" + str0.replace("_", "\_") + "}"
            else:
                return ""

        self.slice_str = slice_str
        self.fun_name = rm_str(fun_name)
        self.fun_args_str = fun_args_str
        self.params_str = params_str
        self.color = color

    @staticmethod
    def get_long_name(node,
                      add_superscripts=True,
                      underline=True):
        """
        This method takes as input a node name and underlines it iff 
        underline = True. In addition, output string adds to the input 
        string a superscript with its slice str.
        
        Parameters
        ----------
        node: Node
        add_superscripts: bool
        underline: bool

        Returns
        -------
        str

        """
        node_name = node.name
        if underline:
            node_name = r"\underline{" + node.name + r"}"
        if not node.slice_str or not add_superscripts:
            return node_name
        else:
            return node_name + "^{" + node.slice_str + "}"


class FancyArrow:
    """
    This class is for giving fancy, non-default  properties to an arrow.

    Default arrows are straight, black and not dashed. Occasionally,
    you want an arrow to be curved, red, dashed, or whatever. This class
    allows you to define such arrows.

    Attributes
    ----------
    child_name: str
        name of arrow's child
    color: str | None
        arrow color
    curvature: str | None
        arrow curvature, ...-3,-2,-1,0, 1,2,3,...
    displacement: int | None
        how much the arrow is displaced sideways (perpendicularly to its
        direction)
    parent_name: str
        name of arrow's parent
    style_name: str | None
        arrow style
    subscript: str | None
        arrow subscript, appears midway between endings
    superscript: str | None
        arrow superscript, appears midway between endings

    """

    def __init__(self,
                 parent_name,
                 child_name,
                 color=None,
                 style_name=None,
                 curvature=None,
                 displacement=None,
                 superscript=None,
                 subscript=None):
        """

        Parameters
        ----------
        parent_name: str
        child_name: str
        color: str | None
        style_name: str | None
        curvature: int | None
        displacement: int | None
        superscript: str | None
        subscript: str | None

        """
        self.parent_name = parent_name
        self.child_name = child_name
        self.color = color
        self.style_name = style_name
        self.curvature = curvature
        self.displacement = displacement
        self.subscript = subscript
        self.superscript = superscript

    def recognize_endings(self, parent_name, child_name):
        """
        This method returns True iff self recognizes the inputs as its
        correct endings.

        Parameters
        ----------
        parent_name: str
        child_name: str

        Returns
        -------
        bool

        """
        if parent_name == self.parent_name and \
                child_name == self.child_name:
            return True
        else:
            return False

    def get_xy_str(self, direction):
        """
        This method returns an xy string which incorporates all the fancy
        arrow attributes. For example,

        r"\ar@[red]@{-->}@<-2ex>[luu]^{superscript}"

        Parameters
        ----------
        direction: str
            a string defining the direction of the arrow. for example,
            "ruu", "rr", "lld", etc.

        Returns
        -------
        str

        """

        str0 = r"\ar"
        if self.color:
            str0 += "@[" + self.color + "]"
        if self.style_name:
            str0 += ARROW_STYLE_TO_XY_STR[self.style_name]
        if self.curvature:
            # @/^1pc/ or @/_1pc/
            curv_str = "^" + str(self.curvature) \
                if self.curvature < 0 else "_" + str(self.curvature)
            str0 += "@/" + curv_str + "pc/"
        if self.displacement:
            # @<+2ex> or @<-2ex>
            disp_str = str(self.displacement) \
                if self.displacement < 0 else "+" + str(self.displacement)
            str0 += "@<" + disp_str + "ex>"
        str0 += "[" + direction + "]"
        if self.superscript:
            str0 += "^{" + self.superscript + "}"
        if self.subscript:
            str0 += "_{" + self.subscript + "}"
        return str0


class Plate:
    """
    This method defines a plate, i.e., a rectangle in the DAG drawing that
    encloses several nodes, and indicates that the enclosed nodes should be
    repeated `num_layers_str` times.

    Attributes
    ----------
    first_and_last_row: tuple(int)
        0-based (>=0) ints. For example, "(3,4)"
    first_and_last_col: tuple(int)
        0-based (>=0) ints. For example, "(3,4)"
    margin: float
    num_layers_str: str
    only_one_layer: bool
        True iff plate has only one layer
    style_name: str

    """

    def __init__(self,
                 first_and_last_row,
                 first_and_last_col,
                 num_layers_str="1",
                 margin=1.0,
                 style_name="shaded"):
        """
        Constructor

        Parameters
        ----------
        first_and_last_row: tuple(int)
        first_and_last_col: tuple(int)
        num_layers_str: str
        margin: float
        style_name: str
        """
        self.first_and_last_row = first_and_last_row
        self.first_and_last_col = first_and_last_col
        self.num_layers_str = num_layers_str
        self.margin = margin
        self.style_name = style_name
        if self.num_layers_str.isdigit() and \
                int(self.num_layers_str) == 1:
            self.only_one_layer = True
        else:
            self.only_one_layer = False

    def get_xy_str(self):
        """
        This method returns an xy string which incorporates all the plate
        attributes. For example,

        rf'\POS"{r1},{c2}"."{r3},{c2}"."{r1},{c4}"."{r3},{c4}"!C*+<.7em>\frm{
        --}'

        Returns
        -------
        str

        """
        str0 = r"\POS"
        first_row, last_row = self.first_and_last_row
        assert first_row <= last_row
        first_col, last_col = self.first_and_last_col
        assert first_col <= last_col
        # row and col are zero based everywhere except here,
        # for r1, c2, r3, c4
        r1, c2, r3, c4 = \
            first_row + 1, first_col + 1, last_row + 1, last_col + 1
        str0 += f'"{r1},{c2}".'
        str0 += f'"{r3},{c2}".'
        str0 += f'"{r1},{c4}".'
        str0 += f'"{r3},{c4}"'
        if self.margin:
            str0 += f"!C*+<{self.margin}em>"
        str0 += r"\frm{"
        xy_str = PLATE_STYLE_TO_XY_STR[self.style_name]
        str0 += xy_str + "}"
        return str0

    def get_owned_nodes(self, node_to_tile_loc):
        """
        This method returns a list of all the nodes that are contained
        within the plate.

        Parameters
        ----------
        node_to_tile_loc: dict[Node, tuple[int]]

        Returns
        -------
        list[Node]

        """
        owned_nodes = []
        for node, tile_loc in node_to_tile_loc.items():
            row, col = tile_loc
            first_row, last_row = self.first_and_last_row
            first_col, last_col = self.first_and_last_col
            if first_row <= row <= last_row and \
                    first_col <= col <= last_col:
                owned_nodes.append(node)
        return owned_nodes


class DAG:
    """
    This class has methods for drawing a NN (via xy-pic) and writing its
    structural equations.

    Attributes
    ----------
    child_to_parents: dict[Node, list[Node]]
        a dictionary mapping every node to a list of its parent nodes. root
        nodes have empty list.
    empty_tile: str
        string for an empty tile, set to "_"
    fancy_arrows: list[FancyArrow] | None
        A list of FancyArrows
    mosaic: list[str]
        a list of strings of equal length which when stacked horizontally
        represent the bnet that we wish to draw, as a tile mosaic.
    name_to_node: dict[str, Node]
        a dictionary mapping node name to Node
    node_to_tile_loc: list[Node, tuple[int]]
        a dictionary mapping each node to its tile location, which is a
        tuple (row, col).
    nodes: list[Node]
        list of nodes for the bnet that we wish to draw
    parent_to_children: dict[Node, list[Node]]
        A dictionary mapping every node to a list of its children. Leaf
        nodes have empty list.
    plates: list[Plate] | None
        A list of Plates

    """
    empty_tile = "_"

    def __init__(self,
                 name,
                 mosaic,
                 nodes,
                 fancy_arrows=None,
                 plates=None):
        """
        
        Parameters
        ----------
        name: str
        mosaic: list[str]
        nodes: list[Node]
        fancy_arrows: list[FancyArrow] | None
        plates: list[Plate] | None
        """
        self.nodes = nodes
        self.fancy_arrows = fancy_arrows
        self.plates = plates

        tiles = [node.tile_ch for node in nodes]
        assert len(tiles) == len(set(tiles)), \
            f"some tile character is repeated.{tiles}"

        node_names = [node.name for node in nodes]
        assert len(node_names) == len(set(node_names)), \
            f"some node name is repeated.{node_names}"
        self.nodes.sort(key=lambda node: node.name.casefold())

        self.name_to_node = self.get_name_to_node()

        if fancy_arrows:
            for arrow in fancy_arrows:
                assert arrow.parent_name in node_names,\
                    "arrow parent name not found in node names. " \
                    f"'{arrow.parent_name}'"
                assert arrow.child_name in node_names, \
                    "arrow child name not found in node names. "\
                    f"'{arrow.child_name}'"
                child = self.name_to_node[arrow.child_name]
                assert arrow.parent_name in child.parent_names,\
                    "trying make fancy an arrow that does not exist\n" \
                    f"{arrow.parent_name}->{arrow.child_name}"

        self.mosaic = mosaic
        len0 = len(self.mosaic)
        len1 = len(self.mosaic[0])
        for row in range(len0):
            assert len(self.mosaic[row]) == len1, \
                f"Tile rows not all of same length.\n{self.mosaic}"

        self.name = name
        self.node_to_tile_loc = self.get_node_to_tile_loc()
        self.parent_to_children = None
        self.child_to_parents = None
        self.set_parentage()
        if plates:
            for plate in plates:
                if plate.only_one_layer:
                    continue
                owned_nodes = plate.get_owned_nodes(self.node_to_tile_loc)
                str0 = "[" + plate.num_layers_str + "]"
                for node in owned_nodes:
                    if node.slice_str:
                        node.slice_str = str0 + "," + node.slice_str
                    else:
                        node.slice_str = str0

    def get_name_to_node(self):
        """
        This method returns a name to node dictionary

        Returns
        -------
        dict[str, Node]

        """
        name_to_node = {}
        for node in self.nodes:
            name_to_node[node.name] = node
        return name_to_node

    def get_tile_ch_to_node(self):
        """
        This method returns a tile_ch_to_node dictionary

        Returns
        -------
        dict[str, Node]

        """
        tile_ch_to_node = {}
        for node in self.nodes:
            tile_ch_to_node[node.tile_ch] = node
        return tile_ch_to_node

    def get_node_to_tile_loc(self):
        """
        This method returns a node_to_tile_loc dictionary
        
        Returns
        -------
        dict[Node, tuple[int]]

        """
        tile_ch_to_node = self.get_tile_ch_to_node()
        len0 = len(self.mosaic)
        len1 = len(self.mosaic[0])
        node_to_tile_loc = {}
        for row in range(len0):
            for col in range(len1):
                tile_ch = self.mosaic[row][col]
                if tile_ch != DAG.empty_tile:
                    node = tile_ch_to_node[tile_ch]
                    node_to_tile_loc[node] = (row, col)
        return node_to_tile_loc

    def set_parentage(self):
        """
        This method fills the dictionaries `self.child_to_parents` and 
        `self.parent_to_children`.
        
        Returns
        -------
        None

        """
        self.child_to_parents = {}
        for child in self.nodes:
            self.child_to_parents[child] = [
                self.name_to_node[parent_name] for
                parent_name in child.parent_names]
        self.parent_to_children = {}
        for parent in self.nodes:
            self.parent_to_children[parent] = []
            for child in self.nodes:
                if parent in self.child_to_parents[child] and \
                        child not in self.parent_to_children[parent]:
                    self.parent_to_children[parent].append(child)

    def get_long_str(self,
                     str0,
                     add_superscripts=True,
                     underline=True):
        """
        This method returns the str `str0` after replacing in it,
        every occurrence of a node name enclosed in double quotes, by that
        same node name without the quotes and with a superscript added. The
        superscript shows the slice str for that node. For example, if "A_0"
        is a node with slice str "[5],[3]", it will replace every occurrence
        of '"A_0"' by "A_0^{[5],[3]}".
        
        Parameters
        ----------
        str0: str
        add_superscripts: bool
        underline: bool

        Returns
        -------
        str

        """
        for node in self.nodes:
            str0 = str0.replace('"' + node.name + '"',
                                Node.get_long_name(node,
                                                   add_superscripts,
                                                   underline))
        return str0

    def get_figure_str(self,
                       fig_header=None,
                       fig_footer=None,
                       fig_caption=None,
                       add_superscripts=True,
                       underline=True,
                       row_separation=None,
                       column_separation=None):
        """
        This method returns a LaTex string for drawing a bnet that 
        represents a neural net.
        
        Parameters
        ----------
        fig_header: str | None
        fig_footer: str | None
        fig_caption: str | None
        add_superscripts: bool
        underline: bool
        row_separation: float | None
        column_separation: float | None

        Returns
        -------
        str

        """
        fig_header = replace_none(fig_header)
        fig_footer = replace_none(fig_footer)
        fig_caption = replace_none(fig_caption)

        len0 = len(self.mosaic)
        len1 = len(self.mosaic[0])
        # print("llmg", self.mosaic)
        str0 = r"\begin{figure}[h!]\centering" + "\n"
        str0 += fig_header
        separation_str = ""
        # \xymatrix@C=1pc@R=1pc{
        if row_separation:
            assert row_separation > 0
            separation_str += "@R=" + str(row_separation) + "pc"
        if column_separation:
            assert column_separation > 0
            separation_str += "@C=" + str(column_separation) + "pc"

        str0 += r"$$\xymatrix" + separation_str + "{\n"
        tile_ch_to_node = self.get_tile_ch_to_node()
        for row in range(len0):
            for col in range(len1):
                if col != 0:
                    str0 += "&"
                parent_tile_ch = self.mosaic[row][col]
                if parent_tile_ch == DAG.empty_tile:
                    continue
                parent = tile_ch_to_node[parent_tile_ch]
                style_name = parent.style_name
                if parent.color and style_name == "plain":
                    style_name = "box"
                node_xy = NODE_STYLE_NAME_TO_XY_STR[style_name]
                if not parent.color:
                    node_xy = node_xy.replace("*:yellow", "")
                else:
                    node_xy = node_xy.replace("yellow", parent.color)
                str0 += node_xy + "{"
                long_name = Node.get_long_name(
                    parent,
                    add_superscripts,
                    underline)
                str0 += long_name + "}"
                for child in self.parent_to_children[parent]:
                    is_fancy_arrow = False
                    which_arrow = None
                    if self.fancy_arrows:
                        for fancy_arrow in self.fancy_arrows:
                            if fancy_arrow.recognize_endings(parent.name,
                                                             child.name):
                                is_fancy_arrow = True
                                which_arrow = fancy_arrow
                                break
                    child_row, child_col = self.node_to_tile_loc[child]
                    delta0 = child_row - row
                    delta1 = child_col - col
                    direction = ""
                    if delta0 > 0:
                        direction += "d" * delta0
                    elif delta0 < 0:
                        direction += "u" * (-delta0)
                    if delta1 > 0:
                        direction += "r" * delta1
                    elif delta1 < 0:
                        direction += "l" * (-delta1)
                    if not is_fancy_arrow:
                        str0 += r"\ar[" + direction + "]"
                    else:
                        str0 += which_arrow.get_xy_str(direction)
            str0 += "\n" + r"\\" + "\n"
        str0 = str0.strip()[:-2]
        if self.plates:
            str0 += r"\save" + "\n"
            for plate in self.plates:
                str0 += plate.get_xy_str() + "\n"
            str0 += r"\restore" + "\n"
            for plate in self.plates:
                if not plate.only_one_layer:
                    str0 += r"\\" + "\n"
                    xy_str0 = PLATE_STYLE_TO_XY_STR[plate.style_name]
                    str0 += "*+[F" + xy_str0 + "]{\;\;}&"
                    str0 += r"\text{$" + plate.num_layers_str + "$ layers}\n"
        str0 += "}$$\n"
        str0 += fig_footer
        str0 += r"\caption{" + fig_caption + "}\n"
        str0 += r"\label{fig-texnn-for-" + self.name + "}\n"
        str0 += r"\end{figure}"
        return str0

    def get_equations_str(self,
                          add_superscripts=True,
                          underline=False,
                          eqs_in_blue=True,
                          conditional_prob=False):
        """
        This method returns a LaTex string for writing the structure 
        equations of the bnet we are drawing.
        
        Parameters
        ----------
        add_superscripts: bool
        underline: bool
        eqs_in_blue: bool
            equations in blue
        conditional_prob: bool
            Suppose A is the node that an equation is about and B, C are its
            parents. If this is true, the equation starts "P(A|B,C)=",
            whereas if it's False, it starts "A=".

        Returns
        -------
        str

        """

        def get_parent_str(node):
            parent_str = ""
            num_parents = 0
            for parent in self.child_to_parents[node]:
                num_parents += 1
                parent_nameL = parent.name
                if add_superscripts:
                    parent_nameL = Node.get_long_name(
                        parent,
                        add_superscripts,
                        underline)
                parent_str += parent_nameL + ","
            if num_parents > 0:
                parent_str = parent_str[:-1]
            return parent_str

        str0 = "\n\n" + r"\begin{subequations}" + "\n\n"
        blue_str = r"\color{blue}" if eqs_in_blue else ""
        for node in self.nodes:
            str0 += r"\begin{equation}" + blue_str + "\n"
            node_nameL = Node.get_long_name(node,
                                            add_superscripts,
                                            underline)
            if not conditional_prob:
                str0 += node_nameL + " = "
            else:
                str0 += "P(" + node_nameL
                if node.parent_names:
                    str0 += "|" + get_parent_str(node)
                if node.params_str:
                    str0 += ";" + node.params_str
                str0 += ")="
            if node.full_right_side_of_eq:
                str0 += node.full_right_side_of_eq + "\n"
                str0 += r"\end{equation}" + "\n\n"
                continue

            fun_args_strL = node.fun_args_str
            if add_superscripts:
                if node.fun_args_str:
                    fun_args_strL = self.get_long_str(
                        node.fun_args_str,
                        add_superscripts,
                        underline)
            open_paren = "("
            close_paren = ")"
            if not node.fun_name:
                node.fun_name = ""
                open_paren = ""
                close_paren = ""
            str0 += node.fun_name + open_paren
            if node.fun_args_str:
                str0 += fun_args_strL
            if not conditional_prob:
                if not node.fun_args_str:
                    str0 += get_parent_str(node)
                semicolon = ";" if node.parent_names else ""
                if node.params_str:
                    str0 += semicolon + node.params_str
            str0 += close_paren
            if node.post_eq_comment:
                str0 += r"\;\;\text{" + node.post_eq_comment + "}"
            str0 += "\n" + r"\label{eq-" + node.tile_ch + \
                    "-fun-" + self.name + "}\n"
            str0 += r"\end{equation}" + "\n\n"
        str0 += r"\end{subequations}"
        return str0

    @staticmethod
    def get_tile_arr_from_mosaic(mosaic):
        """
        This method converts `mosaic` to a numpy array of characters.

        Parameters
        ----------
        mosaic: list[str]

        Returns
        -------
        np.array

        """
        len0 = len(mosaic)
        len1 = len(mosaic[0])
        tile_arr = np.empty(shape=(len0, len1), dtype='U')
        for row in range(len0):
            for col in range(len1):
                tile_arr[row][col] = mosaic[row][col]
        return tile_arr

    @staticmethod
    def get_mosaic_from_tile_array(tile_arr):
        """
        This method converts a numpy array of characters `tile_arr` to an
        mosaic.

        Parameters
        ----------
        tile_arr: np.array

        Returns
        -------
        list[str]

        """
        len0, len1 = tile_arr.shape
        mosaic = []
        for row in range(len0):
            row_str = ""
            for ch in tile_arr[row][:]:
                row_str += ch
            mosaic.append(row_str)
        # print("llkm", tile_arr, mosaic)
        return mosaic

    @staticmethod
    def rotate_mosaic(mosaic, how):
        """
        This method returns a rotated version of `mosaic`. It can rotate by
        +90, +180 and +270 degrees.

        Parameters
        ----------
        mosaic: list[str]
        how: str
            must be in ["+90_degs", "+180_degs", "+270_degs']

        Returns
        -------
        list[str]

        """
        tile_arr = DAG.get_tile_arr_from_mosaic(mosaic)
        if how == "+90_degs":
            new_tile_arr = np.rot90(tile_arr)
            # print("jjlw", tile_arr, new_tile_arr)
        elif how == "+180_degs":
            new_tile_arr = np.rot90(np.rot90(tile_arr))
        elif how == "+270_degs":
            new_tile_arr = np.rot90(np.rot90(np.rot90(tile_arr)))
        else:
            assert False, "illegal rotation str"
        return DAG.get_mosaic_from_tile_array(new_tile_arr)

    def write_tex_file(self,
                       fig_header=None,
                       fig_footer=None,
                       fig_caption=None,
                       add_superscripts=True,
                       underline=True,
                       header=HEADER0,
                       footer=FOOTER0,
                       eqs_in_blue=True,
                       conditional_prob=False,
                       row_separation=None,
                       column_separation=None):
        """
        This method writes a .tex file with the figure and the equations.

        Parameters
        ----------
        fig_header: str | None
        fig_footer: str | None
        fig_caption: str | None
        add_superscripts: bool
        underline: bool
        header: str
        footer: str
        eqs_in_blue: bool
        conditional_prob: bool
        row_separation: float | None
        column_separation: float |None

        Returns
        -------
        None

        """
        str0 = ""
        str0 += header
        str0 += self.get_figure_str(
            fig_header=fig_header,
            fig_footer=fig_footer,
            fig_caption=fig_caption,
            add_superscripts=add_superscripts,
            underline=underline,
            row_separation=row_separation,
            column_separation=column_separation)
        str0 += self.get_equations_str(
            add_superscripts=add_superscripts,
            underline=False,
            eqs_in_blue=eqs_in_blue,
            conditional_prob=conditional_prob)
        str0 += footer
        with open(self.name + ".tex", "w") as f:
            f.write(str0)


if __name__ == "__main__":
    def main1():
        mosaic = [
            "12",
            "34",
            "56"
        ]
        print("\nmosaic:\n", mosaic)
        tile_arr = DAG.get_tile_arr_from_mosaic(mosaic)
        print("tile_arr:\n", tile_arr)
        new_mosaic = DAG.get_mosaic_from_tile_array(tile_arr)
        print("new mosaic:\n", new_mosaic)
        print("rot90:\n", np.rot90(tile_arr))
        print("rot180:\n", np.rot90(np.rot90(tile_arr)))
        print("rot270:\n", np.rot90(np.rot90(np.rot90(tile_arr))))


    main1()
