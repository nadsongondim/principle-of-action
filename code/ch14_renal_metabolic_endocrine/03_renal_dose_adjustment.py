"""
Dose adjustment for renal function (Example 1) — aminoglycoside in a patient with CKD G3b.

Chapter 14: Renal, metabolic and endocrine systems — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def main() -> None:
    crcl = 34.4 / 100.0
    dose_normal = 240
    dose_ajustada = dose_normal * crcl
    # dose_ajustada ≈ 83 mg every 24 h
    print(f"Adjusted dose ≈ {dose_ajustada:.0f} mg every 24 h")


if __name__ == "__main__":
    main()
