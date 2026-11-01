"""
Symplectic velocity-Verlet integrator applied to the harmonic oscillator.

Compares energy conservation against the forward Euler method,
reproducing Figure 5.1 of the volume.

Chapter 5: Lagrangian, Hamiltonian and Phase Space — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def passo_verlet(x: float, v: float, h: float,
                 a_func: Callable[[float], float]) -> tuple[float, float]:
    a_n = a_func(x)
    x_novo = x + h * v + 0.5 * h**2 * a_n
    a_novo = a_func(x_novo)
    v_novo = v + 0.5 * h * (a_n + a_novo)
    return x_novo, v_novo


def passo_euler(x: float, v: float, h: float,
                a_func: Callable[[float], float]) -> tuple[float, float]:
    a_n = a_func(x)
    x_novo = x + h * v
    v_novo = v + h * a_n
    return x_novo, v_novo


def main() -> None:
    h = 0.1
    n_passos = 200
    a_func = lambda x: -x       # oscillator with m=k=1

    x_v, v_v = 1.0, 0.0
    x_e, v_e = 1.0, 0.0
    E_verlet = np.empty(n_passos + 1)
    E_euler = np.empty(n_passos + 1)
    tempos = np.arange(n_passos + 1) * h

    E_verlet[0] = 0.5 * v_v**2 + 0.5 * x_v**2
    E_euler[0] = 0.5 * v_e**2 + 0.5 * x_e**2

    for i in range(1, n_passos + 1):
        x_v, v_v = passo_verlet(x_v, v_v, h, a_func)
        x_e, v_e = passo_euler(x_e, v_e, h, a_func)
        E_verlet[i] = 0.5 * v_v**2 + 0.5 * x_v**2
        E_euler[i] = 0.5 * v_e**2 + 0.5 * x_e**2

    fig, ax = plt.subplots()
    ax.plot(tempos, E_verlet, label="Verlet (symplectic)")
    ax.plot(tempos, E_euler, label="Forward Euler")
    ax.axhline(0.5, color="k", linestyle=":", label="exact E = 0.5")
    ax.set_xlabel("t")
    ax.set_ylabel("E(t)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
