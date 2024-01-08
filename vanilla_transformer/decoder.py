from texnn import *

mosaic = [
    "___G",
    "___I",
    "___Y",
    "__B_",
    "___j",
    "O___",
    "qkva",
    "_o__",
    "QKV_",
    "___p",
    "___R"
]

nodeG=Node(
    name="G",
    tile_ch='G',
    parent_names=["I"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)
nodeI=Node(
    name="I",
    tile_ch='I',
    parent_names=["Y"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)
nodeY=Node(
    name="Y",
    tile_ch='Y',
    parent_names=["F", "j"],
    slice_str="[D], [L]",
    fun_name="normalize",
    fun_args_str='"F" + "a"',
    params_str=None,
    color="yellow"
)
nodeB= Node(
    name="F",
    tile_ch='B',
    parent_names=["j"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)
nodey=Node(
    name="j",
    tile_ch='j',
    parent_names=["o", "a"],
    slice_str="[D], [L]",
    fun_name="normalize",
    fun_args_str='"o" + "a"',
    params_str=None,
    color="yellow"
)
nodeO=Node(
    name="o",
    tile_ch='O',
    parent_names=["q", "k", "v"],
    slice_str="[L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodea=Node(
    name="a",
    tile_ch='a',
    parent_names=["O", "p"],
    slice_str="[D], [L]",
    fun_name="normalize",
    fun_args_str='"O" + "p"',
    params_str=None,
    color="yellow"
)
nodev=Node(
    name="v",
    tile_ch='v',
    parent_names=["a"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str='"a"',
    params_str=None,
    color="Dandelion"
)

nodeo=Node(
    name="O",
    tile_ch='o',
    parent_names=["Q", "K", "V"],
    slice_str="[L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeQ=Node(
    name="Q",
    tile_ch='Q',
    parent_names=["p"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeK=Node(
    name="K",
    tile_ch='K',
    parent_names=["p"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeV=Node(
    name="V",
    tile_ch='V',
    parent_names=["p"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodep=Node(
    name="p",
    tile_ch='p',
    parent_names=["R"],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="gray"
)
nodeR=Node(
    name="R",
    tile_ch='R',
    parent_names=[],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Lavender"
)
nodeq=Node(
    name="q",
    tile_ch='q',
    parent_names=[],
    slice_str="[D], [L]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodek=Node(
    name="k",
    tile_ch='k',
    parent_names=[],
    slice_str="[D], [L]",
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
    nodea, nodev,
    nodeo,
    nodeQ, nodeK, nodeV,
    nodep,
    nodeR,
    nodeq, nodek]
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
                   fig_caption="Decoder.",
                   header=BAY_HEADER)
