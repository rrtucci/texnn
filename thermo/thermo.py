from texnn import *

mosaic = [
    "_VN_",
    "U_S_",
    "____",
    "_Tpm",
    "FGHX"
]


Vnode = Node(
    name="V",
    tile_ch='V',
    parent_names=[],
    fun_name=None,
    fun_args_str=r"{\rm prior}",
    post_eq_comment="(volume)",
    color="SpringGreen"
)

Nnode = Node(
    name="\{N_i\}",
    tile_ch='N',
    parent_names=[],
    fun_name=None,
    fun_args_str=r"{\rm prior}",
    post_eq_comment="(number of particles of species $i$)",
    color="SpringGreen"
)

Snode = Node(
    name="S",
    tile_ch='S',
    parent_names=[],
    fun_name=None,
    fun_args_str=r"{\rm prior}",
    post_eq_comment="(entropy)",
    color="Lavender"
)

Unode = Node(
    name="U",
    tile_ch='U',
    parent_names=["S", "V", "\{N_i\}"],
    fun_name = None,
    fun_args_str = 'U(S, V, \{N_i\})',
    post_eq_comment= "(internal energy)",
    color="SpringGreen"
)

pnode = Node(
    name="p",
    tile_ch='p',
    parent_names=[],
    fun_name=None,
    fun_args_str=r"-\;\pder{U}{V}",
    post_eq_comment="(pressure)",
    color="Lavender"
)

mnode = Node(
    name=r"\{\mu_i\}",
    tile_ch='m',
    parent_names=[],
    fun_name=None,
    fun_args_str=r"\pder{U}{\{N_i\}}",
    post_eq_comment= "(chemical potential for species $i$)",
    color="Lavender"
)

Tnode = Node(
    name="T",
    tile_ch='T',
    parent_names=[],
    fun_name=None,
    fun_args_str=r"\pder{U}{S}",
    post_eq_comment="(temperature)",
    color="Lavender"
)

Fnode = Node(
    name="F",
    tile_ch='F',
    parent_names=["U", "T", "S"],
    fun_name=None,
    fun_args_str=r"U-TS",
    post_eq_comment="(Helmholtz free energy)",
    color="SkyBlue"
)

Gnode = Node(
    name="G",
    tile_ch='G',
    parent_names=["U", "p", "V", "T", "S"],
    fun_name=None,
    fun_args_str=r"U+pV-TS",
    post_eq_comment="(Gibbs free energy)",
    color="SkyBlue"
)

Hnode = Node(
    name="H",
    tile_ch='H',
    parent_names=["U", "p", "V"],
    fun_name=None,
    fun_args_str=r"U+pV",
    post_eq_comment= "(enthalpy)",
    color="SkyBlue"
)

Xnode = Node(
    name="\Phi",
    tile_ch='X',
    parent_names=["U", "T", "S", "\{\mu_i\}", "\{N_i\}"],
    fun_name=None,
    fun_args_str=r"U-TS-\sum_i\mu_iN_i",
    post_eq_comment="(Grand Potential)",
    color="SkyBlue"
)

VG = FancyArrow(
    parent_name="V",
    child_name="G",
    curvature=1
)

SX = FancyArrow(
    parent_name="S",
    child_name=r"\Phi",
    curvature=1
)
SG = FancyArrow(
    parent_name="S",
    child_name="G",
    curvature=1
)
SF = FancyArrow(
    parent_name="S",
    child_name="F",
    curvature=1
)

UX = FancyArrow(
    parent_name="U",
    child_name=r"\Phi",
    curvature=1
)


fancy_arrows= [VG, UX, SF]

nodes = [Vnode, Nnode, Snode,
        Unode, pnode, mnode, Tnode,
         Fnode, Gnode, Hnode, Xnode]

print("\nmosaic:", mosaic)
name = "thermo"
dag = DAG(name, mosaic, nodes, fancy_arrows=fancy_arrows)
dag.write_tex_file(
    header=BAY_HEADER,
    underline=True,
    fig_caption="Thermodynamics, a causal perspective. Extrinsic variables"
                " in green, Intrinsic ones in pink, "
                "and Legendre  transforms of $U$ in blue.",
    conditional_prob=False
)
