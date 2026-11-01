"""
Sensitivity analysis — sweeping a key parameter of the model.

Chapter 3: Modeling, Validation and Reproducibility — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def simular(parametro_k: float, t: np.ndarray | None = None) -> np.ndarray:
    """Exponential decay model evaluated on a vector of times."""
    if t is None:
        t = np.linspace(0, 20, 200)
    return np.exp(-parametro_k * t)


def main() -> None:
    t = np.linspace(0, 20, 200)

    fig, ax = plt.subplots()
    for k in [0.20, 0.25, 0.30, 0.35, 0.40]:
        resultado = simular(parametro_k=k, t=t)      # a sweep of the parameter
        ax.plot(t, resultado, label=f"k = {k:.2f}")
    ax.set_xlabel("time")
    ax.set_ylabel("y(t)")
    ax.legend()
    ax.set_title("Sensitivity sweep in k")
    plt.show()


if __name__ == "__main__":
    main()
