"""
Exponential decay — the smallest reproducible project possible.

Chapter 1: Development environment and project organization — Volume 4 of the
series "The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    k = 0.3                             # decay constant
    t = np.linspace(0, 20, 400)
    y = np.exp(-k * t)                  # the model, executed

    fig, ax = plt.subplots()
    ax.plot(t, y)
    ax.set_xlabel("time")
    ax.set_ylabel("quantity")

    # make sure the figures folder exists before saving
    # (folder and file names kept as in the book's code: figuras/decaimento.png)
    pasta_figuras = Path("figuras")
    pasta_figuras.mkdir(exist_ok=True)
    fig.savefig(pasta_figuras / "decaimento.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
