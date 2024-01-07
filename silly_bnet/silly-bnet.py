from texnn import *

mosaic = [
    "_B_D",
    "A_C_",
]
anode = Node(
    name="A",
    tile_ch="A",
    parent_names=[],
    slice_str="[3], [4]",
    fun_name="fun_a",
    fun_args_str=None,
    params_str="axis=1",
    color="yellow"
)
bnode = Node(
    name="B",
    tile_ch="B",
    parent_names=["A"],
    slice_str="[3]",
    fun_name="fun_b",
    fun_args_str=None,
    params_str=None,
    color="Lavender"
)
cnode = Node(
    name="C",
    tile_ch="C",
    parent_names=["A", "B"],
    slice_str="[4]",
    fun_name=None,
    fun_args_str='"B""A"+b^4',
    params_str=None,
    color="cyan"
)
dnode = Node(
    name="D",
    tile_ch="D",
    parent_names=["A", "B"],
    slice_str="[4]",
    fun_name="cos",
    fun_args_str=None,
    params_str="axis=1",
    color="yellow"
)
nodes = [anode, bnode, cnode, dnode]
print("\nmosaic:", mosaic)
rotated_mosaic = DAG.rotate_mosaic(mosaic, "+90_degs")
print("rotated mosaic:", rotated_mosaic)

str0 = ""
str0 += HEADER
dag = DAG(nodes, mosaic, "silly-bnet")
str0 += dag.get_figure_str(fig_caption="Silly bnet")
str0 += dag.get_equations_str()
dag = DAG(nodes, rotated_mosaic, "rotated-silly-bnet")
str0 += dag.get_figure_str(fig_caption="rotated silly bnet")
str0 += FOOTER
with open("silly-bnet.tex", "w") as f:
    f.write(str0)