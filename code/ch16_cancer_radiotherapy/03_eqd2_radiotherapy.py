"""
EQD2 calculation and comparison of radiotherapy regimens (Example 2).

Chapter 16: Cancer, targeted therapies and radiotherapy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def EQD2(n: int, d: float, ab: float = 10) -> float:
    return n*d*(d + ab)/(2 + ab)


def main() -> None:
    # For the tumor (alpha/beta = 10 Gy)
    A_t = EQD2(25, 2.0, 10)         # 50.0 Gy
    B_t = EQD2(15, 2.67, 10)        # 42.3 Gy

    # For late-responding normal tissue (alpha/beta = 3 Gy)
    A_n = EQD2(25, 2.0, 3)          # 50.0 Gy
    B_n = EQD2(15, 2.67, 3)         # 45.4 Gy

    print(f"Regimen A (50 Gy/25 fx): EQD2 tumor = {A_t:.1f}  late = {A_n:.1f}")
    print(f"Regimen B (40 Gy/15 fx): EQD2 tumor = {B_t:.1f}  late = {B_n:.1f}")


if __name__ == "__main__":
    main()
