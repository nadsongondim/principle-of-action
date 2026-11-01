"""
Integrated breast cancer case — EQD2 of the conventional and hypofractionated regimens.

Chapter 18: Integrated cases in quantitative medicine — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def EQD2(n: int, d: float, ab: float) -> float:
    return n*d*(d + ab) / (2 + ab)


def main() -> None:
    for n, d in [(25, 2.0), (15, 2.67)]:
        print(f"{n}×{d} Gy: tumor EQD2 = {EQD2(n,d,10):.1f}, "
              f"late EQD2 = {EQD2(n,d,3):.1f}")
    # 25×2.0 Gy: tumor EQD2 = 50.0, late EQD2 = 50.0
    # 15×2.67 Gy: tumor EQD2 = 42.3, late EQD2 = 45.4


if __name__ == "__main__":
    main()
