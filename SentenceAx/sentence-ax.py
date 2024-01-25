from texnn import *

mosaic = [
    "_j_",
    "EM_",
    "S__",
    "F__",
    "_n_",
    "_A_",
    "VKQ",
    "___",
    "_B_",
    "_e_",
    "_X_"
]

nodeX= Node(
    name="X",
    tile_ch='X',
    parent_names=[],
    slice_str="[6], [84]",
    fun_name=None,
    fun_args_str=None,
    params_str=None,
    color="SpringGreen",
    post_eq_comment= "prior"
)
nodee= Node(
    name="e",
    tile_ch='e',
    parent_names=["X"],
    slice_str="[768], [105]",
    fun_name="Embedding",
    fun_args_str=None,
    params_str=None,
    color="pink"
)
nodeB= Node(
    name="B",
    tile_ch='B',
    parent_names=["e"],
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
nodeF= Node(
    name="F",
    tile_ch='F',
    parent_names=["n"],
    slice_str="[768], [105]",
    fun_name="feed_forward_nn",
    fun_args_str=None,
    params_str=None,
    color="SkyBlue"
)
nodeE= Node(
    name="E",
    tile_ch='E',
    parent_names=["S"],
    slice_str="[768], [105]",
    fun_name="Embedding",
    fun_args_str=None,
    params_str=None,
    color="pink"
)
nodeS= Node(
    name="S",
    tile_ch='S',
    parent_names=["F"],
    slice_str="[6], [84]",
    fun_name="ilabel",
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)

nodeM= Node(
    name="M",
    tile_ch='M',
    parent_names=["E", "n"],
    slice_str="[768], [105]",
    fun_name=None,
    fun_args_str='"E" + "n"',
    params_str=None,
    color="Orchid"
)
nodej= Node(
    name="j",
    tile_ch='j',
    parent_names=["M"],
    slice_str="[6], [84]",
    fun_name="ilabel",
    fun_args_str=None,
    params_str=None,
    color="SpringGreen"
)

nodes = [nodej, nodeM, nodeF, nodeE, noden, nodeA,
    nodeV, nodeK, nodeQ, nodeB, nodeX, nodeS, nodee]

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
    first_and_last_row=(1,6),
    first_and_last_col=(0,2),
    margin= 2.5
)

plateAtt = Plate(
    first_and_last_row=(4,6),
    first_and_last_col=(0,2),
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
    fig_caption="Sentence Ax tranet. $D= d n_\\rvh$ where "
                "$d=768$ is the hidden dimension per head, and "
                "$n_\\rvh=12$ is the number of heads. "
                "2 copies of dashed box connected in "
                "series. 5 copies of plain box connected in series.",
    row_separation= 2,
    column_separation=2
)