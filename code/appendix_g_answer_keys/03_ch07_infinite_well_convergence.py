"""
Answer key Ch. 7 — Ex. 6 (Challenge): O(dx²) convergence of the well's eigenvalues.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


def autovalores(N: int, L: float = 1.0, k: int = 3) -> tuple[np.ndarray, float]:
    dx = L/(N+1)
    diag_p = 1.0/dx**2 * np.ones(N)
    diag_l = -0.5/dx**2 * np.ones(N-1)
    H = diags([diag_l, diag_p, diag_l], offsets=[-1, 0, 1])
    E, _ = eigsh(H, k=k, which='SA')
    return np.sort(E), dx


def main() -> None:
    exatos = np.array([n**2 * np.pi**2 / 2 for n in (1, 2, 3)])
    for N in (200, 800):
        E, dx = autovalores(N)
        print(f"N = {N}  dx = {dx:.5f}")
        for n_idx, (e, ex) in enumerate(zip(E, exatos), start=1):
            print(f"  E{n_idx} = {e:.5f}   error = {abs(e - ex):.2e}")


if __name__ == "__main__":
    main()
