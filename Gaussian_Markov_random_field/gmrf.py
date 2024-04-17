from texnn import *

mosaic = [
    "__T__",
    "A_B_C",
    "D_E_F",
    "GH__I",
    "__JK_",
    "__L__"
]

nodeTheta = Node(
    name="\\theta",
    tile_ch='T',
    parent_names=[],
    style_name="dashed-oval",
)

nodeC1 = Node(
    name="C_1",
    tile_ch='A',
    parent_names=[],
    style_name="oval",
    color="SkyBlue"

)
nodeC2 = Node(
    name="C_2",
    tile_ch='B',
    parent_names=[],
    style_name="oval",
    color="SkyBlue"

)
nodeC3 = Node(
    name="C_3",
    tile_ch='C',
    parent_names=[],
    style_name="oval",
    color="SkyBlue"

)
nodeC4 = Node(
    name="C_4",
    tile_ch='K',
    parent_names=[],
    style_name="oval",
    color="SkyBlue"

)

nodeX1 = Node(
    name="X_1",
    tile_ch='D',
    parent_names=["C_1", "\\theta"],
    style_name="oval"
)

nodeX2 = Node(
    name="X_2",
    tile_ch='E',
    parent_names=["C_2", "X_1", "\\theta"],
    style_name="oval"
)

nodeX3 = Node(
    name="X_3",
    tile_ch='F',
    parent_names=["C_3", "X_2", "\\theta"],
    style_name="oval"
)

nodeX4 = Node(
    name="X_4",
    tile_ch='J',
    parent_names=["C_4", "X_2", "X_3", "\\theta"],
    style_name="oval"
)

nodeY1 = Node(
    name="Y_1",
    tile_ch='G',
    parent_names=["X_1"],
    style_name="oval",
    color="SkyBlue"
)

nodeY2 = Node(
    name="Y_2",
    tile_ch='H',
    parent_names=["X_2"],
    style_name="oval",
    color="SkyBlue"
)

nodeY3 = Node(
    name="Y_3",
    tile_ch='I',
    parent_names=["X_3"],
    style_name="oval",
    color="SkyBlue"
)

nodeY4 = Node(
    name="Y_4",
    tile_ch='L',
    parent_names=["X_4"],
    style_name="oval",
    color="SkyBlue"
)

nodes = [nodeC1, nodeC2, nodeC3, nodeC4,
         nodeX1, nodeX2, nodeX3, nodeX4,
         nodeY1, nodeY2, nodeY3, nodeY4,
         nodeTheta]

X1X2 = FancyArrow(
    parent_name="X_1",
    child_name="X_2",
    color="black",
    style_name="undirected",
    script_tuple=("super", r"\tau")
)

X2X4 = FancyArrow(
    parent_name="X_2",
    child_name="X_4",
    color="black",
    style_name="undirected",
    script_tuple=("sub", r"\tau")
)

X2X3 = FancyArrow(
    parent_name="X_2",
    child_name="X_3",
    color="black",
    style_name="undirected",
    script_tuple=("super", r"\tau")
)

X3X4 = FancyArrow(
    parent_name="X_3",
    child_name="X_4",
    color="black",
    style_name="undirected",
    script_tuple=("super", r"\tau")
)

C1X1 = FancyArrow(
    parent_name="C_1",
    child_name="X_1",
    color="black",
    script_tuple=("super", r"\beta_1")
)

C2X2 = FancyArrow(
    parent_name="C_2",
    child_name="X_2",
    color="black",
    script_tuple=("super", r"\beta_2")
)

C3X3 = FancyArrow(
    parent_name="C_3",
    child_name="X_3",
    color="black",
    script_tuple=("super", r"\beta_3")
)

C4X4 = FancyArrow(
    parent_name="C_4",
    child_name="X_4",
    color="black",
    script_tuple=("super", r"\beta_4")
)

TX1 = FancyArrow(
    parent_name="\\theta",
    child_name="X_1",
    color="black",
    style_name="dashed"
)
TX2 = FancyArrow(
    parent_name="\\theta",
    child_name="X_2",
    color="black",
    style_name="dashed",
    curvature=2
)
TX3 = FancyArrow(
    parent_name="\\theta",
    child_name="X_3",
    color="black",
    style_name="dashed"
)
TX4 = FancyArrow(
    parent_name="\\theta",
    child_name="X_4",
    color="black",
    style_name="dashed",
    curvature=-4
)

fancy_arrows = [X1X2, X2X3, X2X4, X3X4,
                C1X1, C2X2, C3X3, C4X4,
                TX1, TX2, TX3, TX4]

plate = Plate(
    first_and_last_row=(1, 5),
    first_and_last_col=(0, 4),
    num_layers_str="m",
    margin=2.0
)

import pathlib

# dir = str(pathlib.Path(__file__).parent.resolve())
# name = "gmrf2"
name = "gmrf"
# name = dir + "/" + name
# print("writing to ", name)
dag = DAG(name, mosaic, nodes, fancy_arrows=fancy_arrows, plates=[plate])
dag.write_tex_file()