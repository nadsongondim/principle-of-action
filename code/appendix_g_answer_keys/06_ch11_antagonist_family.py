"""
Answer key Ch. 11 — Ex. 6 (Challenge): family of dose-response curves with an antagonist.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    A = np.logspace(-1, 2, 200)         # µM
    fig, ax = plt.subplots()
    for I in [0.0, 0.5, 2.0]:
        EC = 1.0 * (1 + I/0.5)
        E = A / (EC + A)
        ax.semilogx(A, E, label=f"[I]={I} µM  EC50_ap={EC} µM")
    ax.set_xlabel("[A] (µM)")
    ax.set_ylabel("E")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
