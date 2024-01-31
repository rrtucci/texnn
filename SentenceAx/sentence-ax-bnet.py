from texnn import *

mosaic = [
    "_S_ML",
    "__Ea_",
    "__G__",
    "__n__",
    "__A__",
    "_VKQ_",
    "_____",
    "_XB__"
]

nodeX= Node(
    name="X",
    tile_ch='X',
    parent_names=[],
    slice_str="[86], [768]",
    fun_name=None,
    fun_args_str="0",
    params_str=None,
    color="pink",
    cc_name="lll_word_hidstate"
)

nodeB= Node(
    name="B",
    tile_ch='B',
    parent_names=[],
    slice_str="[121], [768]",
    fun_name="BERT",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    cc_name="lll_hidstate"
)
nodeQ= Node(
    name="Q",
    tile_ch='Q',
    parent_names=["B"],
    slice_str="[121], [D]",
    fun_name=None,
    fun_args_str=r'"B"W_\rvq^{[768], [D]}',
    params_str=None,
    color="Dandelion"
)
nodeK= Node(
    name="K",
    tile_ch='K',
    parent_names=["B"],
    slice_str="[121], [D]",
    fun_name=None,
    fun_args_str=r'"B"W_\rvk^{[768], [D]}',
    params_str=None,
    color="Dandelion"
)
nodeV= Node(
    name="V",
    tile_ch='V',
    parent_names=["B"],
    slice_str="[121], [D]",
    fun_name=None,
    fun_args_str=r'"B"W_\rvv^{[768], [D]}',
    params_str=None,
    color="Dandelion"
)
nodeA= Node(
    name="A",
    tile_ch='A',
    parent_names=["Q", "K", "V"],
    slice_str="[121], [D]",
    fun_name="Attention",
    fun_args_str=None,
    params_str=None,
    color="Dandelion"
)
noden= Node(
    name="n",
    tile_ch='n',
    parent_names=["A"],
    slice_str="[121], [768]",
    fun_name=None,
    fun_args_str=r'"A"W_\rva^{[D], [768]}',
    params_str=None,
    color="Orchid",
    cc_name="lll_hidstate"
)
nodeS= Node(
    name="S",
    tile_ch='S',
    parent_names=["X","E" ],
    slice_str="[86], [768]",
    fun_name=None,
    fun_args_str=r'"X" + "E"',
    params_str=None,
    color="pink",
    cc_name="lll_word_hidstate"
)
nodeL= Node(
    name="L",
    tile_ch='L',
    parent_names=["M"],
    slice_str="[86], [6]",
    fun_name=None,
    fun_args_str=r'"M"W_{il}^{[300],[6]}',
    params_str=None,
    color="SpringGreen",
    cc_name="lll_word_score"
)
nodeE= Node(
    name="E",
    tile_ch='E',
    parent_names=["a"],
    slice_str="[86], [768]",
    fun_name="embedding",
    fun_args_str=None,
    params_str=None,
    color="pink",
    cc_name="lll_pred_code"
)

nodea= Node(
    name="a",
    tile_ch='a',
    parent_names=["G"],
    slice_str="[86]",
    fun_name="argmax",
    fun_args_str=None,
    params_str="dim=-1",
    color="yellow",
    cc_name="ll_greedy_ilabel"
)

nodeG= Node(
    name="G",
    tile_ch='G',
    parent_names=["n"],
    slice_str="[86], [768]",
    fun_name="gather",
    fun_args_str=None,
    params_str=None,
    color="pink",
    cc_name="lll_word_hidstate"
)


nodeM= Node(
    name="M",
    tile_ch='M',
    parent_names=["S"],
    slice_str="[86], [300]",
    fun_name=None,
    fun_args_str=r'"G"W_{me}^{[768], [300]}',
    params_str=None,
    color="SkyBlue",
    cc_name="lll_merge_hidstate"
)

nodes = [nodeG, nodeM, nodeL, noden, nodeS, nodeA,
    nodeV, nodeK, nodeQ, nodeB, nodeX, nodeE, nodea]

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

ES= FancyArrow(parent_name="E",
               child_name="S",
               superscript="1"
)

SM= FancyArrow(parent_name="S",
               child_name="M",
               subscript="W_{me}"
)

ML= FancyArrow(parent_name="M",
               child_name="L",
               subscript="W_{il}"
)

fancy_arrows = [BV, BQ, BK, An, XS, ML, SM, ES]

plateEx = Plate(
    first_and_last_row=(0,5),
    first_and_last_col=(0,3),
    margin= 3.5
)

plateAtt = Plate(
    first_and_last_row=(3,5),
    first_and_last_col=(1,3),
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
    row_separation= 2.5,
    column_separation=2.5
)