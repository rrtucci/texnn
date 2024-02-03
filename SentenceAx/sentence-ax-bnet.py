from texnn import *

mosaic = [
    "___",
    "___",
    "_ML",
    "SEa",
    "dG_",
    "_I_",
    "_BX"
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

noden= Node(
    name="I",
    tile_ch='I',
    parent_names=["B"],
    slice_str="[121], [768]",
    fun_name=None,
    fun_args_str=r'\left["B"\indi(depth=0) "M"\indi(depth> 0)\right]',
    params_str=None,
    color="Orchid",
    cc_name="lll_hidstate"
)
nodeS= Node(
    name="S",
    tile_ch='S',
    parent_names=["E", "G"],
    slice_str="[86], [768]",
    fun_name=None,
    fun_args_str=r'"E" + "G"',
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
nodeX= Node(
    name="X",
    tile_ch='X',
    parent_names=[],
    slice_str="[86], [6]",
    fun_name=None,
    fun_args_str=r'"L"\indi(depth> 0)',
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
    parent_names=["X"],
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
    fun_args_str=r'\left["G"\indi(depth=0) + "S"\indi(depth> 0) \right] '
                 r'W_{me}^{[768], [300]}',
    params_str=None,
    color="Dandelion",
    cc_name="lll_word_hidstate"
)

noded = Node(
    name="d",
    tile_ch='d',
    parent_names=["I"],
    slice_str="[121], [768]",
    fun_name="dropout",
    fun_args_str=None,
    params_str=None,
    color="Orchid",
    cc_name="lll_hidstate"
)

nodes = [nodeG, nodeL, noden, nodeS, noded,
    nodeB, nodeE, nodea, nodeM, nodeX]

GS= FancyArrow(parent_name="G",
               child_name="S",
               superscript="1"
)

ES= FancyArrow(parent_name="E",
               child_name="S",
               superscript="1"
)

SM= FancyArrow(parent_name="S",
               child_name="M",
               superscript="W_{me}",
)

GM= FancyArrow(parent_name="G",
               child_name="M",
               inscript="W_{me}",
               color="red",
               curvature= 5
)

ML= FancyArrow(parent_name="M",
               child_name="L",
               superscript="W_{il}"
)


fancy_arrows = [SM, ML, ES, GS, GM]

M_ = EndingArrow(
    parent_name="M",
    num_u=2,
    num_r=0
)

L_ = EndingArrow(
    parent_name="L",
    num_u=2,
    num_r=0
)


ending_arrows = [M_, L_]

plateOnce = Plate(
    first_and_last_row=(3,3),
    first_and_last_col=(0,2),
    style_name= "dotted"
)

plateEx = Plate(
    first_and_last_row=(2,5),
    first_and_last_col=(0,2),
    margin= 4.8
)

plateAtt = Plate(
    first_and_last_row=(5,5),
    first_and_last_col=(1,1),
    style_name="dashed",
    margin= 3.8
)

plates= [plateEx, plateAtt, plateOnce]

print("\nmosaic:", mosaic)
name = "sentence-ax-bnet"
dag = DAG(name, mosaic, nodes,
          fancy_arrows=fancy_arrows,
          ending_arrows= ending_arrows,
          plates=plates)
dag.write_tex_file(
    header=BAY_HEADER,
    fig_caption="Sax bnet. 2 copies of dashed box are connected in "
                "series. 5 copies (5 depths) of plain box are connected in "
                "series. "
                " However, in the first of those 5 plain box copies, "
                "the dotted box "
                " is omitted and node $\\ul{G}$ feeds directly into node "
                " $\\ul{M}$ (indicated by red arrow). "
                "We display the tensor "
                "shape superscripts in the PyTorch L2R order. All "
                "tensor shape superscripts have been simplified by "
                "omitting a $[s_{ba}]$ from their left side, where $s_{"
                "ba}=24$ is the batch size. "
                ,
    row_separation= 2.5,
    column_separation=3.5
)