from texnn import *

mosaic = [
    "___G",
    "___I",
    "___Y",
    "__B_",
    "_O_j",
    "vkq_",
    "n__a",
    "_o__",
    "QKV_",
    "___p",
    "___R"
]

nodeG = Node(
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
nodeI = Node(
    name="I",
    tile_ch='I',
    parent_names=["Y"],
    slice_str="[L],[\ell]",
    fun_name=None,
    fun_args_str='W^{[L], [d]}"Y"',
    params_str=None,
    color="Orchid"
)
nodeY = Node(
    name="Y",
    tile_ch='Y',
    parent_names=["F", "j"],
    slice_str="[d], [\ell]",
    fun_name="normalize",
    fun_args_str='"F" + "J"',
    params_str=None,
    color="yellow"
)
nodeB = Node(
    name="F",
    tile_ch='B',
    parent_names=["j"],
    slice_str="[d], [\ell]",
    fun_name="feed_forward_nn",
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)
nodey = Node(
    name="j",
    tile_ch='j',
    parent_names=["a", "J"],
    slice_str="[d], [\ell]",
    fun_name="normalize",
    fun_args_str=r'U_\rva^{[d],[D]}"a" + "J"',
    params_str=None,
    color="yellow"
)
nodeO = Node(
    name="a",
    tile_ch='O',
    parent_names=["v", "k", "q"],
    slice_str="[D],[\ell]",
    fun_name="Attention",
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodea = Node(
    name="J",
    tile_ch='a',
    parent_names=["A", "e"],
    slice_str="[d], [\ell]",
    fun_name="normalize",
    fun_args_str=r'W_\rva^{[d], [D]}"A" + "e"',
    params_str=None,
    color="yellow"
)
nodev = Node(
    name="v",
    tile_ch='v',
    parent_names=["n"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'U_\rvv^{[D], [d]}"n"',
    params_str=None,
    color="Dandelion"
)

nodeo = Node(
    name="A",
    tile_ch='o',
    parent_names=["Q", "K", "V"],
    slice_str="[D],[\ell]",
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
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvv^{[D],[d]}"e"',
    color="Dandelion"
)
nodep = Node(
    name="e",
    tile_ch='p',
    parent_names=["x"],
    slice_str="[d],[\ell]",
    fun_name=None,
    fun_args_str=r'E^{[d],[L]}"x"',
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
    post_eq_comment="prior, right shifted output"
)
nodeq = Node(
    name="q",
    tile_ch='q',
    parent_names=["J"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'U_\rvq^{[D],[d]}"J"',
    params_str=None,
    color="Dandelion"
)
nodek = Node(
    name="k",
    tile_ch='k',
    parent_names=["n"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=r'U_\rvk^{[D],[d]}"n"',
    params_str=None,
    color="Dandelion"
)

noden = Node(
    name="n",
    tile_ch='n',
    parent_names=[],
    slice_str="[d], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow",
    post_eq_comment="Prior coming from Encoder."
)

nodes = [
    nodeG,
    nodeI,
    nodeY,
    nodeB,
    nodey,
    nodeO,
    nodea, nodeq,
    nodeo,
    nodeQ, nodeK, nodeV,
    nodep,
    nodeR,
    nodek, nodev, noden]

ek= FancyArrow(
    parent_name="e",
    child_name="K",
    subscript="W_\\rvk")

eq= FancyArrow(
    parent_name="e",
    child_name="Q",
    superscript="W_\\rvq")

ev= FancyArrow(
    parent_name="e",
    child_name="V",
    subscript="W_\\rvv")

aa= FancyArrow(
    parent_name="A",
    child_name="J",
    superscript="W_\\rva")

nk= FancyArrow(
    parent_name="n",
    child_name="k",
    subscript="U_\\rvk")

nq= FancyArrow(
    parent_name="J",
    child_name="q",
    superscript="U_\\rvq")

nv= FancyArrow(
    parent_name="n",
    child_name="v",
    superscript="U_\\rvv")

aj= FancyArrow(
    parent_name="a",
    child_name="j",
    superscript="U_\\rva")

fancy_arrows = [ek, eq, ev, aa,
                nk, nq, nv, aj]

plate0 = Plate(
    first_and_last_row=(2,8),
    first_and_last_col=(0,3),
    margin=6.0
)

plates = [plate0]

print("\nmosaic:", mosaic)
name = "decoder"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          plates=plates)
fig_header = \
r"""\begin{minipage}{.4\linewidth}
\includegraphics[width=2in]{decoder.jpg}
\end{minipage}%blank lines between minispaces breaks this
\begin{minipage}{.6\linewidth}
"""

fig_footer = \
"""\end{minipage}
"""
dag.write_tex_file(fig_header,
                   fig_footer,
                   fig_caption="Decoder of Vanilla Transformer Net. $\Lam$ "
                               "copies of the boxed part are "
                               "connected in series.",
                   header=BAY_HEADER,
                   column_separation=.2,
                   row_separation=3)
