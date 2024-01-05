from texnn import *

mosaic = [
    "___G",
    "___I",
    "___Y",
    "__B_",
    "___j",
    "O___",
    "___a",
    "__o_",
    "_QKV",
    "___p",
    "___R",
    "qv_i"
]

nodeG=Node(
    name="G",
    tile_ch='G',
    parent_names=["I"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="green"
)
nodeI=Node(
    name="I",
    tile_ch='I',
    parent_names=["Y"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="purple"
)
nodeY=Node(
    name="Y",
    tile_ch='Y',
    parent_names=["B", "a"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)
nodeB= Node(
    name="B",
    tile_ch='B',
    parent_names=["a"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="blue"
)
nodey=Node(
    name="j",
    tile_ch='j',
    parent_names=["O", "a"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)
nodeO=Node(
    name="O",
    tile_ch='O',
    parent_names=["q", "v", "a"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodea=Node(
    name="a",
    tile_ch='a',
    parent_names=["o", "p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)
nodeo=Node(
    name="o",
    tile_ch='o',
    parent_names=["Q", "K", "V"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodeQ=Node(
    name="Q",
    tile_ch='Q',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodeK=Node(
    name="K",
    tile_ch='K',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodeV=Node(
    name="V",
    tile_ch='V',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodep=Node(
    name="p",
    tile_ch='p',
    parent_names=["R"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="gray"
)
nodeR=Node(
    name="R",
    tile_ch='R',
    parent_names=["i"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="red"
)
nodeq=Node(
    name="q",
    tile_ch='q',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodev=Node(
    name="v",
    tile_ch='v',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="orange"
)
nodei=Node(
    name="i",
    tile_ch='i',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)

nodes = [
    nodeG,
    nodeI,
    nodeY,
    nodeB,
    nodey,
    nodeO,
    nodea,
    nodeo,
    nodeQ, nodeK, nodeV,
    nodep,
    nodeR,
    nodeq, nodev, nodei]
name = "decoder"
dag = DAG(nodes, mosaic, name)
dag.write_tex_file(fig_caption="Decoder")