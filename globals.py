HEADER0 = \
r"""\documentclass[12pt]{article}
\usepackage[dvipsnames]{xcolor}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[color,matrix,frame,arrow,curve]{xy}
\begin{document}


"""

FOOTER0 = \
"""


\end{document}  
"""

BAY_HEADER=\
r"""\documentclass[12pt]{article}
\input{bayesuvius.sty}
\begin{document}

"""

#replace yellow by other color or remove "*:yellow"
NODE_STYLE_NAME_TO_XY_STR = {
    "plain": "",
    "box": "*+[F*:yellow]",
    "double-box": "*+[F=*:yellow]",
    "dotted-box": "*+[F.*:yellow]",
    "dashed-box": "*+[F--*:yellow]",
    "shaded-box": "*+[F-,*:yellow]",
    "rounded-box": "*+[F-:<3pt>]",
    "oval": "*++[o][F*:yellow]",
    "dashed-oval": "*++[o][F--*:yellow]"
}

ARROW_STYLE_TO_XY_STR = {
    "dashed": "@{-->}",
    "dotted": "@{.>}",
    "photon": "@{~>}",
    "undirected": "@{-}",
    "double": "@{=>}",
    "dotted_double": "@{:>}",
    "two_way_dashed": "@{<-->}"
}


PLATE_STYLE_TO_XY_STR = {
    "plain": "-",
    "dashed": "--",
    "dotted": ".",
    "shaded": "-,",
    "double": "=",
    "rounded": "-:<3pt>"
}

ARROW_SCRIPT_TYPE_TO_XY_STR = {
    "super": "^",
    "sub": "_",
    "in": "|-"
}

# u, d must be first if 2 letters
SIMPLE_DIRECTIONS = ["u", "d", "r", "l",
                     "ur", "ul", "dr", "dl"]