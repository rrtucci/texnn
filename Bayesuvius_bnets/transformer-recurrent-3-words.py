from texnn import *

mosaic = [
    "_x__y__z_",
    "_X__Y__Z_",
    "123456789",
    "_A__B__C_"
]

mosaic = DAG.rotate_mosaic(mosaic, "+270_degs")

nodeA = Node(
    name="e_0^t",
    tile_ch='A',
    parent_names=[],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None,
    post_eq_comment="prior"
)
nodeB = Node(
    name="e_1^t",
    tile_ch='B',
    parent_names=[],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None,
    post_eq_comment="prior"
)

nodeC = Node(
    name="e_2^t",
    tile_ch='C',
    parent_names=[],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None,
    post_eq_comment="prior"
)

node1 = Node(
    name="v_0^t",
    tile_ch='1',
    parent_names=["e_0^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_\rvv^t e_0^t',
    params_str=None,
    color=None
)

node2 = Node(
    name="q_0^t",
    tile_ch='2',
    parent_names=["e_0^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvq}^t e_0^t',
    params_str=None,
    color=None
)

node3 = Node(
    name="k_0^t",
    tile_ch='3',
    parent_names=["e_0^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvk 0}^t e_0^t',
    params_str=None,
    color=None
)

node4 = Node(
    name="v_1^t",
    tile_ch='4',
    parent_names=["e_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvv}^t e_1^t',
    params_str=None,
    color=None
)

node5 = Node(
    name="q_1^t",
    tile_ch='5',
    parent_names=["e_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvq}^t e_1^t',
    params_str=None,
    color=None
)

node6 = Node(
    name="k_1^t",
    tile_ch='6',
    parent_names=["e_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvk}^t e_1^t',
    params_str=None,
    color=None
)

node7 = Node(
    name="v_2^t",
    tile_ch='7',
    parent_names=["e_2^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvv}^t e_2^t',
    params_str=None,
    color=None
)

node8 = Node(
    name="q_2^t",
    tile_ch='8',
    parent_names=["e_2^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvq}^t e_2^t',
    params_str=None,
    color=None
)

node9 = Node(
    name="k_2^t",
    tile_ch='9',
    parent_names=["e_2^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=r'W_{\rvk}^t e_2^t',
    params_str=None,
    color=None
)


nodeX = Node(
    name="a_0^t",
    tile_ch='X',
    parent_names=["v_0^t", "q_0^t", "k_0^t",
                  "v_1^t", "k_1^t",
                  "v_2^t", "k_2^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodeY = Node(
    name="a_1^t",
    tile_ch='Y',
    parent_names=["v_0^t", "k_0^t",
                  "v_1^t", "q_1^t", "k_1^t",
                  "v_2^t", "k_2^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodeZ = Node(
    name="a_2^t",
    tile_ch='Z',
    parent_names=["v_0^t", "k_0^t",
                  "v_1^t", "k_1^t",
                  "v_2^t", "q_2^t", "k_2^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodex = Node(
    name="e_0^{t+1}",
    tile_ch='x',
    parent_names=["a_0^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodey = Node(
    name="e_1^{t+1}",
    tile_ch='y',
    parent_names=["a_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodez = Node(
    name="e_2^{t+1}",
    tile_ch='z',
    parent_names=["a_2^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodes = [
    nodeA, nodeB, nodeC,
    node1, node2, node3, node4, node5, node6, node7, node8, node9,
    nodeX, nodeY, nodeZ,
    nodex, nodey, nodez
]

xv0 = FancyArrow(parent_name="e_0^t",
                 child_name="v_0^t",
                 superscript=r"W_{\rvv}^t")
xv1 = FancyArrow(parent_name="e_1^t",
                 child_name="v_1^t",
                 superscript=r"W_{\rvv}^t")
xv2 = FancyArrow(parent_name="e_2^t",
                 child_name="v_2^t",
                 superscript=r"W_{\rvv}^t")
xk0 = FancyArrow(parent_name="e_0^t",
                 child_name="k_0^t",
                 subscript=r"W_{\rvk}^t")
xk1 = FancyArrow(parent_name="e_1^t",
                 child_name="k_1^t",
                 subscript=r"W_{\rvk}^t")
xk2 = FancyArrow(parent_name="e_2^t",
                 child_name="k_2^t",
                 subscript=r"W_{\rvk}^t")

xq0 = FancyArrow(parent_name="e_0^t",
                 child_name="q_0^t",
                 color="red",
                 superscript=r"W_{\rvq}^t")
qc0 = FancyArrow(parent_name="q_0^t",
                 child_name="a_0^t",
                 color="red")

xq1 = FancyArrow(parent_name="e_1^t",
                 child_name="q_1^t",
                 color="red",
                 superscript=r"W_{\rvq}^t")
qc1 = FancyArrow(parent_name="q_1^t",
                 child_name="a_1^t",
                 color="red")
xq2 = FancyArrow(parent_name="e_2^t",
                 child_name="q_2^t",
                 color="red",
                 superscript=r"W_{\rvq}^t")
qc2 = FancyArrow(parent_name="q_2^t",
                 child_name="a_2^t",
                 color="red")

ce0 = FancyArrow(parent_name="a_0^t",
                 child_name="e_0^{t+1}",
                 superscript="1")

ce1 = FancyArrow(parent_name="a_1^t",
                 child_name="e_1^{t+1}",
                 superscript="1")

ce2 = FancyArrow(parent_name="a_2^t",
                 child_name="e_2^{t+1}",
                 superscript="1")


fancy_arrows = [xq0, qc0, xq1, qc1, xq2, qc2,
                xv0, xv1, xv2, xk0, xk1, xk2,
                ce0, ce1, ce2]

plateX = Plate(first_and_last_row= (1,7),
               first_and_last_col=(0,0),
               style_name="dashed")

plate0 = Plate(first_and_last_row= (0,2),
               first_and_last_col=(1,2),
               style_name="dashed",
               margin=1.5)

plate1 = Plate(first_and_last_row= (3,5),
               first_and_last_col=(1,2),
               style_name="dashed",
               margin=1.5)

plate2 = Plate(first_and_last_row= (6,8),
               first_and_last_col=(1,2),
               style_name="dashed",
               margin=1.5)

plates = [plateX, plate0, plate1, plate2]

print("\nmosaic:", mosaic)
name = "transformer-recurrent-3-words"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          plates=plates)
dag.write_tex_file(
    header=BAY_HEADER,
    fig_caption="Recurrent single-head attention for 3 words.",
    column_separation=4
)
