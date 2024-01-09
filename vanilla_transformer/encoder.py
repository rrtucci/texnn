from texnn import *


mosaic = [
    "qk__",
    "n___",
    "_F__",
    "N___",
    "__O_",
    "_QKV",
    "p___",
    "R___"
]

nodeq = Node(
    name="q",
    tile_ch='q',
    parent_names=["n"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodek = Node(
    name="k",
    tile_ch='k',
    parent_names=["n"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)

noden = Node(
    name="n",
    tile_ch='n',
    parent_names=["N", "F"],
    slice_str="[D], [\ell]",
    fun_name="normalize",
    fun_args_str='"N" + "F"',
    params_str=None,
    color="yellow"
)

nodeF = Node(
    name="F",
    tile_ch='F',
    parent_names=["N"],
    slice_str="[D], [\ell]",
    fun_name="feed_forwrd_nn",
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)

nodeN = Node(
    name="N",
    tile_ch='N',
    parent_names=["e", "O"],
    slice_str="[D], [\ell]",
    fun_name="normalize",
    fun_args_str='"e" + "O"',
    params_str=None,
    color="yellow"
)

nodeO = Node(
    name="O",
    tile_ch='O',
    parent_names=["Q", "K", "V"],
    slice_str="[D], [\ell]",
    fun_name="multi_headed_attention",
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)

nodeQ = Node(
    name="Q",
    tile_ch='Q',
    parent_names=["e"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvq^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodeK = Node(
    name="K",
    tile_ch='K',
    parent_names=["e"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvk^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodeV = Node(
    name="V",
    tile_ch='V',
    parent_names=["e"],
    slice_str="[D],[\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvv^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodep = Node(
    name="e",
    tile_ch='p',
    parent_names=["x"],
    slice_str="[d], [\ell]",
    fun_name=None,
    fun_args_str='M^{[\ell], [\ell]}"x"',
    params_str=None,
    color="gray"
)

nodeR = Node(
    name="x",
    tile_ch='R',
    parent_names=[],
    slice_str="[L],[\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str="prior",
    color="Lavender"
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


name = "encoder"
dag = DAG(nodes, mosaic, name)
fig_header =\
r"""\begin{minipage}{.5\linewidth}
\includegraphics[width=2in]{encoder.jpg}
\end{minipage}%blank lines between minispaces breaks this
\begin{minipage}{.5\linewidth}
"""

fig_footer=\
"""\end{minipage}
"""
dag.write_tex_file(fig_header,
                   fig_footer,
                   fig_caption="Encoder.",
                   header=BAY_HEADER)
