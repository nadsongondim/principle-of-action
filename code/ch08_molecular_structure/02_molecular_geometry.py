"""
Geometric functions — distances and angles from atomic coordinates.

Chapter 8: Molecular structure and potential energy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def distancia(ri: np.ndarray, rj: np.ndarray) -> float:
    return float(np.linalg.norm(ri - rj))


def angulo(ri: np.ndarray, rj: np.ndarray, rk: np.ndarray) -> float:
    u = ri - rj
    v = rk - rj
    cos_t = (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return float(np.arccos(np.clip(cos_t, -1.0, 1.0)))


def main() -> None:
    # water
    H1 = np.array([-0.7572,  0.5860, 0.0])
    O = np.array([ 0.0,     0.0,    0.0])
    H2 = np.array([ 0.7572,  0.5860, 0.0])

    rOH1 = distancia(H1, O)
    rOH2 = distancia(H2, O)
    theta_HOH = np.degrees(angulo(H1, O, H2))

    print(f"r(O-H1) = {rOH1:.4f} Å")
    print(f"r(O-H2) = {rOH2:.4f} Å")
    print(f"H-O-H angle = {theta_HOH:.2f}°")


if __name__ == "__main__":
    main()
