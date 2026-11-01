"""
Answer key Ch. 9 — Ex. 6 (Challenge): accumulation of B in A→B→C varying k1/k2.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def main() -> None:
    rhos = np.logspace(-1, 1, 21)
    Bmax = []
    for r in rhos:
        k1, k2 = r, 1.0
        sol = solve_ivp(lambda t, y: [-k1*y[0], k1*y[0]-k2*y[1], k2*y[1]],
                        [0, 50], [1, 0, 0], dense_output=True)
        Bmax.append(sol.sol(np.linspace(0, 50, 5001))[1].max())   # dense grid
    Bmax = np.array(Bmax)
    for rho in (0.1, 1.0, 10.0):
        i = int(np.argmin(np.abs(rhos - rho)))
        print(f"ρ = {rhos[i]:5.1f}: B_max = {Bmax[i]:.4f}")
    # ρ = 0.1: 0.0774;  ρ = 1: 0.3679 (= 1/e);  ρ = 10: 0.7742

    fig, ax = plt.subplots()
    ax.semilogx(rhos, Bmax)
    ax.set_xlabel("k1 / k2")
    ax.set_ylabel("B_max")
    ax.set_title("Accumulation of intermediate B in the A→B→C network")
    plt.show()


if __name__ == "__main__":
    main()
