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
    "qv_R"
]

nodeG=Node(
    name="G",
    tile_ch='G',
    parent_names=["I"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)
nodeI=Node(
    name="I",
    tile_ch='I',
    parent_names=["Y"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Orchid"
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
    color="SkyBlue"
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
    color="Dandelion"
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
    color="Dandelion"
)
nodeQ=Node(
    name="Q",
    tile_ch='Q',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeK=Node(
    name="K",
    tile_ch='K',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeV=Node(
    name="V",
    tile_ch='V',
    parent_names=["p"],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
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
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Lavender"
)
nodeq=Node(
    name="q",
    tile_ch='q',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodev=Node(
    name="v",
    tile_ch='v',
    parent_names=[],
    shape_str="(3, 4)",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
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
    nodeq, nodev]
name = "decoder"
dag = DAG(nodes, mosaic, name)
fig_header =\
r"""\begin{minipage}{.5\linewidth}
\includegraphics[width=2in]{decoder.jpg}
\end{minipage}%blank lines between minispaces breaks this
\begin{minipage}{.5\linewidth}
"""

fig_footer=\
"""\end{minipage}
"""
dag.write_tex_file(fig_header,
                   fig_footer,
                   fig_caption="Decoder.")
