"""
Visual identity of the series — palette and rcParams for all figures.

Appendix E: Good Practices for Figures and Reports — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


# series palette
NAVY = "#1b2a4a"     # text, axes, outlines
ACCENT = "#2f6fdb"   # main highlight
SOFT = "#98a4ba"     # auxiliary elements
FILL = "#dce6f5"     # fills


def aplicar_estilo() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 13,
        "text.color": NAVY,
        "axes.edgecolor": NAVY,
        "axes.labelcolor": NAVY,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "mathtext.fontset": "dejavusans",
        "axes.unicode_minus": False,
    })


def main() -> None:
    aplicar_estilo()
    x = np.linspace(0, 10, 200)
    fig, ax = plt.subplots()
    ax.plot(x, np.exp(-0.3 * x), color=ACCENT, lw=2, label="curve")
    ax.fill_between(x, 0, np.exp(-0.3 * x), color=FILL, alpha=0.5)
    ax.set_xlabel("time")
    ax.set_ylabel("y(t)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
