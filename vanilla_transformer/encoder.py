from texnn import *

mosaic = [
    "n___",
    "_F__",
    "N___",
    "__O_",
    "_QKV",
    "p___",
    "R___"
]

noden = Node(
    name="n",
    tile_ch='n',
    parent_names=["N", "F"],
    slice_str="[d], [\ell]",
    fun_name="normalize",
    fun_args_str='"N" + "F"',
    params_str=None,
    color="yellow"
)

nodeF = Node(
    name="F",
    tile_ch='F',
    parent_names=["N"],
    slice_str="[d], [\ell]",
    fun_name="feed_forward_nn",
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)

nodeN = Node(
    name="N",
    tile_ch='N',
    parent_names=["e", "O"],
    slice_str="[d], [\ell]",
    fun_name="normalize",
    fun_args_str='"e" + "O"',
    params_str=None,
    color="yellow"
)

nodeO = Node(
    name="O",
    tile_ch='O',
    parent_names=["Q", "K", "V"],
    slice_str="[d], [\ell]",
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
    fun_args_str=r'W_\rvq^{[D], [d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodeK = Node(
    name="K",
    tile_ch='K',
    parent_names=["e"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvk^{[D], [d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodeV = Node(
    name="V",
    tile_ch='V',
    parent_names=["e"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvv^{[D], [d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodep = Node(
    name="e",
    tile_ch='p',
    parent_names=["x"],
    slice_str="[d], [\ell]",
    fun_name=None,
    fun_args_str='E^{[\Lambda],[d], [L]}"x"',
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
    params_str=None,
    color="Lavender",
    post_eq_comment="prior"
)

nodes = [
    noden,
    nodeF,
    nodeN,
    nodeO,
    nodeQ, nodeK, nodeV,
    nodep,
    nodeR
]

plate0 = Plate(
    first_and_last_row=(0,6),
    first_and_last_col=(0,3),
    num_layers_str= r"\Lambda",
    margin= 4.0
)

plates = [plate0]

print("\nmosaic:", mosaic)
name = "encoder"
dag = DAG(name, mosaic, nodes, plates=plates)
fig_header = \
r"""\begin{minipage}{.4\linewidth}
\includegraphics[width=2in]{encoder.jpg}
\end{minipage}%blank lines between minispaces breaks this
\begin{minipage}{.6\linewidth}
"""

fig_footer = \
"""\end{minipage}
"""
dag.write_tex_file(fig_header,
                   fig_footer,
                   fig_caption="Encoder.",
                   header=BAY_HEADER,
                   column_separation=.1,
                   row_separation=2.5)
