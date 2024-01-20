from texnn import *

mosaic = [
    "_X_",
    "KQV",
    "_A_"
]

mosaic = DAG.rotate_mosaic(mosaic, "+270_degs")

nodeA = Node(
    name="(e^t)",
    tile_ch='A',
    parent_names=[],
    slice_str="[d],[\\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None,
    post_eq_comment="prior"
)

nodeV = Node(
    name="(v^t)",
    tile_ch='V',
    parent_names=["(e^t)"],
    slice_str="[D],[\\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvv^{[D], [d]} "(e^t)"',
    params_str=None,
    color=None
)

nodeQ = Node(
    name="(q^t)",
    tile_ch='Q',
    parent_names=["(e^t)"],
    slice_str="[D],[\\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvq^{[D], [d]} "(e^t)"',
    params_str=None,
    color=None
)

nodeK = Node(
    name="(k^t)",
    tile_ch='K',
    parent_names=["(e^t)"],
    slice_str="[D],[\\ell]",
    fun_name=None,
    fun_args_str=r'W_\rvk^{[D], [d]} "(e^t)"',
    params_str=None,
    color=None
)

nodeX = Node(
    name="(e^{t+1})",
    tile_ch='X',
    parent_names=["(v^t)", "(q^t)", "(k^t)"],
    slice_str="[d],[\\ell]",
    fun_name="Multi-Head-Attention",
    fun_args_str=None,
    params_str=None,
    color=None
)

nodes = [nodeA,
         nodeV, nodeQ, nodeK,
         nodeX
         ]

xk = FancyArrow(parent_name="(e^t)",
                child_name="(k^t)",
                superscript=r"W_\rvk^{[D], [d]}")
xv = FancyArrow(parent_name="(e^t)",
                child_name="(v^t)",
                subscript=r"W_\rvv^{[D], [d]}")


xq = FancyArrow(parent_name="(e^t)",
                  child_name="(q^t)",
                  color="red",
                superscript=r"W_\rvq^{[D], [d]}")
qx = FancyArrow(parent_name="(q^t)",
                  child_name="(e^{t+1})",
                  color="red")
fancy_arrows = [xq, qx, xv, xk]

print("\nmosaic:", mosaic)
name = "transformer-recurrent-3-words-folded-multi-head"
dag = DAG(name, mosaic, nodes, fancy_arrows=fancy_arrows)
dag.write_tex_file(
    header=BAY_HEADER,
    fig_caption="Recurrent single-head attention "
                "for $\\ell=3$ words. Folded. Note that the"
                "  input $e^t$ and the output $e^{t+1}$ have the "
                "same shape $([d], [\\ell])$.",
    row_separation= 4,
    column_separation=4
)
