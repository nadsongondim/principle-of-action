"""
Dose adjustment for renal function — drug eliminated mostly by the kidneys.

Chapter 12: Computational pharmacokinetics and pharmacodynamics — Volume 4 of
the series "The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def main() -> None:
    CL_normal = 5.0
    fr_renal = 0.8
    CCr_rel = 0.30
    CL_paciente = CL_normal * (1 - fr_renal + fr_renal * CCr_rel)
    C_ss = (1 * 90) / (12 * CL_paciente)
    # C_ss ≈ 3.4 mg/L  (above the window)

    print(f"Patient CL = {CL_paciente:.2f} L/h")
    print(f"C_ss with the standard dose = {C_ss:.2f} mg/L (target: within [0.5, 2.5])")

    # proportional adjustment to bring it back into the window
    D_ajustada = 90 * (CL_paciente / CL_normal)
    print(f"Recommended adjusted dose ≈ {D_ajustada:.0f} mg")


if __name__ == "__main__":
    main()
