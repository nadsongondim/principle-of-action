"""
Competitive antagonism — dose-response curve shifted to the right (Example 2).

Chapter 11: Drug-receptor interaction and molecular pharmacology — Volume 4 of
the series "The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    A = np.logspace(-1, 2, 200)            # agonist in µM
    EC50, Ki = 1.0, 0.5

    fig, ax = plt.subplots()
    for I in [0.0, 0.5, 2.0]:
        EC = EC50 * (1 + I/Ki)
        E = A / (EC + A)
        ax.semilogx(A, E, label=f"[I] = {I:.1f} µM, EC50_app = {EC:.1f} µM")

    ax.set_xlabel("[agonist] (µM)")
    ax.set_ylabel("Normalized effect")
    ax.set_title("Competitive antagonism")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
