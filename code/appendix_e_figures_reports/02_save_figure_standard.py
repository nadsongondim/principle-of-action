"""
Standard for saving figures — consistent name, high dpi, tight bbox.

Appendix E: Good Practices for Figures and Reports — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


IMG = Path("figures")


def main() -> None:
    IMG.mkdir(exist_ok=True)

    n = 4                       # chapter number
    slug = "oscilador-harmonico"

    fig, ax = plt.subplots()
    x = np.linspace(0, 20, 400)
    ax.plot(x, np.cos(x))
    ax.set_xlabel("t")
    ax.set_ylabel("x(t)")

    fig.savefig(IMG / f"fig-{n:02d}-{slug}.png",
                dpi=200, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"Figure saved to {IMG / f'fig-{n:02d}-{slug}.png'}")


if __name__ == "__main__":
    main()
