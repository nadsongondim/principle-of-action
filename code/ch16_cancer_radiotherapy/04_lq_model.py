"""
Linear-quadratic model — survival curves S(d) for tumor and late-responding tissue.

Chapter 16: Cancer, targeted therapies and radiotherapy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def sobrevivencia(d: np.ndarray, alpha: float, beta: float) -> np.ndarray:
    return np.exp(-alpha * d - beta * d**2)


def main() -> None:
    d = np.linspace(0, 10, 200)

    # Tumor: alpha/beta = 10 Gy
    alpha_t, beta_t = 0.3, 0.03
    # Late-responding tissue: alpha/beta = 3 Gy
    alpha_n, beta_n = 0.15, 0.05

    fig, ax = plt.subplots()
    ax.semilogy(d, sobrevivencia(d, alpha_t, beta_t),
                label=r"Tumor / acute ($\alpha/\beta$ = 10)")
    ax.semilogy(d, sobrevivencia(d, alpha_n, beta_n),
                label=r"Late-responding tissue ($\alpha/\beta$ = 3)")
    ax.axvline(2.0, color="gray", linestyle=":", label="d = 2 Gy")
    ax.set_xlabel("dose per fraction d (Gy)")
    ax.set_ylabel("Survival S(d)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
