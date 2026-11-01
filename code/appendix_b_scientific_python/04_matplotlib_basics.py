"""
Quick guide — Matplotlib: basic figure and multiple panels.

Appendix B: Quick Guide to Scientific Python — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def figura_basica() -> None:
    x = np.linspace(0, 10, 200)
    y = np.exp(-0.3 * x)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x, y, color='steelblue', lw=2, label='data')
    ax.set_xlabel('time')
    ax.set_ylabel('concentration')
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig('curva.png', dpi=200, bbox_inches='tight')
    plt.close(fig)


def multiplos_paineis() -> None:
    x = np.linspace(0, 10, 200)
    y1 = np.exp(-0.3 * x)
    y2 = np.sin(x)

    fig, (axA, axB) = plt.subplots(1, 2, figsize=(10, 4))
    axA.plot(x, y1)
    axB.plot(x, y2)
    plt.show()


def main() -> None:
    figura_basica()
    multiplos_paineis()


if __name__ == "__main__":
    main()
