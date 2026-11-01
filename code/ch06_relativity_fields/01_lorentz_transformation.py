"""
Lorentz transformation applied to an event — checks the invariance of the interval.

Chapter 6: Relativity, fields and electromagnetism — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def lorentz(beta: float) -> np.ndarray:
    g = 1.0 / np.sqrt(1.0 - beta**2)
    return np.array([[g, -g*beta], [-g*beta, g]])


def main() -> None:
    c = 1.0
    evento = np.array([3.0, 1.0])      # (ct, x)
    beta = 0.6
    Lambda = lorentz(beta)
    evento_linha = Lambda @ evento

    s2 = evento[0]**2 - evento[1]**2
    s2_linha = evento_linha[0]**2 - evento_linha[1]**2
    # s2 and s2_linha are both equal to 8.0

    print(f"event   = {evento}")
    print(f"event'  = {evento_linha}")
    print(f"s^2     = {s2}")
    print(f"s'^2    = {s2_linha}")


if __name__ == "__main__":
    main()
