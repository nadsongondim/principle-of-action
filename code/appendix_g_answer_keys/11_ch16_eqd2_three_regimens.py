"""
Answer key Ch. 16 — Ex. 6 (Challenge): EQD2 of the three regimens (conventional, hypo, SBRT).

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def EQD2(n: int, d: float, ab: float) -> float:
    return n*d*(d + ab)/(2 + ab)


def main() -> None:
    for n, d in [(30, 2.0), (15, 2.67), (5, 10.0)]:
        print(n, d, "tumor:",  round(EQD2(n, d, 10), 1),
              "late:", round(EQD2(n, d, 3), 1))


if __name__ == "__main__":
    main()
