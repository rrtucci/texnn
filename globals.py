HEADER = \
r"""\documentclass[12pt]{article}
\usepackage[dvipsnames]{xcolor}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[color,matrix,frame,arrow,curve]{xy}
\begin{document}


"""

FOOTER = \
"""


\end{document}  
"""

BAY_HEADER=\
r"""\documentclass[12pt]{article}
\input{bayesuvius.sty}
\begin{document}

"""

#replace yellow by other color or remove "*:yellow"
NODE_STYLE_NAME_TO_XY_STR={
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

ARROW_STYLE_TO_XY_STR={
    "dashed": "@{-->}",
    "dotted": "@{.>}",
    "photon": "@{~>}",
    "undirected": "@{-}",
    "double": "@{=>}",
    "dotted_double": "@{:>}"
}

PLATE_STYLE_TO_XY_STR={
    "plain": "-",
    "dashed": "--",
    "dotted": ".",
    "shaded": "-,",
    "double": "=",
    "rounded": "-:<3pt>"
}



