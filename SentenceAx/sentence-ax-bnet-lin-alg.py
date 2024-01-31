from texnn import *

"""

This draws the same bnet as sentence-ax-bnet.py, except that the tensor 
shape superscripts are ordered in  the R2L convention, as in Linear Algebra.

"""

mosaic = [
    "_E___",
    "L_MS_",
    "___n_",
    "___A_",
    "__VKQ",
    "_____",
    "_X_B_"
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
    color="pink"
)
nodeS= Node(
    name="S",
    tile_ch='S',
    parent_names=["X","n" ],
    slice_str="[768], [105]",
    fun_name=None,
    fun_args_str=r'"X" + "n"',
    params_str=None,
    color="pink"
)
nodeL= Node(
    name="L",
    tile_ch='L',
    parent_names=["M"],
    slice_str="[6], [105]",
    fun_name=None,
    fun_args_str=r'W_{il}^{[6],[300]}"M"',
    params_str=None,
    color="SpringGreen"
)
nodeE= Node(
    name="E",
    tile_ch='E',
    parent_names=["L"],
    slice_str="[768], [105]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)

nodeM= Node(
    name="M",
    tile_ch='M',
    parent_names=["S"],
    slice_str="[300], [105]",
    fun_name=None,
    fun_args_str=r'W_{me}^{[300], [768]}"S"',
    params_str=None,
    color="pink"
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

nS= FancyArrow(parent_name="n",
               child_name="S",
               subscript="1"
)

SM= FancyArrow(parent_name="S",
               child_name="M",
               superscript="W_{me}"
)
ML= FancyArrow(parent_name="M",
               child_name="L",
               superscript="W_{il}"
)

fancy_arrows = [BV, BQ, BK, An, XS, nS, SM, ML]

plateEx = Plate(
    first_and_last_row=(0,4),
    first_and_last_col=(1,4),
    margin= 3.5
)

plateAtt = Plate(
    first_and_last_row=(2,4),
    first_and_last_col=(2,4),
    style_name="dashed",
    margin= 2.5
)

plates= [plateEx, plateAtt]

print("\nmosaic:", mosaic)
name = "sentence-ax-bnet"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          plates=plates)
dag.write_tex_file(
    header=BAY_HEADER,
    fig_caption="SentenceAx Bayesian network. "
                "2 copies of dashed box are connected in "
                "series. 5 copies of plain box are connected in series. "
                "We display the tensor "
                "shape superscripts in the Linear Algebra R2L order. "
                "(PyTorch uses a L2R order instead). All "
                "tensor shape superscripts have been simplified by "
                "omitting a $[s_{ba}]$, where $s_{ba}=24$ is the batch size. " 
                "$D= d n_\\rvh$ where "
                "$d=768$ is the hidden dimension per head, and "
                "$n_\\rvh=12$ is the number of heads. "
                ,
    row_separation= 3.5,
    column_separation=2.5
)