"""
Fitting the Michaelis-Menten V_max and K_m to experimental data (Example 1).

Chapter 10: Enzyme kinetics and biochemical networks — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def mm(S: np.ndarray, Vmax: float, Km: float) -> np.ndarray:
    return Vmax * S / (Km + S)


def main() -> None:
    S = np.array([0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0])
    v = np.array([0.18, 0.32, 0.48, 0.67, 0.84, 0.91, 0.96])

    (Vmax, Km), _ = curve_fit(mm, S, v, p0=[1.0, 1.0])
    # Vmax ≈ 1.01   Km ≈ 1.05
    print(f"Vmax = {Vmax:.4f}    Km = {Km:.4f}")

    S_plot = np.linspace(0.01, 25, 200)
    fig, ax = plt.subplots()
    ax.plot(S, v, "o", label="data")
    ax.plot(S_plot, mm(S_plot, Vmax, Km), "-", label="MM fit")
    ax.set_xlabel("[S] (mM)")
    ax.set_ylabel("v (µmol/min)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
