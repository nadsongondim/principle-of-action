"""
1D infinite well — diagonalization and comparison with the exact eigenvalues.

For hbar = m = 1 and L = 1, we expect E_n = n² π² / 2.

Chapter 7: Computational quantum mechanics — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


def main() -> None:
    N = 200
    L = 1.0
    dx = L / (N + 1)
    x = np.linspace(dx, L - dx, N)

    diag_p = 1.0 / dx**2 * np.ones(N)
    diag_l = -0.5 / dx**2 * np.ones(N - 1)
    H = diags([diag_l, diag_p, diag_l], offsets=[-1, 0, 1])

    E, _ = eigsh(H, k=3, which='SA')
    E = np.sort(E)

    print("Numerical eigenvalues:", E)
    print("Exact (n² π² / 2):", [n**2 * np.pi**2 / 2 for n in (1, 2, 3)])


if __name__ == "__main__":
    main()
