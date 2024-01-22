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
    parent_names=["e", "A"],
    slice_str="[d], [\ell]",
    fun_name="normalize",
    fun_args_str=r'"e" + W_\rva^{[d],[D]}"A"',
    params_str=None,
    color="yellow"
)

nodeO = Node(
    name="A",
    tile_ch='O',
    parent_names=["Q", "K", "V"],
    slice_str="[D], [\ell]",
    fun_name="Attention",
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
    fun_args_str='E^{[d], [L]}"x"',
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

ek= FancyArrow(
    parent_name="e",
    child_name="K",
    superscript="W_\\rvk")

eq= FancyArrow(
    parent_name="e",
    child_name="Q",
    superscript="W_\\rvq")

ev= FancyArrow(
    parent_name="e",
    child_name="V",
    subscript="W_\\rvv")

an= FancyArrow(
    parent_name="A",
    child_name="N",
    subscript="W_\\rva")

fancy_arrows = [ek, eq, ev, an]

plate0 = Plate(
    first_and_last_row=(0,4),
    first_and_last_col=(0,3),
    margin= 6.0
)

plates = [plate0]

print("\nmosaic:", mosaic)
name = "encoder"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          plates=plates)
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
                   fig_caption="Encoder of Vanilla Transformer Net. $\Lam$ "
                               "copies of the boxed part are "
                               "connected in series.",
                   header=BAY_HEADER,
                   column_separation=.1,
                   row_separation=3.5)
