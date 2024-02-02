from texnn import *

mosaic = [
    "____",
    "____",
    "S_ML",
    "_Ea_",
    "_Gd_",
    "_n__",
    "_A__",
    "VKQ_",
    "____",
    "_B__",
]

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
    parent_names=["E", "G" ],
    slice_str="[86], [768]",
    fun_name=None,
    fun_args_str=r'("E" + "S")\indi(depth\neq 0)',
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
    color="SkyBlue",
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
    parent_names=["d"],
    slice_str="[86], [768]",
    fun_name="gather",
    fun_args_str=None,
    params_str="dim=-2",
    color="pink",
    cc_name="lll_word_hidstate"
)


nodeM= Node(
    name="M",
    tile_ch='M',
    parent_names=["S", "G"],
    slice_str="[86], [300]",
    fun_name=None,
    fun_args_str=r'"G"W_{il}^{[768], [300]}',
    params_str=None,
    color="SpringGreen",
    cc_name="lll_merge_hidstate"
)

noded = Node(
    name="d",
    tile_ch='d',
    parent_names=["n"],
    slice_str="[121], [768]",
    fun_name="dropout",
    fun_args_str=None,
    params_str=None,
    color="pink",
    cc_name="lll_hidstate"
)

nodes = [nodeG, nodeL, noden, nodeS, nodeA, noded,
    nodeV, nodeK, nodeQ, nodeB, nodeE, nodea, nodeM]

BV= FancyArrow(parent_name="B",
               child_name="V",
               inscript="W_\\rvv"
)
BQ= FancyArrow(parent_name="B",
               child_name="Q",
               inscript="W_\\rvq"
)
BK= FancyArrow(parent_name="B",
               child_name="K",
               inscript="W_\\rvk"
)

An= FancyArrow(parent_name="A",
               child_name="n",
               subscript="W_\\rva"
)

ES= FancyArrow(parent_name="E",
               child_name="S",
               inscript="depth\\neq 0",
               color="red"
)

SM= FancyArrow(parent_name="S",
               child_name="M",
               inscript="depth\\neq 0",
               color="red"
)

ML= FancyArrow(parent_name="M",
               child_name="L",
               subscript="W_{il}"
)

fancy_arrows = [BV, BQ, BK, An, SM, ML, ES]

S_ = EndingArrow(
    parent_name="S",
    num_u=2,
    num_r=0
)

S_r = EndingArrow(
    parent_name="S",
    num_u=2,
    num_r=1
)
S_rr = EndingArrow(
    parent_name="S",
    num_u=2,
    num_r=2
)
ending_arrows = [S_, S_r, S_rr]

plateEx = Plate(
    first_and_last_row=(2,8),
    first_and_last_col=(0,2),
    margin= 4.8
)

plateAtt = Plate(
    first_and_last_row=(5,8),
    first_and_last_col=(0,2),
    style_name="dashed",
    margin= 3.8
)

plates= [plateEx, plateAtt]

print("\nmosaic:", mosaic)
name = "sentence-ax-bnet"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          ending_arrows= ending_arrows,
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
    column_separation=3.5
)