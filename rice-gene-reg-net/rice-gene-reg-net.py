from texnn import *

mosaic = [
    "P_a_A__",
    "_CbRL_G",
    "H_S_cdD",
    "___e___"
]

Pnode = Node(
    name="PAT1",
    tile_ch='P',
    parent_names=[],
    fun_name=None,
    color="Dandelion"
)

anode = Node(
    name="P1F3",
    tile_ch='a',
    parent_names=[],
    fun_name=None,
    color="Dandelion"
)

Anode = Node(
    name="APRR",
    tile_ch='A',
    parent_names=[],
    fun_name=None,
    color="Dandelion"
)

Lnode = Node(
    name="LHY",
    tile_ch='L',
    parent_names=["P1F3", "APRR", "GI"],
    fun_name=None,
    color="Dandelion"
)

Gnode = Node(
    name="GI",
    tile_ch='G',
    parent_names=["LHY"],
    fun_name=None,
    color="Orchid"
)

Cnode = Node(
    name="CHS",
    tile_ch='C',
    parent_names=["PAT1", "P1F3",
                    "HOG1", "STO"],
    fun_name=None,
    color="Orchid"
)

bnode = Node(
    name="CAB1",
    tile_ch='b',
    parent_names=["P1F3"],
    fun_name=None,
    color="Orchid"
)

Rnode = Node(
    name="RBCB1A",
    tile_ch='R',
    parent_names=["P1F3"],
    fun_name=None,
    color="Orchid"
)

cnode = Node(
    name="GBSS1",
    tile_ch='c',
    parent_names=["LHY"],
    fun_name=None,
    color="Orchid"
)

Hnode = Node(
    name="HOG1",
    tile_ch='H',
    parent_names=[],
    fun_name=None,
    color="Orchid"
)

Snode = Node(
    name="STO",
    tile_ch='S',
    parent_names=[],
    fun_name=None,
    color="Orchid"
)

dnode = Node(
    name="CAT3",
    tile_ch='d',
    parent_names=["LHY"],
    fun_name=None,
    color="Orchid"
)

Dnode = Node(
    name="DND1",
    tile_ch='D',
    parent_names=[],
    fun_name=None,
    color="Orchid"
)


enode = Node(
    name="RCD1",
    tile_ch='e',
    parent_names=["STO", "CAT3", "DND1"],
    fun_name=None,
    color="Orchid"
)

LG = FancyArrow(
    parent_name="LHY",
    child_name="GI",
    curvature=1
)

GL = FancyArrow(
    parent_name="GI",
    child_name="LHY",
    curvature=1
)

nodes = [
    Pnode, anode, Anode,
    Lnode, Gnode,
    Cnode, bnode, Rnode, cnode,
    Hnode, Snode, dnode, Dnode,
    enode]

fancy_arrows =[GL, LG]

print("\nmosaic:", mosaic)
name = "rice-gene-reg-net"
dag = DAG(name, mosaic, nodes, fancy_arrows=fancy_arrows)
dag.write_tex_file(
    header=BAY_HEADER,
    underline=True,
    fig_caption="Hybrid rice gene reg net",
    conditional_prob=False
)