"""
Answer key Ch. 17 — Ex. 6 (Challenge): Gompertz fit to simulated CT volumes.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import curve_fit


def gompertz(t: np.ndarray, r: float, V0: float = 1.0, Vinf: float = 100.0) -> np.ndarray:
    return Vinf * np.exp(np.log(V0/Vinf)*np.exp(-r*t))


def main() -> None:
    t = np.array([0, 90, 180, 270, 360])
    V_true = gompertz(t, 0.005)
    rng = np.random.default_rng(0)
    ruido = rng.normal(1.0, 0.05, len(t))    # 5% segmentation noise
    V_obs = V_true * ruido

    (r_fit,), cov = curve_fit(gompertz, t, V_obs, p0=[0.01])
    print(f"fitted r = {r_fit:.5f}   (true r = 0.00500)")
    print(f"relative bias = {(r_fit - 0.005)/0.005*100:+.2f}%")


if __name__ == "__main__":
    main()
