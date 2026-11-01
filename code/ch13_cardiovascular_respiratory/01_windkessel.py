"""
Arterial Windkessel model — pulsatile pressure over several cycles.

The flow Q(t) is discontinuous (a half-sine in systole, zero in diastole),
which violates the smoothness assumption of adaptive integrators: without a
controlled maximum step, RK45 may jump over a transition between phases
and produce absurd pressures. That is why we set `max_step=0.005 s`,
ensuring that the solver sees every edge of Q(t).

Chapter 13: Cardiovascular and respiratory systems — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


T, t_sys = 0.9, 0.3                     # cardiac cycle and systole duration
SV = 70.0                                # stroke volume (mL)
R, C = 1.3, 1.2                          # mmHg·s/mL and mL/mmHg


def Q(t: float) -> float:
    tt = t % T
    if tt < t_sys:
        return (np.pi*SV/(2*t_sys)) * np.sin(np.pi*tt/t_sys)
    return 0.0


def windkessel(t: float, P: np.ndarray) -> float:
    return (Q(t) - P/R) / C


def main() -> None:
    sol = solve_ivp(windkessel, [0, 5], [80.0],
                    t_eval=np.linspace(0, 5, 2000), max_step=0.005)

    fig, ax = plt.subplots()
    ax.plot(sol.t, sol.y[0])
    ax.set_xlabel("t (s)")
    ax.set_ylabel("P (mmHg)")
    ax.set_title("Windkessel — pulsatile arterial pressure")
    plt.show()


if __name__ == "__main__":
    main()
