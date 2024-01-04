from texnn import *

nodeQ = Node(
    name="Q",
    tile_ch="Q",
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

nodeK = Node(
    name="K",
    tile_ch="K",
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

nodeV = Node(
    name="V",
    tile_ch="V",
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

node1 = Node(
    name="1",
    tile_ch="1",
    parent_names=["Q"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

node2 = Node(
    name="2",
    tile_ch="2",
    parent_names=["Q"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

node3 = Node(
    name="3",
    tile_ch="3",
    parent_names=["Q"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

node4 = Node(
    name="4",
    tile_ch="4",
    parent_names=["K"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)
node5 = Node(
    name="5",
    tile_ch="5",
    parent_names=["K"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

node6 = Node(
    name="6",
    tile_ch="6",
    parent_names=["K"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

node7 = Node(
    name="7",
    tile_ch="7",
    parent_names=["V"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

node8 = Node(
    name="8",
    tile_ch="8",
    parent_names=["V"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

node9 = Node(
    name="9",
    tile_ch="9",
    parent_names=["V"],
    shape_str="(3, 4)",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="green"
)

nodeX = Node(
    name="X",
    tile_ch="X",
    parent_names=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    shape_str="(3, 4)",
    fun_name="scaled_dot_prod_att",
    fun_args_str=None,
    params_str=None,
    color="blue"
)


nodeY = Node(
    name="Y",
    tile_ch="Y",
    parent_names=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    shape_str="(3, 4)",
    fun_name="scaled_dot_prod_att",
    fun_args_str=None,
    params_str=None,
    color="blue"
)

nodeZ = Node(
    name="Z",
    tile_ch="Z",
    parent_names=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    shape_str="(3, 4)",
    fun_name="scaled_dot_prod_att",
    fun_args_str=None,
    params_str=None,
    color="blue"
)

nodeC = Node(
    name="C",
    tile_ch="C",
    parent_names=["X", "Y", "Z"],
    shape_str="(3, 4)",
    fun_name="concat",
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

nodeL = Node(
    name="L",
    tile_ch="L",
    parent_names=["C"],
    shape_str="(3, 4)",
    fun_name="concat",
    fun_args_str=None,
    params_str=None,
    color="yellow"
)


nodes = [
    nodeQ, nodeK, nodeV,
    node1, node2, node3, node4, node5, node6, node7, node8, node9,
    nodeX, nodeY, nodeZ,
    nodeC,
    nodeL
]
ll_tile = [
    "____L____",
    "____C____",
    "_X__Y__Z_",
    "123456789",
    "_Q__K__V_"
]
name = "multi-head-att"
dag = DAG(nodes, ll_tile, name)
print()
print(dag.get_figure_str(
    fig_caption="Multi-head Attention."))
print()
print(dag.get_equations_str())