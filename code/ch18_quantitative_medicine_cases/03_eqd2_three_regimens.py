"""
Comparison of three adjuvant radiotherapy regimens in breast cancer (Example 2).

Chapter 18: Integrated cases in quantitative medicine — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def EQD2(n: int, d: float, ab: float) -> float:
    return n*d*(d + ab) / (2 + ab)


def main() -> None:
    for n, d in [(25, 2.0), (15, 2.67), (5, 5.20)]:
        print(f"{n}×{d:.2f} Gy: "
              f"tumor (α/β=10): EQD2 = {EQD2(n,d,10):.1f}; "
              f"late (α/β=3): EQD2 = {EQD2(n,d,3):.1f}")
    # 25×2.00 Gy: tumor (α/β=10): EQD2 = 50.0; late (α/β=3): EQD2 = 50.0
    # 15×2.67 Gy: tumor (α/β=10): EQD2 = 42.3; late (α/β=3): EQD2 = 45.4
    # 5×5.20 Gy: tumor (α/β=10): EQD2 = 32.9; late (α/β=3): EQD2 = 42.6


if __name__ == "__main__":
    main()
