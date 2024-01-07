from texnn import *

mosaic = [
    "___P",
    "_G__",
    "_R__",
    "_Y__",
    "_B__",
    "Q_KV",
]

Qnode = Node(
    name="Q",
    tile_ch='Q',
    parent_names=[],
    slice_str=r"[d],[L]",
    fun_name=None,
    fun_args_str=None,
    params_str="prior",
    color="Dandelion"
)
Knode = Node(
    name="K",
    tile_ch='K',
    parent_names=[],
    slice_str=r"[d],[L]",
    fun_name=None,
    fun_args_str=None,
    params_str="prior",
    color="Dandelion"
)
Vnode = Node(
    name="V",
    tile_ch='V',
    parent_names=[],
    slice_str=r"[d],[L]",
    fun_name=None,
    fun_args_str=None,
    params_str="prior",
    color="Dandelion"
)
Bnode = Node(
    name="B",
    tile_ch='B',
    parent_names=["Q", "K"],
    slice_str="[L], [L]",
    fun_name=None,
    fun_args_str=r"(<Q>)^T <K>",
    params_str=None,
    color="Orchid"
)
Ynode = Node(
    name="Y",
    tile_ch='Y',
    parent_names=["B"],
    slice_str="[L],[L]",
    fun_name=None,
    fun_args_str=r"\frac{<B>}{\sqrt{d_\rvk}}",
    params_str=None,
    color="yellow"
)

Rnode = Node(
    name="R",
    tile_ch='R',
    parent_names=["Y"],
    slice_str="[L], [L]",
    fun_name="mask",
    fun_args_str=None,
    params_str=None,
    color="Lavender"
)

Gnode = Node(
    name="G",
    tile_ch='G',
    parent_names=["R"],
    slice_str="[L], [L]",
    fun_name="softmax",
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)

Pnode = Node(
    name="P",
    tile_ch='P',
    parent_names=["G", "V"],
    slice_str=r"[d], [L]",
    fun_name=None,
    fun_args_str="<V><G>",
    params_str=None,
    color="Orchid"
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
name = "scaled-dot-prod-att"
dag = DAG(nodes, mosaic, name)

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
