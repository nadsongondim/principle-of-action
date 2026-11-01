"""
Estimating creatinine clearance with the Cockcroft-Gault formula.

Chapter 14: Renal, metabolic and endocrine systems — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def cockcroft_gault(idade: float, peso_kg: float,
                    cr_sericamg: float, sexo: str) -> float:
    base = (140 - idade) * peso_kg / (72 * cr_sericamg)
    return base * (0.85 if sexo == 'F' else 1.0)


def main() -> None:
    # Woman, 72 years, 60 kg, Cr 1.4 mg/dL
    ccr = cockcroft_gault(72, 60, 1.4, 'F')      # ≈ 35 mL/min — moderate CKD
    print(f"Estimated CrCl = {ccr:.1f} mL/min")


if __name__ == "__main__":
    main()
