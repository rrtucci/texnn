from texnn import *

mosaic = [
    "E_M_L",
    "__S__",
    "__n__",
    "__A__",
    "_VKQ_",
    "_____",
    "X_B__"
]

nodeX= Node(
    name="X",
    tile_ch='X',
    parent_names=[],
    slice_str="[768], [105]",
    fun_name=None,
    fun_args_str="0",
    params_str=None,
    color="SkyBlue"
)

nodeB= Node(
    name="B",
    tile_ch='B',
    parent_names=[],
    slice_str="[768], [105]",
    fun_name="BERT",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)
nodeQ= Node(
    name="Q",
    tile_ch='Q',
    parent_names=["B"],
    slice_str="[D], [105]",
    fun_name=None,
    fun_args_str=r'W_\rvq^{[D], [768]}"B"',
    params_str=None,
    color="Dandelion"
)
nodeK= Node(
    name="K",
    tile_ch='K',
    parent_names=["B"],
    slice_str="[D], [105]",
    fun_name=None,
    fun_args_str=r'W_\rvk^{[D], [768]}"B"',
    params_str=None,
    color="Dandelion"
)
nodeV= Node(
    name="V",
    tile_ch='V',
    parent_names=["B"],
    slice_str="[D], [105]",
    fun_name=None,
    fun_args_str=r'W_\rvv^{[D], [768]}"B"',
    params_str=None,
    color="Dandelion"
)
nodeA= Node(
    name="A",
    tile_ch='A',
    parent_names=["Q", "K", "V"],
    slice_str="[D], [105]",
    fun_name="Attention",
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
noden= Node(
    name="n",
    tile_ch='n',
    parent_names=["A"],
    slice_str="[768], [105]",
    fun_name=None,
    fun_args_str=r'W_\rva^{[768], [D]}"A"',
    params_str=None,
    color="Orchid"
)
nodeS= Node(
    name="S",
    tile_ch='S',
    parent_names=["X","n" ],
    slice_str="[768], [105]",
    fun_name=None,
    fun_args_str=r'"X" + "n"',
    params_str=None,
    color="Orchid"
)
nodeL= Node(
    name="L",
    tile_ch='L',
    parent_names=["M"],
    slice_str="[6], [84]",
    fun_name="ilabel",
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)
nodeE= Node(
    name="E",
    tile_ch='E',
    parent_names=["S"],
    slice_str="[768], [105]",
    fun_name=None,
    fun_args_str='"X"',
    params_str=None,
    color="SkyBlue"
)

nodeM= Node(
    name="M",
    tile_ch='M',
    parent_names=["S"],
    slice_str="[768], [105]",
    fun_name="merge",
    fun_args_str=None,
    params_str=None,
    color="Orchid"
)

nodes = [nodeM, nodeL, noden, nodeS, nodeA,
    nodeV, nodeK, nodeQ, nodeB, nodeX, nodeE]

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
               subscript="W_\\rva"
)

XS= FancyArrow(parent_name="X",
               child_name="S",
               superscript="1",
               curvature= -5
)
SE= FancyArrow(parent_name="S",
               child_name="E",
               subscript="1"
)

nS= FancyArrow(parent_name="n",
               child_name="S",
               subscript="1"
)

fancy_arrows = [BV, BQ, BK, An, XS, SE, nS]

plateEx = Plate(
    first_and_last_row=(0,4),
    first_and_last_col=(0,3),
    margin= 4.5
)

plateAtt = Plate(
    first_and_last_row=(2,4),
    first_and_last_col=(1,3),
    style_name="dashed",
    margin= 3.5
)

plates= [plateEx, plateAtt]

print("\nmosaic:", mosaic)
name = "sentence-ax"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          plates=plates)
dag.write_tex_file(
    header=BAY_HEADER,
    fig_caption="Sentence Ax tranet. $D= d n_\\rvh$ where "
                "$d=768$ is the hidden dimension per head, and "
                "$n_\\rvh=12$ is the number of heads. "
                "2 copies of dashed box connected in "
                "series. 5 copies of plain box connected in series.",
    row_separation= 3.5,
    column_separation=2.5
)