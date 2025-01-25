HEADER0 = \
r"""\documentclass[12pt]{article}
\usepackage[dvipsnames]{xcolor}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[color,matrix,frame,arrow,curve]{xy}
\begin{document}

%https://tex.stackexchange.com/questions/208905/loops-of-different-sizes

\newcommand{\loopup}[2]{ % \ar@(ul,ur) size is like 3
\ar@`{[]+/ul+#1pc/,[]+/ur+#1pc/}#2[]}
\newcommand{\loopdown}[2]{ % \ar@(ul,ur) size is like 3
\ar@`{[]+/dl+#1pc/,[]+/dr+#1pc/}#2[]}
\newcommand{\loopright}[2]{ % \ar@(ul,ur) size is like 3
\ar@`{[]+/dr+#1pc/,[]+/ur+#1pc/}#2[]}
\newcommand{\loopleft}[2]{ % \ar@(ul,ur) size is like 3
\ar@`{[]+/dl+#1pc/,[]+/ul+#1pc/}#2[]}

% test code
%\xymatrix{
%\rva\loopup{3}{@[green]_r}
%&
%\rvb\loopdown{3}{@[red]_r}
%&
%\rvc\loopright{3}{@[blue]_r}
%\\
%\rvd\loopleft{3}{@[violet]_r}
%}
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