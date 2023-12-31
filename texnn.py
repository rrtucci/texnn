"""
XYpic is a LaTex package for drawing network graphs with LaTex.

This stand-alone python file takes as input a bunch of strings for each node
of a Neural Net (nn).

The function DAG.get_figure_str() outputs a LaTex (tex) str for a figure
containing XYpic code for drawing a bnet that represents the NN.

The function DAG.get_equations_str() outputs a LaTex (tex) str for the
structural equations for a bnet of the NN.

"""



class Node:
    """
    
    Attributes
    ----------
    color: str
        the color of the node in the bnet
    fun_args_str: str
        function arguments str
    fun_name: str
    name: str
    params_str: str
    parent_names: list[str]
    shape_str: str
    """
    def __init__(self,
                 name,
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
        parent_names: list[str]
        shape_str: str
        fun_name: str
        fun_args_str: str
        params_str: str
        color: str
        """
        self.name = name
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
        
        Parameters
        ----------
        shape_str:str

        Returns
        -------
        str

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
    
    Attributes
    ----------
    child_to_parents: dict[Node, list[Node]]
    empty_tile: str
    ll_tile: list[list[str]]
    node_to_tile_loc: list[Node, tuple[int]]
    nodes: list[Node]
    parent_to_children: dict[Node, list[Node]]
    
    
    """
    empty_tile = "_"

    def __init__(self, nodes, ll_tile):
        """
        
        Parameters
        ----------
        nodes: list[Node]
        ll_tile: list[list[str]]
        """
        self.nodes = nodes
        self.ll_tile = ll_tile
        self.node_to_tile_loc = None
        self.parent_to_children = None
        self.child_to_parents = None
        self.set_node_tile_locs()
        self.set_parentage()

    def get_node(self, node_name):
        """
        
        Parameters
        ----------
        node_name: str

        Returns
        -------
        Node

        """
        node = None
        for node0 in self.nodes:
            if node0.name == node_name:
                node = node0
                break
        if node:
            return node
        else:
            assert False, f"'{node_name}' is not in: " + \
                          str([node0.name for node0 in self.nodes])

    def set_node_tile_locs(self):
        """
        
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
                node_name = self.ll_tile[row][col]
                if node_name != DAG.empty_tile:
                    node = self.get_node(node_name)
                    self.node_to_tile_loc[node] = (row, col)

    def set_parentage(self):
        """
        
        Returns
        -------
        None

        """
        self.child_to_parents = {}
        for child in self.nodes:
            self.child_to_parents[child] = [self.get_node(parent_name) for
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
                if col !=0:
                    str0 += "&"
                parent_name = self.ll_tile[row][col]
                if parent_name == DAG.empty_tile:
                    continue
                parent = self.get_node(parent_name)
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
            str0 += r"\label{" + fig_label + "}\n"
        str0 += r"\end{figure}"
        return str0

    def get_equations_str(self, add_superscripts=True):
        """
        
        Parameters
        ----------
        add_superscripts: bool

        Returns
        -------
        str

        """
        str0 = r"\begin{subequations}" + "\n"
        for parent in self.nodes:
            str0 += r"\begin{equation}" + "\n"
            parent_nameL = parent.name
            fun_args_strL = parent.fun_args_str
            if add_superscripts:
                parent_nameL = Node.get_long_name(parent)
                if parent.fun_args_str:
                    fun_args_strL = self.get_long_str(parent.fun_args_str)
            str0 += parent_nameL + " = " + parent.fun_name + "("
            if parent.fun_args_str:
                str0 += fun_args_strL + ")"
            else:
                for child in self.parent_to_children[parent]:
                    child_nameL = child.name
                    if add_superscripts:
                        child_nameL = Node.get_long_name(child)
                    str0 += child_nameL + ","
                if parent.params_str:
                    str0 += parent.params_str + ","
                str0 = str0[:-1] + ")"
            str0 += "\n" + r"\end{equation}" + "\n\n"
        str0 += r"\end{subequations}"
        return str0


if __name__ == "__main__":
    def main():
        anode = Node(
            name="A",
            parent_names=[],
            shape_str="(3, 4)",
            fun_name="fun_a",
            fun_args_str=None,
            params_str="axis=1",
            color="yellow"
        )
        bnode = Node(
            name="B",
            parent_names=["A"],
            shape_str="(3,)",
            fun_name="fun_b",
            fun_args_str=None,
            params_str=None,
            color="Lavender"
        )
        cnode = Node(
            name="C",
            parent_names=["A", "B"],
            shape_str="(4,)",
            fun_name="fun_c",
            fun_args_str="BA+b^4",
            params_str=None,
            color="cyan"
        )
        nodes = [anode, bnode, cnode]
        ll_tile = [
            "_B_",
            "A_C",
        ]
        dag = DAG(nodes, ll_tile)
        print()
        print(dag.get_figure_str(fig_caption="Boring bnet",
                                 fig_label="fig-boring"))
        print()
        print(dag.get_equations_str())


    main()
