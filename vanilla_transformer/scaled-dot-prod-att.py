from texnn import *

Qnode = Node(
    name="Q",
    tile_ch="Q",
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)
Knode = Node(
    name="K",
    tile_ch="K",
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)
Vnode = Node(
    name="V",
    tile_ch="V",
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)
Bnode = Node(
    name="B",
    tile_ch="B",
    parent_names=["Q", "K"],
    shape_str="(3, 4)",
    fun_name="mat_mult",
    fun_args_str=None,
    params_str=None,
    color="blue"
)
Ynode = Node(
    name="Y",
    tile_ch="Y",
    parent_names=["B"],
    shape_str="(3, 4)",
    fun_name="scale",
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

Rnode = Node(
    name="R",
    tile_ch="R",
    parent_names=["Y"],
    shape_str="(3, 4)",
    fun_name="mask",
    fun_args_str=None,
    params_str=None,
    color="red"
)

Gnode = Node(
    name="G",
    tile_ch="G",
    parent_names=["R"],
    shape_str="(3, 4)",
    fun_name="softmax",
    fun_args_str=None,
    params_str=None,
    color="green"
)

Pnode = Node(
    name="P",
    tile_ch="P",
    parent_names=["G", "V"],
    shape_str="(3, 4)",
    fun_name="mat_mult",
    fun_args_str=None,
    params_str=None,
    color="purple"
)

nodes = [
    Qnode,
    Knode,
    Vnode,
    Bnode,
    Ynode,
    Rnode,
    Gnode,
    Pnode
]
ll_tile = [
    "___P",
    "_G__",
    "_R__",
    "_Y__",
    "_B__",
    "Q_KV",
]
name = "scaled-dot_prod_att"
dag = DAG(nodes, ll_tile, name)
print()
print(dag.get_figure_str(fig_caption="Scaled Dot Product Attention."))
print()
print(dag.get_equations_str())
