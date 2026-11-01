"""
1D FDTD for Maxwell — leap-frog update of the E and H fields on the Yee grid.

Chapter 6: Relativity, fields and electromagnetism — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    nx = 400
    dx = 1.0
    eps = 1.0
    mu = 1.0
    c = 1.0 / np.sqrt(eps * mu)
    dt = 0.5 * dx / c            # CFL = 0.5

    E = np.zeros(nx)
    H = np.zeros(nx - 1)

    # initial Gaussian pulse in E
    x = np.arange(nx) * dx
    E[:] = np.exp(-((x - nx*dx/2) / (10*dx))**2)

    # The domain has 400 cells and the pulse starts from the center at speed c
    # (CFL = 0.5, so each edge is ~200 / 0.5 = 400 steps away). We limit
    # n_passos = 300 to stop before the wavefront reaches the edges —
    # otherwise, with no absorbing boundary condition, spurious reflections
    # would appear and pollute the teaching plot.
    n_passos = 300
    snapshots = []
    snap_em = [0, 60, 120, 180]

    for n in range(n_passos):
        H[:] += dt/(mu*dx) * (E[1:] - E[:-1])     # B from the curl of E
        E[1:-1] += dt/(eps*dx) * (H[1:] - H[:-1]) # E from the curl of B
        if n in snap_em:
            snapshots.append((n, E.copy()))

    fig, ax = plt.subplots()
    for n, snap in snapshots:
        ax.plot(x, snap, label=f"n = {n}")
    ax.set_xlabel("x")
    ax.set_ylabel("E")
    ax.legend()
    ax.set_title("1D electromagnetic wave — FDTD")
    plt.show()


if __name__ == "__main__":
    main()
