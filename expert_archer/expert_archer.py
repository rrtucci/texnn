from texnn import *

mosaic = [
    "__",
    "AB",
    "CD"
]
nodeA = Node(
    name="A",
    tile_ch='A',
    parent_names=[]
)
nodeB = Node(
    name="B",
    tile_ch='B',
    parent_names=["A"],
)
nodeC = Node(
    name="C",
    tile_ch='C',
    parent_names=["A"],
)
nodeD = Node(
    name="D",
    tile_ch='D',
    parent_names=["B", "C"],
)

nodes = [nodeA, nodeB, nodeC, nodeD]

AB = FancyArrow(
    parent_name="A",
    child_name="B",
    color="red",
    style_name="dashed",
    curvature=1,
    script_tuple=("super", "F")
)

BD = FancyArrow(
    parent_name="B",
    child_name="D",
    script_tuple=("in", r"(x,y)")
)

CD = FancyArrow(
    parent_name="C",
    child_name="D",
    script_tuple=("sub", r"\mu"),
    style_name="photon"
)

AC = FancyArrow(
    parent_name="A",
    child_name="C",
    style_name="double",
    script_tuple=("sub", "500")
)

fancy_arrows = [AB, BD, CD, AC]

A_ = EndingArrow(
    parent_name="A",
    num_r=1,
    num_u=1
)

ending_arrows = [A_]

DD = RoundTripArrow(
    parent_name="D",
    starting_dir="dl",
    ending_dir="dr",
    color="green",
    script_tuple=("sub", "xx")
)

round_trip_arrows = [DD]

A_C = ConfounderArrow(
    parent_name="A",
    child_name="C",
    color="blue",
    curvature=3
)

confounder_arrows = [A_C]

D_B = FeedbackArrow(
    parent_name="D",
    child_name="B",
    color="green",
    curvature=3
)

feedback_arrows = [D_B]

print("\nmosaic:", mosaic)
name = "expert-archer"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          ending_arrows=ending_arrows,
          round_trip_arrows=round_trip_arrows,
          confounder_arrows=confounder_arrows,
          feedback_arrows=feedback_arrows)
dag.write_tex_file(
    underline=True,
    fig_caption="Expert Archer.",
    conditional_prob=True,
    column_separation=5,
    row_separation=5)
