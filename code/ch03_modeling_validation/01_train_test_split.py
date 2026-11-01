"""
Calibration/validation split with train_test_split (decay model).

Chapter 3: Modeling, Validation and Reproducibility — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import curve_fit
from sklearn.model_selection import train_test_split


def modelo(t: np.ndarray, y0: float, k: float) -> np.ndarray:
    return y0 * np.exp(-k * t)


def main() -> None:
    # synthetic data: the truth is known (y0=2, k=0.4)
    rng = np.random.default_rng(0)
    x = np.linspace(0, 10, 60)
    y = modelo(x, 2.0, 0.4) + rng.normal(0, 0.05, x.size)

    x_cal, x_val, y_cal, y_val = train_test_split(x, y, test_size=0.3, random_state=0)
    # calibrate ONLY with (x_cal, y_cal); validate with (x_val, y_val)

    parametros, _ = curve_fit(modelo, x_cal, y_cal)
    print(f"calibrated parameters: y0={parametros[0]:.4f}  k={parametros[1]:.4f}")

    residuo_cal = y_cal - modelo(x_cal, *parametros)
    residuo_val = y_val - modelo(x_val, *parametros)
    print(f"calibration RMSE = {np.sqrt(np.mean(residuo_cal**2)):.4f}")
    print(f"validation RMSE  = {np.sqrt(np.mean(residuo_val**2)):.4f}")


if __name__ == "__main__":
    main()
