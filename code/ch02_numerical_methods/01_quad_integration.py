"""
Adaptive numerical integration with quad — Gaussian integral from 0 to infinity.

Chapter 2: Essential numerical methods — Volume 4 of the series "The Principle
of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import quad


def main() -> None:
    valor, erro = quad(lambda x: np.exp(-x**2), 0, np.inf)
    print(f"value = {valor:.10f}   estimated error = {erro:.2e}")
    # expected value: sqrt(pi)/2 ≈ 0.8862269255


if __name__ == "__main__":
    main()
