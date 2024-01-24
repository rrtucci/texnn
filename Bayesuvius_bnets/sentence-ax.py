from texnn import *

mosaic = [
    "__j_",
    "_E__",
    "SF__",
    "__n_",
    "__A_",
    "_VKQ",
    "____",
    "__B_",
    "__X_"
]

nodeX= Node(
    name="X",
    tile_ch='X',
    parent_names=[],
    slice_str="[L]], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)
nodeB= Node(
    name="B",
    tile_ch='B',
    parent_names=["X"],
    slice_str="[d], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)
nodeQ= Node(
    name="Q",
    tile_ch='Q',
    parent_names=["B"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeK= Node(
    name="K",
    tile_ch='K',
    parent_names=["B"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeV= Node(
    name="V",
    tile_ch='V',
    parent_names=["B"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
nodeA= Node(
    name="A",
    tile_ch='A',
    parent_names=["Q", "K", "V"],
    slice_str="[D], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
noden= Node(
    name="n",
    tile_ch='n',
    parent_names=["A"],
    slice_str="[d], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="yellow"
)
nodeF= Node(
    name="F",
    tile_ch='F',
    parent_names=["n"],
    slice_str="[d], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)
nodeS= Node(
    name="S",
    tile_ch='S',
    parent_names=["F"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)
nodeE= Node(
    name="E",
    tile_ch='E',
    parent_names=["F"],
    slice_str=None,
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color=None
)
nodej= Node(
    name="j",
    tile_ch='j',
    parent_names=["E", "n"],
    slice_str="[d], [\ell]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)

nodes = [nodej, nodeE, nodeF, noden, nodeA,
    nodeV, nodeK, nodeQ, nodeB, nodeX, nodeS]

BV= FancyArrow(parent_name="B",
               child_name="V",
               superscript="W_\\rvv"
)
BQ= FancyArrow(parent_name="B",
               child_name="Q",
               subscript="W_\\rvq"
)
BK= FancyArrow(parent_name="B",
               child_name="K",
               superscript="W_\\rvk"
)

An= FancyArrow(parent_name="A",
               child_name="n",
               superscript="W_\\rva"
)

fancy_arrows = [BV, BQ, BK, An]

plateEx = Plate(
    first_and_last_row=(0,5),
    first_and_last_col=(1,3),
    margin= 2.5
)

plateAtt = Plate(
    first_and_last_row=(3,5),
    first_and_last_col=(1,3),
    style_name="dashed",
    margin= 1.5
)

plates= [plateEx, plateAtt]

print("\nmosaic:", mosaic)
name = "sentence-ax"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          plates=plates)
dag.write_tex_file(
    header=BAY_HEADER,
    fig_caption="Sentence Ax tranet.",
    row_separation= 2,
    column_separation=2
)