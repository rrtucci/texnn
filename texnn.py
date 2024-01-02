"""

texnn (pronounced like "Texan") is a Python script that outputs LaTex (tex)
strings for visualizing a Neural Net (nn) as a causal DAG (Bayesian Network).

texnn is a stand-alone app, although I wrote it specifically to aid me in
writing a chapter on transformer architectures for my free, open source book
Bayesuvius.

texnn uses the LaTex package xy-pic for drawing.

texnn takes as input a bunch of strings with info for each node of a Neural 
Net (NN).

The function DAG.get_figure_str() outputs a LaTex str for drawing via xy-pic 
a bnet that represents the NN.

The function DAG.get_equations_str() outputs a LaTex str for writing the 
structural equations for a bnet that represents the NN.

"""


class Node:
    """
    This class just stores a bunch of strings with info about a node.
    
    Attributes
    ----------
    color: str
        the color of node `self` in the bnet
    fun_args_str: str
        the string of function arguments
    fun_name: str
        the name of the function which equals `self`
    name: str
        a name that identifies the node uniquely
    params_str: str
        a str containing parameter names and their values
    parent_names: list[str]
        a list of the names of the parents of node `self`.
    shape_str: str
        the string of the shape of the output of node `self`. For example, 
        "(3, )", "(4, 3)", "(N, M)"
    tile_ch: str
        tile character, a character that identifies the node uniquely
    """

    def __init__(self,
                 name,
                 tile_ch,
                 parent_names,
                 shape_str,
                 fun_name,
                 fun_args_str=None,
                 params_str=None,
                 color=None):
        """
        
        Parameters
        ----------
        name: str
        tile_ch: str
        parent_names: list[str]
        shape_str: str
        fun_name: str
        fun_args_str: str
        params_str: str
        color: str
        """
        self.name = name
        assert len(tile_ch) == 1
        self.tile_ch = tile_ch
        self.parent_names = parent_names

        def rm_str(str0):
            if str0:
                return r"{\rm " + str0.replace("_", "\_") + "}"
            else:
                return ""

        self.shape_str = shape_str
        self.fun_name = rm_str(fun_name)
        self.fun_args_str = fun_args_str
        self.params_str = rm_str(params_str)
        self.color = color

    @staticmethod
    def get_dimensions_str(shape_str):
        """
        This method takes as input a tensor shape string and returns as 
        output a dimensions string. For example. "(8, 5, 3)" ->"8X5X3"
        
        Parameters
        ----------
        shape_str:str
            tensor shape string

        Returns
        -------
        str
            dimensions string

        """
        # remove parentheses
        str0 = shape_str.strip()[1:-1].strip(",")
        l_ch = str0.split(",")
        shape_len = len(l_ch)
        str1 = ""
        if shape_len == 1:
            return l_ch[0]
        for i in range(shape_len):
            if i != shape_len - 1:
                str1 += l_ch[i] + r"\times "
            else:
                str1 += str(l_ch[i])
        return str1

    @staticmethod
    def get_long_name(node, underline_it=False):
        """
        This method takes as input a node name and underlines it iff 
        underline = True. In addition, output string adds to the input 
        string a superscript with its dimensions str.
        
        Parameters
        ----------
        node: Node
        underline_it: bool

        Returns
        -------
        str

        """
        node_name = node.name
        if underline_it:
            node_name = r"\underline{" + node.name + r"}"
        return node_name + "^{" + Node.get_dimensions_str(
            node.shape_str) + "}"


class DAG:
    """
    This class has methods for drawing a NN (via xy-pic) and writing its 
    structural equations.
    
    Attributes
    ----------
    child_to_parents: dict[Node, list[Node]]
        a dictionary mapping each node to a list of its parent nodes
    empty_tile: str
        str for an empty tile,usually "_" 
    ll_tile: list[str]
        a list of string which when stacked horizontally represent
        the bnet that we wish to draw, as a tile mosaic, with one or zero 
        nodes per tile.
    node_to_tile_loc: list[Node, tuple[int]]
        a dictionary mapping each node to its tile location, which
        should be a tuple (row, col).
    nodes: list[Node]
        the list of nodes in the bnet that we wish to draw
    parent_to_children: dict[Node, list[Node]]
        A dictionary mapping every node to a list of its children
    
    
    """
    empty_tile = "_"

    def __init__(self, nodes, ll_tile, name):
        """
        
        Parameters
        ----------
        nodes: list[Node]
        ll_tile: list[str]
        fig_label: str
        """
        self.nodes = nodes
        self.ll_tile = ll_tile
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
        len0 = len(self.ll_tile)
        len1 = len(self.ll_tile[0])
        for row in range(len0):
            assert len(self.ll_tile[row]) == len1, \
                "Tile rows not all of same length."
        self.node_to_tile_loc = {}
        for row in range(len0):
            for col in range(len1):
                tile_ch = self.ll_tile[row][col]
                
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
            self.child_to_parents[child] = [self.get_node_from_name(parent_name) for
                                            parent_name in child.parent_names]
        self.parent_to_children = {}
        for parent in self.nodes:
            self.parent_to_children[parent] = []
            for child in self.nodes:
                if parent in self.child_to_parents[child] and \
                        child not in self.parent_to_children[parent]:
                    self.parent_to_children[parent].append(child)

    def get_long_str(self, str0):
        """
        This method returns the str `str0` after replacing in it every 
        occurrence of a node name by that same node name with a superscript 
        added. The superscript shows the dimensions str for that node.
        
        Parameters
        ----------
        str0: str

        Returns
        -------
        str

        """
        for node in self.nodes:
            str0 = str0.replace(node.name, Node.get_long_name(node))
        return str0

    def get_figure_str(self,
                       fig_caption=None,
                       fig_label=None,
                       add_superscripts=True):
        """
        This method returns a LaTex string for drawing a bnet that 
        represents a neural net.
        
        Parameters
        ----------
        fig_caption: str
        fig_label: str
        add_superscripts: bool

        Returns
        -------

        """
        len0 = len(self.ll_tile)
        len1 = len(self.ll_tile[0])
        str0 = r"\begin{figure}[h!]\centering" + "\n"
        str0 += r"$$\xymatrix{" + "\n"
        for row in range(len0):
            for col in range(len1):
                if col != 0:
                    str0 += "&"
                parent_tile_ch = self.ll_tile[row][col]
                if parent_tile_ch == DAG.empty_tile:
                    continue
                parent = self.get_node_from_tile_ch(parent_tile_ch)
                box_str = r"*+[F*]{"
                if parent.color:
                    box_str = r"*+[F*:" + parent.color + "]{"
                str0 += box_str
                long_name = r"\underline{" + parent.name + "}"
                if add_superscripts:
                    long_name = Node.get_long_name(parent, underline_it=True)
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
        if fig_caption:
            str0 += r"\caption{" + fig_caption + "}\n"
        if fig_label:
            str0 += r"\label{fig-" + fig_label + "}\n"
        str0 += r"\end{figure}"
        return str0

    def get_equations_str(self, add_superscripts=True):
        """
        This method returns a LaTex string for writing the structure 
        equations of the bnet we are drawing.
        
        Parameters
        ----------
        add_superscripts: bool

        Returns
        -------
        str

        """
        str0 = r"\begin{subequations}" + "\n"
        for child in self.nodes:
            str0 += r"\begin{equation}" + "\n"
            child_nameL = child.name
            fun_args_strL = child.fun_args_str
            if add_superscripts:
                child_nameL = Node.get_long_name(child)
                if child.fun_args_str:
                    fun_args_strL = self.get_long_str(child.fun_args_str)
            open_paren = "("
            close_paren = ")"
            if not child.fun_name:
                open_paren = ""
                close_paren = ""
            str0 += child_nameL + " = " + child.fun_name + open_paren
            if child.fun_args_str:
                str0 += fun_args_strL + close_paren
            else:
                for parent in self.child_to_parents[child]:
                    parent_nameL = parent.name
                    if add_superscripts:
                        parent_nameL = Node.get_long_name(parent)
                    str0 += parent_nameL + ","
                if child.params_str:
                    str0 += child.params_str + ","
                str0 = str0[:-1] + ")"
            str0 += "\n" + r"\label{eq-" + child.name + \
                    "-fun-" + self.name + "}\n"
            str0 += r"\end{equation}" + "\n\n"
        str0 += r"\end{subequations}"
        return str0


if __name__ == "__main__":
    def main():
        anode = Node(
            name="A",
            tile_ch = "A",
            parent_names=[],
            shape_str="(3, 4)",
            fun_name="fun_a",
            fun_args_str=None,
            params_str="axis=1",
            color="yellow"
        )
        bnode = Node(
            name="B",
            tile_ch="B",
            parent_names=["A"],
            shape_str="(3,)",
            fun_name="fun_b",
            fun_args_str=None,
            params_str=None,
            color="Lavender"
        )
        cnode = Node(
            name="C",
            tile_ch="C",
            parent_names=["A", "B"],
            shape_str="(4,)",
            fun_name=None,
            fun_args_str="BA+b^4",
            params_str=None,
            color="cyan"
        )
        dnode = Node(
            name="D",
            tile_ch="D",
            parent_names=["A", "B"],
            shape_str="(4,)",
            fun_name="cos",
            fun_args_str=None,
            params_str="axis=1",
            color="yellow"
        )
        nodes = [anode, bnode, cnode, dnode]
        ll_tile = [
            "_B_D",
            "A_C_",
        ]
        name = "silly-bnet"
        dag = DAG(nodes, ll_tile, name)
        print()
        print(dag.get_figure_str(fig_caption="Silly bnet",
                                 fig_label="silly"))
        print()
        print(dag.get_equations_str())


    main()
