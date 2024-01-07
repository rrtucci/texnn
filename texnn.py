"""

texnn (pronounced like "Texan") is a Python script that outputs LaTex (tex)
strings for visualizing a Neural Net (nn) as a causal DAG (Bayesian Network).

texnn is capable of reproducing with ease most of the xy-pic generated bnets
(Bayesian Networks) displayed in my book

[Bayesuvius](https://github.com/rrtucci/Bayesuvius)

texnn is a stand-alone app. I wrote it specifically to aid me in writing a
chapter on transformer architectures (see directory "vanilla_transformer")
for my free, open source book Bayesuvius. But I soon realized that it could
be easily converted into a general tool that is independent of the transformer
topic and of Bayesuvius.

texnn uses the LaTex package xy-pic for drawing.

texnn takes as input a bunch of strings with info for each node of a Neural 
Net (NN).

The function DAG.get_figure_str() outputs a LaTex str for drawing via xy-pic 
a bnet that represents the NN.

The function DAG.get_equations_str() outputs a LaTex str for writing the 
structural equations for a bnet that represents the NN.

"""
import numpy as np
from globals import *


class Node:
    """
    This class just stores a bunch of strings with info about a node.
    
    Attributes
    ----------
    color: str | None
        the color of node
    fun_args_str: str | None
        the string of function arguments
    fun_name: str | None
        the name of the function
    name: str
        a name that identifies the node uniquely. We recommend that you input
        all node names in double quotes and all tile_ch in single quotes.
        That way, if you want to replace the name of a node from "A"
        to "B", and the tile_ch='A', you can do a replace of "A"  without
        changing the tile_ch.
    params_str: str | None
        a string containing parameter names and their values
    parent_names: list[str]
        a list of the names of the parents of the node.
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
                 slice_str,
                 fun_name=None,
                 fun_args_str=None,
                 params_str=None,
                 color=None,
                 style_name="plain"):
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
        style_name: str
        """

        self.name = name
        self.style_name = style_name
        assert len(tile_ch) == 1, \
            f"tile_ch has length > 1. {tile_ch}"
        self.tile_ch = tile_ch
        self.parent_names = parent_names

        def rm_str(str0):
            if str0:
                return r"{\rm " + str0.replace("_", "\_") + "}"
            else:
                return ""

        self.slice_str = slice_str
        self.fun_name = rm_str(fun_name)
        self.fun_args_str = fun_args_str
        self.params_str = params_str
        self.color = color

    @staticmethod
    def get_long_name(node,
                      add_superscript=True,
                      underline=True):
        """
        This method takes as input a node name and underlines it iff 
        underline = True. In addition, output string adds to the input 
        string a superscript with its slice str.
        
        Parameters
        ----------
        node: Node
        add_superscript: bool
        underline: bool

        Returns
        -------
        str

        """
        node_name = node.name
        if underline:
            node_name = r"\underline{" + node.name + r"}"
        if not node.slice_str or not add_superscript:
            return node_name
        else:
            return node_name + "^{" + node.slice_str + "}"


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
    mosaic: list[str]
        a list of strings of equal length which when stacked horizontally
        represent the bnet that we wish to draw, as a tile mosaic.
    node_to_tile_loc: list[Node, tuple[int]]
        a dictionary mapping each node to its tile location, which is a
        tuple (row, col).
    nodes: list[Node]
        list of nodes for the bnet that we wish to draw
    parent_to_children: dict[Node, list[Node]]
        A dictionary mapping every node to a list of its children. Leaf
        nodes have empty list.

    """
    empty_tile = "_"

    def __init__(self, nodes, mosaic, name):
        """
        
        Parameters
        ----------
        nodes: list[Node]
        mosaic: list[str]
        name: str
        """
        self.nodes = nodes
        tiles = [node.tile_ch for node in nodes]
        assert len(tiles) == len(set(tiles)), \
            "some tile character is repeated."
        self.mosaic = mosaic
        len0 = len(self.mosaic)
        len1 = len(self.mosaic[0])
        for row in range(len0):
            assert len(self.mosaic[row]) == len1, \
                f"Tile rows not all of same length.\n{self.mosaic}"
        self.name = name
        self.node_to_tile_loc = None
        self.parent_to_children = None
        self.child_to_parents = None
        self.set_node_tile_locs()
        self.set_parentage()

    def get_node_from_name(self, name):
        """
        This method returns the unique Node with name `name`.
        
        Parameters
        ----------
        name: str

        Returns
        -------
        Node

        """
        node = None
        for node0 in self.nodes:
            if node0.name == name:
                node = node0
                break
        if node:
            return node
        else:
            assert False, f"'{name}' is not in: " + \
                          str([node0.name for node0 in self.nodes])

    def get_node_from_tile_ch(self, tile_ch):
        """
        This method returns the unique Node with tile_ch `tile_ch`.

        Parameters
        ----------
        tile_ch: str

        Returns
        -------
        Node

        """
        node = None
        for node0 in self.nodes:
            if node0.tile_ch == tile_ch:
                node = node0
                break
        if node:
            return node
        else:
            assert False, f"'{tile_ch}' is not in: " + \
                          str([node0.tile_ch for node0 in self.nodes])

    def set_node_tile_locs(self):
        """
        This method fills the dictionary `self.node_to_tile_loc`
        
        Returns
        -------
        None

        """
        len0 = len(self.mosaic)
        len1 = len(self.mosaic[0])
        self.node_to_tile_loc = {}
        for row in range(len0):
            for col in range(len1):
                tile_ch = self.mosaic[row][col]

                if tile_ch != DAG.empty_tile:
                    node = self.get_node_from_tile_ch(tile_ch)
                    self.node_to_tile_loc[node] = (row, col)

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
                self.get_node_from_name(parent_name) for
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
                     add_superscript=True,
                     underline=True):
        """
        This method returns the str `str0` after replacing in it,
        every occurrence of a node name enclosed by angle brakets <>,
        by that same node name with a superscript added. The superscript
        shows the slice str for that node. For example, if "A_0" is a node
        with slice str "[5],[3]", it will replace every occurrence of
        "<A_0>" by "A_0^{[5],[3]}".
        
        Parameters
        ----------
        str0: str
        add_superscript: bool
        underline: bool

        Returns
        -------
        str

        """
        for node in self.nodes:
            str0 = str0.replace('<' + node.name + '>',
                                Node.get_long_name(node,
                                                   add_superscript,
                                                   underline))
        return str0

    def get_figure_str(self,
                       fig_header=None,
                       fig_footer=None,
                       fig_caption=None,
                       add_superscript=True,
                       underline=True):
        """
        This method returns a LaTex string for drawing a bnet that 
        represents a neural net.
        
        Parameters
        ----------
        fig_header: str | None
        fig_footer: str | None
        fig_caption: str | None
        add_superscript: bool
        underline: bool

        Returns
        -------

        """
        if not fig_header:
            fig_header = ""
        if not fig_footer:
            fig_footer = ""
        if not fig_caption:
            fig_caption = ""
        len0 = len(self.mosaic)
        len1 = len(self.mosaic[0])
        # print("llmg", self.mosaic)
        str0 = r"\begin{figure}[h!]\centering" + "\n"
        str0 += fig_header
        str0 += r"$$\xymatrix{" + "\n"
        for row in range(len0):
            for col in range(len1):
                if col != 0:
                    str0 += "&"
                parent_tile_ch = self.mosaic[row][col]
                if parent_tile_ch == DAG.empty_tile:
                    continue
                parent = self.get_node_from_tile_ch(parent_tile_ch)
                style_name = parent.style_name
                if parent.color and style_name=="plain":
                    style_name = "box"
                node_xy = NODE_STYLE_NAME_TO_XY_STR[style_name]
                if not parent.color:
                    node_xy = node_xy.replace("*:yellow", "")
                else:
                    node_xy = node_xy.replace("yellow", parent.color)
                str0 += node_xy + "{"
                long_name = Node.get_long_name(
                    parent,
                    add_superscript,
                    underline)
                str0 += long_name + "}"
                for child in self.parent_to_children[parent]:
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
                    str0 += r"\ar[" + direction + "]"
            str0 += "\n" + r"\\" + "\n"
        str0 = str0.strip()[:-2] + r"}$$" + "\n"
        str0 += fig_footer
        str0 += r"\caption{" + fig_caption + "}\n"
        str0 += r"\label{fig-texnn-for-" + self.name + "}\n"
        str0 += r"\end{figure}"
        return str0

    def get_equations_str(self,
                          add_superscript=True,
                          underline=False,
                          in_blue=True):
        """
        This method returns a LaTex string for writing the structure 
        equations of the bnet we are drawing.
        
        Parameters
        ----------
        add_superscript: bool
        underline: bool
        in_blue: bool

        Returns
        -------
        str

        """
        str0 = "\n\n" + r"\begin{subequations}" + "\n\n"
        blue_str = r"\color{blue}" if in_blue else ""
        for node in self.nodes:
            str0 += r"\begin{equation}" + blue_str + "\n"
            fun_args_strL = node.fun_args_str
            node_nameL = Node.get_long_name(node,
                                            add_superscript,
                                            underline)
            if add_superscript:
                if node.fun_args_str:
                    fun_args_strL = self.get_long_str(
                        node.fun_args_str,
                        add_superscript,
                        underline)
            open_paren = "("
            close_paren = ")"
            if not node.fun_name:
                open_paren = ""
                close_paren = ""
            str0 += node_nameL + " = " + node.fun_name + open_paren
            if node.fun_args_str:
                str0 += fun_args_strL + close_paren
            else:
                for parent in self.child_to_parents[node]:
                    parent_nameL = parent.name
                    if add_superscript:
                        parent_nameL = Node.get_long_name(
                            parent,
                            add_superscript,
                            underline)
                    str0 += parent_nameL + ","
                if node.params_str:
                    str0 += node.params_str + ","
                str0 = str0[:-1] + close_paren
            str0 += "\n" + r"\label{eq-" + node.name + \
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
            assert False
        return DAG.get_mosaic_from_tile_array(new_tile_arr)

    def write_tex_file(self,
                       fig_header=None,
                       fig_footer=None,
                       fig_caption=None,
                       add_sperscripts=True,
                       underline=True,
                       header=HEADER,
                       footer=FOOTER):
        """
        This method writes a .tex file with the figure and the equations.

        Parameters
        ----------
        fig_header: str
        fig_footer: str
        fig_caption: str
        add_sperscripts: bool
        underline: bool
        header: str
        footer: str

        Returns
        -------
        None

        """
        str0 = ""
        str0 += header
        str0 += self.get_figure_str(
            fig_header,
            fig_footer,
            fig_caption,
            add_sperscripts,
            underline)
        str0 += self.get_equations_str(add_sperscripts)
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
