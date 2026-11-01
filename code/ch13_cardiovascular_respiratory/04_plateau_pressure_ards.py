"""
ARDS — plateau pressure for two tidal volumes (10 mL/kg vs 6 mL/kg).

Chapter 13: Cardiovascular and respiratory systems — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def main() -> None:
    Cp, Rv = 0.03, 10.0
    for VT in [0.70, 0.42]:          # 10 and 6 mL/kg ×70 kg
        P_plateau = VT / Cp           # cmH2O (elastic component)
        print(VT, P_plateau)
    # 0.70 → 23 cmH2O    (without the resistive term)
    # 0.42 → 14 cmH2O


if __name__ == "__main__":
    main()
