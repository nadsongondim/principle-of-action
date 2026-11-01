"""
Tumor growth with the Gompertz model integrated by solve_ivp.

Chapter 16: Cancer, targeted therapies and radiotherapy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


r, K = 0.01, 1e12         # rate and carrying capacity


def gompertz(t: float, N: np.ndarray) -> list[float]:
    return [r * N[0] * np.log(K / N[0])]


def main() -> None:
    sol = solve_ivp(gompertz, [0, 365], [1e6],
                    t_eval=np.linspace(0, 365, 400))

    fig, ax = plt.subplots()
    ax.semilogy(sol.t, sol.y[0])
    ax.set_xlabel("t (days)")
    ax.set_ylabel("N (cells)")
    ax.set_title("Tumor growth — Gompertz")
    plt.show()


if __name__ == "__main__":
    main()
