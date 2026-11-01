"""
Building the tridiagonal matrix of the 1D Hamiltonian with finite differences.

Chapter 7: Computational quantum mechanics — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from typing import Callable

import numpy as np
from scipy.sparse import diags


def H_matriz(x: np.ndarray, V_func: Callable[[np.ndarray], np.ndarray],
             hbar: float = 1.0, m: float = 1.0):
    dx = x[1] - x[0]
    diag_principal = hbar**2 / (m * dx**2) + V_func(x)
    diag_lateral = -hbar**2 / (2 * m * dx**2) * np.ones(len(x) - 1)
    return diags([diag_lateral, diag_principal, diag_lateral],
                 offsets=[-1, 0, 1])


def main() -> None:
    x = np.linspace(-5.0, 5.0, 200)
    V_oscilador = lambda x: 0.5 * x**2
    H = H_matriz(x, V_oscilador)
    print(f"H matrix assembled, shape = {H.shape}, nnz = {H.nnz}")


if __name__ == "__main__":
    main()
