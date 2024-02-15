from texnn import *

mosaic = [
    "____F____",
    "____C____",
    "___X_Y___",
    "1_24_57_8",
    "_Q__K__V_",
    "____e____"
]

mosaic = DAG.rotate_mosaic(mosaic, "+270_degs")

nodee = Node(
    name="e",
    tile_ch='e',
    parent_names=[],
    slice_str=r"[d], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SpringGreen",
    post_eq_comment="prior"
)

nodeQ = Node(
    name="Q",
    tile_ch='Q',
    parent_names=["e"],
    slice_str=r"[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvq^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodeK = Node(
    name="K",
    tile_ch='K',
    parent_names=["e"],
    slice_str=r"[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvk^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)

nodeV = Node(
    name="V",
    tile_ch='V',
    parent_names=["e"],
    slice_str=r"[D], [\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvv^{[D],[d]}"e"',
    params_str=None,
    color="Dandelion"
)

node1 = Node(
    name="Q_0",
    tile_ch='1',
    parent_names=["Q"],
    slice_str="[d],[\ell]",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="(split, then project a component)"
)

node2 = Node(
    name="Q_1",
    tile_ch='2',
    parent_names=["Q"],
    slice_str="[d],[\ell]",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="(split, then project a component)"
)

node4 = Node(
    name="K_0",
    tile_ch='4',
    parent_names=["K"],
    slice_str="[d],[\ell]",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="(split, then project a component)"
)
node5 = Node(
    name="K_1",
    tile_ch='5',
    parent_names=["K"],
    slice_str="[d],[\ell]",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="(split, then project a component)"
)

node7 = Node(
    name="V_0",
    tile_ch='7',
    parent_names=["V"],
    slice_str="[d],[\ell]",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="(split, then project a component)"
)

node8 = Node(
    name="V_1",
    tile_ch='8',
    parent_names=["V"],
    slice_str="[d],[\ell]",
    fun_name="linear",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="(split, then project a component)"
)

nodeX = Node(
    name="A_0",
    tile_ch='X',
    parent_names=["V_0", "K_0", "Q_0"],
    slice_str="[d],[\ell]",
    fun_name="Attention",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)


nodeY = Node(
    name="A_1",
    tile_ch='Y',
    parent_names=["V_1", "K_1", "Q_1"],
    slice_str="[d],[\ell]",
    fun_name="Attention",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)

nodeC = Node(
    name="A",
    tile_ch='C',
    parent_names=["A_0", "A_1"],
    slice_str="[D],[\ell]",
    fun_name=None,
    fun_args_str=r'["A_0"|"A_1"]',
    params_str=None,
    color="Dandelion"
)

nodeL = Node(
    name="O",
    tile_ch='F',
    parent_names=["A"],
    slice_str="[d],[\ell]",
    fun_name=None,
    fun_args_str=r'W_\rva^{[d],[D]}"A"',
    params_str=None,
    color="SpringGreen"
)


nodes = [nodee,
    nodeQ, nodeK, nodeV,
    node1, node2, node4, node5, node7, node8,
    nodeX, nodeY,
    nodeC,
    nodeL
]

ek= FancyArrow(
    parent_name="e",
    child_name="K",
    script_tuple=("super", "W_\\rvk")
)

eq= FancyArrow(
    parent_name="e",
    child_name="Q",
    script_tuple=("super", "W_\\rvq")
)

ev= FancyArrow(
    parent_name="e",
    child_name="V",
    script_tuple=("super", "W_\\rvv")
)

ao= FancyArrow(
    parent_name="A",
    child_name="O",
    script_tuple=("super", "W_\\rva")
)

fancy_arrows = [ek, eq, ev, ao]

print("\nmosaic:", mosaic)
name = "multi-head-att"
dag = DAG(name, mosaic, nodes, fancy_arrows=fancy_arrows)
header=\
r"""\documentclass[12pt]{article}
\input{bayesuvius.sty}
\begin{document}

"""
fig_header =\
r"""\begin{minipage}{.3\linewidth}
\includegraphics[width=1.7in]{multi-head-att.png}
\end{minipage}%blank lines between minispaces breaks this
\begin{minipage}{.7\linewidth}
"""

fig_footer=\
"""\end{minipage}
"""
dag.write_tex_file(fig_header,
                   fig_footer,
                   fig_caption="Multi-head Attention with 2 heads."
                                " Note that the orange nodes all have"
                                " the same tensor shape.",
                   header=header,
                   column_separation=1.3)