"""
Converting K_d -> binding ΔG for two hypothetical drugs (Example 1).

Chapter 11: Drug-receptor interaction and molecular pharmacology — Volume 4 of
the series "The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    R = 8.314e-3       # kJ/(mol·K)
    T = 310.0
    for nome, Kd in [("A", 100e-9), ("B", 1e-9)]:
        dG = -R*T*np.log(1.0/Kd)
        print(f"{nome}: ΔG° = {dG:.1f} kJ/mol")
    # A: ΔG° = -41.5 kJ/mol
    # B: ΔG° = -53.4 kJ/mol


if __name__ == "__main__":
    main()
