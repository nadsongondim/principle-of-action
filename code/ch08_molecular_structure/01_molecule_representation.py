"""
Minimal representation of a molecule — water as an example (atoms, bonds).

Chapter 8: Molecular structure and potential energy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    # water: H — O — H
    posicoes = np.array([
        [-0.7572,  0.5860, 0.0],     # H1
        [ 0.0,     0.0,    0.0],     # O
        [ 0.7572,  0.5860, 0.0],     # H2
    ])
    elementos = ["H", "O", "H"]
    ligacoes = [(0, 1), (1, 2)]

    print("Positions:")
    for el, r in zip(elementos, posicoes):
        print(f"  {el}: {r}")
    print(f"Bonds: {ligacoes}")


if __name__ == "__main__":
    main()
