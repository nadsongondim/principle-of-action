"""
Computing the dose needed to reach a target average steady-state concentration.

Chapter 12: Computational pharmacokinetics and pharmacodynamics — Volume 4 of
the series "The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def main() -> None:
    F, V, ke = 1.0, 50.0, 0.1
    CL = V * ke                       # 5 L/h
    C_ss_alvo = 1.5                   # mg/L
    tau = 12.0
    D = C_ss_alvo * tau * CL / F      # 90 mg

    print(f"CL = {CL} L/h")
    print(f"Recommended dose: {D:.1f} mg every {tau:.0f} h")
    print(f"to maintain an average C_ss ≈ {C_ss_alvo} mg/L")


if __name__ == "__main__":
    main()
