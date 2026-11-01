"""
Bacterial growth — exponential vs. logistic (lag, log, stationary phases).

Chapter 15: Neurophysiology, immunology and infection — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def main() -> None:
    mu, K = 1.0, 1e9          # μ in 1/h, K in CFU/mL
    N0 = 1e4

    def exponencial(t, N): return [mu * N[0]]
    def logistico(t, N): return [mu * N[0] * (1 - N[0] / K)]

    t_eval = np.linspace(0, 20, 400)
    sol_e = solve_ivp(exponencial, [0, 20], [N0], t_eval=t_eval)
    sol_l = solve_ivp(logistico, [0, 20], [N0], t_eval=t_eval)

    fig, ax = plt.subplots()
    ax.semilogy(sol_e.t, sol_e.y[0], label="exponential")
    ax.semilogy(sol_l.t, sol_l.y[0], label="logistic")
    ax.axhline(K, color="gray", linestyle=":", label="K")
    ax.set_xlabel("t (h)")
    ax.set_ylabel("N (CFU/mL)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
