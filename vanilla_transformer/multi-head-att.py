from texnn import *

mosaic = [
    "____F____",
    "____C____",
    "_X__Y__Z_",
    "123456789",
    "_Q__K__V_"
]
mosaic = DAG.rotate_mosaic(mosaic, "+270_degs")

nodeQ = Node(
    name="Q",
    tile_ch='Q',
    parent_names=[],
    slice_str=r"[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion",
    post_eq_comment="prior"
)

nodeK = Node(
    name="K",
    tile_ch='K',
    parent_names=[],
    slice_str=r"[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion",
    post_eq_comment="prior"
)

nodeV = Node(
    name="V",
    tile_ch='V',
    parent_names=[],
    slice_str=r"[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion",
    post_eq_comment="prior"
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

node3 = Node(
    name="Q_2",
    tile_ch='3',
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

node6 = Node(
    name="K_2",
    tile_ch='6',
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

node9 = Node(
    name="V_2",
    tile_ch='9',
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
    parent_names=["Q_0", "K_0", "V_0"],
    slice_str="[d],[\ell]",
    fun_name="scaled_dot_prod_att",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)


nodeY = Node(
    name="A_1",
    tile_ch='Y',
    parent_names=["Q_1", "K_1", "V_1"],
    slice_str="[d],[\ell]",
    fun_name="scaled_dot_prod_att",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)

nodeZ = Node(
    name="A_2",
    tile_ch='Z',
    parent_names=["Q_2", "K_2","V_2"],
    slice_str="[d],[\ell]",
    fun_name="scaled_dot_prod_att",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)

nodeC = Node(
    name="A",
    tile_ch='C',
    parent_names=["A_0", "A_1", "A_2"],
    slice_str="[D],[\ell]",
    fun_name=None,
    fun_args_str=r'["A_0"|"A_1"|"A_2"]',
    params_str=None,
    color="yellow"
)

nodeL = Node(
    name="O",
    tile_ch='F',
    parent_names=["A"],
    slice_str="[D],[\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvo^{[D],[D]}"A"',
    params_str=None,
    color="Dandelion"
)


nodes = [
    nodeQ, nodeK, nodeV,
    node1, node2, node3, node4, node5, node6, node7, node8, node9,
    nodeX, nodeY, nodeZ,
    nodeC,
    nodeL
]
name = "multi-head-att"
dag = DAG(nodes, mosaic, name)
header=\
r"""\documentclass[12pt]{article}
\input{bayesuvius.sty}
\begin{document}

"""
fig_header =\
r"""\begin{minipage}{.5\linewidth}
\includegraphics[width=2in]{multi-head-att.png}
\end{minipage}%blank lines between minispaces breaks this
\begin{minipage}{.5\linewidth}
"""

fig_footer=\
"""\end{minipage}
"""
dag.write_tex_file(fig_header,
                   fig_footer,
                   fig_caption="Multi-head Attention.",
                   header=header)
