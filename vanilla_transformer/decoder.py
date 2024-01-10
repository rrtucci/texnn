from texnn import *

mosaic = [
    "___G",
    "___I",
    "___Y",
    "__B_",
    "___j",
    "_O__",
    "qkva",
    "_o__",
    "QKV_",
    "___p",
    "___R"
]

nodeG=Node(
    name="P",
    tile_ch='G',
    parent_names=["I"],
    slice_str="[L],[\ell]",
    fun_name="softmax",
    fun_args_str=None,
    params_str=None,
    color="SpringGreen",
    post_eq_comment=r"$(\sum_{\alp\in[\ell]}P^{[L], \alp}=1)$"
)
nodeI=Node(
    name="I",
    tile_ch='I',
    parent_names=["Y"],
    slice_str="[L],[\ell]",
    fun_name=None,
    fun_args_str='W^{[L], [D]}"Y"',
    params_str=None,
    color="Orchid"
)
nodeY=Node(
    name="Y",
    tile_ch='Y',
    parent_names=["F", "j"],
    slice_str="[D], [\ell]",
    fun_name="normalize",
    fun_args_str='"F" + "a"',
    params_str=None,
    color="yellow"
)
nodeB= Node(
    name="F",
    tile_ch='B',
    parent_names=["j"],
    slice_str="[D], [\ell]",
    fun_name="feed_forward_nn",
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)
nodey=Node(
    name="j",
    tile_ch='j',
    parent_names=["o", "a"],
    slice_str="[D], [\ell]",
    fun_name="normalize",
    fun_args_str='"o" + "a"',
    params_str=None,
    color="yellow"
)
nodeO=Node(
    name="o",
    tile_ch='O',
    parent_names=["q", "k", "v"],
    slice_str="[D],[\ell]",
    fun_name="multi_head_attention",
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodea=Node(
    name="a",
    tile_ch='a',
    parent_names=["O", "e"],
    slice_str="[D], [\ell]",
    fun_name="normalize",
    fun_args_str='"O" + "e"',
    params_str=None,
    color="yellow"
)
nodev=Node(
    name="v",
    tile_ch='v',
    parent_names=["a"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str='"a"',
    params_str=None,
    color="Dandelion"
)

nodeo=Node(
    name="O",
    tile_ch='o',
    parent_names=["Q", "K", "V"],
    slice_str="[D],[\ell]",
    fun_name="multi_head_attention",
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeQ=Node(
    name="Q",
    tile_ch='Q',
    parent_names=["e"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvq^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)
nodeK=Node(
    name="K",
    tile_ch='K',
    parent_names=["e"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvk^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)
nodeV=Node(
    name="V",
    tile_ch='V',
    parent_names=["e"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvv^{[D],[d]}"e"',
    color="Dandelion"
)
nodep=Node(
    name="e",
    tile_ch='p',
    parent_names=["x"],
    slice_str="[d],[\ell]",
    fun_name=None,
    fun_args_str=r'E^{[d],[L]}"x"',
    params_str=None,
    color="gray"
)
nodeR=Node(
    name="x",
    tile_ch='R',
    parent_names=[],
    slice_str="[L],[\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Lavender",
    post_eq_comment="prior"
)
nodeq=Node(
    name="q",
    tile_ch='q',
    parent_names=[],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion",
    post_eq_comment="prior, obtained from encoder."
)
nodek=Node(
    name="k",
    tile_ch='k',
    parent_names=[],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion",
    post_eq_comment="prior, obtained from encoder."
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
