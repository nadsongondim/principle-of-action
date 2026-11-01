"""
2D Laplace equation solved by iterative relaxation (vectorized Jacobi).

Chapter 6: Relativity, fields and electromagnetism — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    nx, ny = 80, 80
    phi = np.zeros((nx, ny))

    # boundary conditions (Dirichlet): edges with fixed values
    phi[0, :] = 1.0          # top edge at 1
    phi[-1, :] = 0.0         # bottom edge at 0
    phi[:, 0] = 0.0
    phi[:, -1] = 0.0

    N_iter = 2_000
    for _ in range(N_iter):
        phi[1:-1, 1:-1] = 0.25 * (
            phi[2:, 1:-1] + phi[:-2, 1:-1] +
            phi[1:-1, 2:] + phi[1:-1, :-2]
        )
        # reapply the fixed boundary conditions
        phi[0, :] = 1.0
        phi[-1, :] = 0.0
        phi[:, 0] = 0.0
        phi[:, -1] = 0.0

    fig, ax = plt.subplots()
    im = ax.imshow(phi, origin="lower", cmap="viridis")
    fig.colorbar(im, ax=ax, label="phi")
    ax.set_title("Steady-state 2D Laplace potential")
    plt.show()


if __name__ == "__main__":
    main()
