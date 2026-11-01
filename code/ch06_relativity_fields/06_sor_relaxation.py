"""
2D Laplace equation solved by SOR (Successive Over-Relaxation).

Compares the number of iterations to convergence between Jacobi (ω = 1) and SOR
with ω ≈ 1.9 — for an 80×80 grid the speed-up is more than an order of
magnitude, illustrating why naive iterative solvers rarely survive
in realistic domains.

Chapter 6: Relativity, fields and electromagnetism — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def aplicar_condicoes_contorno(phi: np.ndarray) -> None:
    phi[0, :] = 1.0
    phi[-1, :] = 0.0
    phi[:, 0] = 0.0
    phi[:, -1] = 0.0


def resolver(omega: float, nx: int = 80, ny: int = 80,
             tol: float = 1e-5, max_iter: int = 20_000) -> tuple[np.ndarray, int]:
    """Gauss-Seidel iteration with row-wise relaxation (SOR). ω=1 reproduces Gauss-Seidel."""
    phi = np.zeros((nx, ny))
    aplicar_condicoes_contorno(phi)

    for k in range(1, max_iter + 1):
        delta_max = 0.0
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                phi_novo = 0.25 * (
                    phi[i + 1, j] + phi[i - 1, j] +
                    phi[i, j + 1] + phi[i, j - 1]
                )
                delta = phi_novo - phi[i, j]
                phi[i, j] += omega * delta
                if abs(delta) > delta_max:
                    delta_max = abs(delta)
        if delta_max < tol:
            return phi, k
    return phi, max_iter


def main() -> None:
    phi_gs, k_gs = resolver(omega=1.0)
    phi_sor, k_sor = resolver(omega=1.9)

    print(f"Gauss-Seidel (ω=1.0): {k_gs} iterations")
    print(f"SOR          (ω=1.9): {k_sor} iterations")
    print(f"speed-up: ~{k_gs / max(k_sor, 1):.1f}×")

    fig, ax = plt.subplots()
    im = ax.imshow(phi_sor, origin="lower", cmap="viridis")
    fig.colorbar(im, ax=ax, label="phi")
    ax.set_title(f"SOR (ω=1.9) — converged in {k_sor} iterations")
    plt.show()


if __name__ == "__main__":
    main()
