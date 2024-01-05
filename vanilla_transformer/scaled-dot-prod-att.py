from texnn import *

mosaic = [
    "___P",
    "_G__",
    "_R__",
    "_Y__",
    "_B__",
    "Q_KV",
]

Qnode = Node(
    name="Q",
    tile_ch='Q',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
Knode = Node(
    name="K",
    tile_ch='K',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
Vnode = Node(
    name="V",
    tile_ch='V',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
Bnode = Node(
    name="B",
    tile_ch='B',
    parent_names=["Q", "K"],
    shape_str="(3, 4)",
    fun_name="mat_mult",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)
Ynode = Node(
    name="Y",
    tile_ch='Y',
    parent_names=["B"],
    shape_str="(3, 4)",
    fun_name="scale",
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

Rnode = Node(
    name="R",
    tile_ch='R',
    parent_names=["Y"],
    shape_str="(3, 4)",
    fun_name="mask",
    fun_args_str=None,
    params_str=None,
    color="Lavender"
)

Gnode = Node(
    name="G",
    tile_ch='G',
    parent_names=["R"],
    shape_str="(3, 4)",
    fun_name="softmax",
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)

Pnode = Node(
    name="P",
    tile_ch='P',
    parent_names=["G", "V"],
    shape_str="(3, 4)",
    fun_name="mat_mult",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
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
name = "scaled-dot-prod-att"
dag = DAG(nodes, mosaic, name)
dag.write_tex_file(fig_caption="Scaled Dot Product Attention.")
