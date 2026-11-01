"""
Fitting parameters to synthetic data with curve_fit (decay model).

Chapter 2: Essential numerical methods — Volume 4 of the series "The Principle
of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def modelo(t: np.ndarray, y0: float, k: float) -> np.ndarray:
    return y0 * np.exp(-k * t)


def main() -> None:
    # generate synthetic data for the fit — test the method against a known truth
    rng = np.random.default_rng(0)
    y0_verd, k_verd = 2.0, 0.4
    t_dados = np.linspace(0, 10, 40)
    y_dados = modelo(t_dados, y0_verd, k_verd) + rng.normal(0, 0.05, t_dados.size)

    parametros, _ = curve_fit(modelo, t_dados, y_dados)
    print(f"fitted y0 = {parametros[0]:.4f}   fitted k = {parametros[1]:.4f}")

    fig, ax = plt.subplots()
    ax.plot(t_dados, y_dados, "o", label="data")
    ax.plot(t_dados, modelo(t_dados, *parametros), "-", label="fitted model")
    ax.set_xlabel("t")
    ax.set_ylabel("y(t)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
