"""
Answer key Ch. 13 — Ex. 6 (Challenge): Windkessel comparing compliances.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


T, t_sys, SV = 0.9, 0.3, 70.0              # cycle (s), systole (s), stroke volume (mL)


def Q(t: float) -> float:                  # aortic flow (half-sine)
    tt = t % T
    if tt < t_sys:
        return (np.pi*SV/(2*t_sys)) * np.sin(np.pi*tt/t_sys)
    return 0.0


def main() -> None:
    for R_, C_, rotulo in [(1.3, 1.2, "normal"), (1.3, 0.6, "stiff")]:
        sol = solve_ivp(lambda t, P: (Q(t) - P/R_)/C_,
                        [0, 5], [80.0],
                        t_eval=np.linspace(0, 5, 2000), max_step=0.005)
        P = sol.y[0][sol.t > 5 - 2*T]          # last two cycles
        print(rotulo, round(P.max()), round(P.min()),
              round(P.max()-P.min()), round(P.mean()))
    # normal 122 82 40 101
    # stiff 144 65 79 101


if __name__ == "__main__":
    main()
