from texnn import *

nodeq = Node(
    name="q",
    tile_ch='q',
    parent_names=["n"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodek = Node(
    name="k",
    tile_ch='k',
    parent_names=["n"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)

noden = Node(
    name="n",
    tile_ch='n',
    parent_names=["N", "F"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

nodeF = Node(
    name="F",
    tile_ch='F',
    parent_names=["N"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="blue"
)

nodeN = Node(
    name="N",
    tile_ch='N',
    parent_names=["p", "O"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

nodeO = Node(
    name="O",
    tile_ch='O',
    parent_names=["Q", "K", "V"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)

nodeQ = Node(
    name="Q",
    tile_ch='Q',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)

nodeK = Node(
    name="K",
    tile_ch='K',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)

nodeV = Node(
    name="V",
    tile_ch='V',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

nodep = Node(
    name="p",
    tile_ch='p',
    parent_names=["R"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="gray"
)

nodeR = Node(
    name="R",
    tile_ch='R',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="red"
)


nodes = [
    nodeq,
    nodek,
    noden,
    nodeF,
    nodeN,
    nodeO,
    nodeQ, nodeK, nodeV,
    nodep,
    nodeR
]

mosaic = [
    "____q",
    "____k",
    "n____",
    "_F___",
    "N____",
    "__O__",
    "_QKV_",
    "p____",
    "R____"
]

name = "encoder"
dag = DAG(nodes, mosaic, name)
dag.write_tex_file(fig_caption="Encoder")
