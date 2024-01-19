from texnn import *

mosaic = [
    "_X__Y_",
    "142536",
    "_A__B_"
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

node1 = Node(
    name="v_0^t",
    tile_ch='1',
    parent_names=["e_0^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

node2 = Node(
    name="q_0^t",
    tile_ch='2',
    parent_names=["e_0^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

node3 = Node(
    name="k_0^t",
    tile_ch='3',
    parent_names=["e_0^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

node4 = Node(
    name="v_1^t",
    tile_ch='4',
    parent_names=["e_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

node5 = Node(
    name="q_1^t",
    tile_ch='5',
    parent_names=["e_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

node6 = Node(
    name="k_1^t",
    tile_ch='6',
    parent_names=["e_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodeX = Node(
    name="e_0^{t+1}",
    tile_ch='X',
    parent_names=["v_0^t", "q_0^t", "k_0^t",
                  "v_1^t", "q_1^t", "k_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodeY = Node(
    name="e_1^{t+1}",
    tile_ch='Y',
    parent_names=["v_0^t", "q_0^t", "k_0^t",
                  "v_1^t", "q_1^t", "k_1^t"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodes = [nodeA, nodeB,
         node1, node2, node3, node4, node5, node6,
         nodeX, nodeY
         ]

x0q0 = FancyArrow(parent_name="e_0^t",
                  child_name="q_0^t",
                  color="red")
q0x0 = FancyArrow(parent_name="q_0^t",
                  child_name="e_0^{t+1}",
                  color="red")

x1q1 = FancyArrow(parent_name="e_1^t",
                  child_name="q_1^t",
                  color="red")
q1x1 = FancyArrow(parent_name="q_1^t",
                  child_name="e_1^{t+1}",
                  color="red")
fancy_arrows = [x0q0, q0x0, x1q1, q1x1]

print("\nmosaic:", mosaic)
name = "transformer-recurrent-2-heads-attention-1st"
dag = DAG(name, mosaic, nodes, fancy_arrows=fancy_arrows)
dag.write_tex_file(
    header=BAY_HEADER,
    fig_caption="Recurrent multi-head attention with 2 heads, attention-first"
)
