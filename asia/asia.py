from texnn import *

mosaic = [
    "V__S_",
    "T_L_B",
    "_O___",
    "X_D__"
]
nodeV = Node(
    name="VisitedAsia",
    tile_ch='V',
    parent_names=[],
    slice_str=None,
    fun_name="fun",
    fun_args_str="x,y",
    params_str=r"\sigma=5",
    color="red",
    post_eq_comment="(an equation comment)"
)
nodeS = Node(
    name="Smokes",
    tile_ch='S',
    parent_names=[],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None,
    style_name="box",
    full_right_side_of_eq= r"\text{full right side of equation}"
)
nodeT = Node(
    name="Tuberculosis",
    tile_ch='T',
    parent_names=["VisitedAsia"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None,
    style_name="dashed-oval"
)
nodeL = Node(
    name="LungCancer",
    tile_ch='L',
    parent_names=["Smokes"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow",
    style_name="oval"
)
nodeB = Node(
    name="Bronchitis",
    tile_ch='B',
    parent_names=["Smokes"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)
nodeO = Node(
    name="Or",
    tile_ch='O',
    parent_names=["LungCancer", "Tuberculosis"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)
nodeX = Node(
    name="X-Ray",
    tile_ch='X',
    parent_names=["Or"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="blue",
    style_name='rounded-box'
)
nodeD = Node(
    name="Dyspnea",
    tile_ch='D',
    parent_names=["Or", "Bronchitis"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)

nodes = [nodeV, nodeS, nodeT, nodeL,
         nodeB, nodeO, nodeX, nodeD]

print("\nmosaic:", mosaic)
name = "asia"
dag = DAG(nodes, mosaic, name)
dag.write_tex_file(
    underline=False,
    fig_caption="Asia Bnet.",
    conditional_prob=True)
