from texnn import *

mosaic = [
    "P___",
    "__G_",
    "__R_",
    "__Y_",
    "__B_",
    "VK_Q",
]

Qnode = Node(
    name="Q",
    tile_ch='Q',
    parent_names=[],
    slice_str=r"[d],[\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="prior"
)
Knode = Node(
    name="K",
    tile_ch='K',
    parent_names=[],
    slice_str=r"[d],[\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="prior"
)
Vnode = Node(
    name="V",
    tile_ch='V',
    parent_names=[],
    slice_str=r"[d],[\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    post_eq_comment="prior"
)
Bnode = Node(
    name="B",
    tile_ch='B',
    parent_names=["Q", "K"],
    slice_str="[\ell], [\ell]",
    fun_name=None,
    fun_args_str=r'("K")^T "Q"',
    params_str=None,
    color="Dandelion"
)
Ynode = Node(
    name="S",
    tile_ch='Y',
    parent_names=["B"],
    slice_str="[\ell],[\ell]",
    fun_name=None,
    fun_args_str=r'\frac{"B"}{\sqrt{d}}',
    params_str=None,
    color="yellow"
)

Rnode = Node(
    name="M",
    tile_ch='R',
    parent_names=["S"],
    slice_str="[\ell], [\ell]",
    fun_name="mask",
    fun_args_str=None,
    params_str=None,
    color="Lavender"
)

Gnode = Node(
    name="P",
    tile_ch='G',
    parent_names=["M"],
    slice_str="[\ell], [\ell]",
    fun_name="softmax",
    fun_args_str=None,
    params_str=None,
    color="SpringGreen",
    post_eq_comment=r"$\left(\text{Note that }\sum_{\alp\in[\ell]} P^{\alp, "
                    r"[\ell]}=1\right)$"
)

Pnode = Node(
    name="A",
    tile_ch='P',
    parent_names=["P", "V"],
    slice_str=r"[d], [\ell]",
    fun_name=None,
    fun_args_str='"V" "P"',
    params_str=None,
    color="Orchid",
    post_eq_comment=r"$\left(\text{Note that }\sum_{\alp\in[\ell]} P^{\alp, "
                    r"[\ell]}=1\right)$"
)

nodes = [
    Qnode,
    Knode,
    Vnode,
    Bnode,
    Ynode,
    Rnode,
    Gnode,
    Pnode
]

print("\nmosaic:", mosaic)
name = "scaled-dot-prod-att"
dag = DAG(name, mosaic, nodes)

fig_header =\
r"""\begin{minipage}{.5\linewidth}
\includegraphics[width=2in]{scaled-dot-prod-att.jpg}
\end{minipage}%blank lines between minispaces breaks this
\begin{minipage}{.5\linewidth}
"""

fig_footer=\
"""\end{minipage}
"""
dag.write_tex_file(fig_header,
                   fig_footer,
                   fig_caption="Scaled Dot Product Attention.",
                   header=BAY_HEADER)
