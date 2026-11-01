"""
Arrhenius equation — ratio between rates at 25 °C and 35 °C (the Q10 rule).

Chapter 9: Reaction pathways, free energy and kinetics — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    Ea = 50e3                # J/mol
    R = 8.314                # J/(mol·K)
    T1, T2 = 298.0, 308.0
    razao = np.exp(-Ea/R * (1/T2 - 1/T1))
    # razao ≈ 1.93
    print(f"k(308 K) / k(298 K) ≈ {razao:.3f}")
    print(f"Q10 rule: approximately 2 when Ea ~ 50 kJ/mol")


if __name__ == "__main__":
    main()
