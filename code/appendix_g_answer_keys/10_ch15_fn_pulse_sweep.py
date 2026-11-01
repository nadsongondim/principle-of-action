"""
Answer key Ch. 15 — Ex. 6 (Challenge): amplitude sweep in the FN model.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def fn(t: float, y: np.ndarray, I_t: Callable[[float], float]) -> list[float]:
    v, w = y
    return [v - v**3/3 - w + I_t(t), 0.08*(v + 0.7 - 0.8*w)]


def pulso(amp: float, t0: float = 5, dur: float = 1) -> Callable[[float], float]:
    return lambda t: amp if t0 <= t <= t0+dur else 0.0


y0 = [-1.1994, -0.6243]                    # rest


def v_max(amp: float) -> float:            # small max_step: does not "skip" the pulse
    sol = solve_ivp(fn, [0, 50], y0, args=(pulso(amp),), max_step=0.05)
    return float(sol.y[0].max())


def main() -> None:
    # stimuli of Example 1 of ch. 15 (pulse of 1 time unit at t = 5)
    for amp in (0.55, 0.60, 1.20):
        print(f"I = {amp:.2f}: peak of v = {v_max(amp):+.2f}")
    # I = 0.55: -0.66 | I = 0.60: -0.46 (subthreshold) | I = 1.20: +1.80 (fires)

    amps = np.linspace(0.30, 1.20, 91)
    pico_v = np.array([v_max(a) for a in amps])
    dispara = pico_v > 1.0
    I_lim = amps[dispara.argmax()]             # first amplitude that fires
    print(f"sweep: threshold identified at I* ≈ {I_lim:.2f}")

    # refinement by bisection between the last one that does not fire and the first one that does
    lo, hi = amps[dispara.argmax() - 1], I_lim
    for _ in range(14):                         # 0.01 / 2**14 ≈ 6e-7
        meio = 0.5*(lo + hi)
        if v_max(meio) > 1.0:
            hi = meio
        else:
            lo = meio
    print(f"bisection: I* ≈ {hi:.4f}")
    # sweep: I* ≈ 0.61; bisection: I* ≈ 0.6065

    fig, ax = plt.subplots()
    ax.plot(amps, pico_v, "o-")
    ax.axhline(1.0, color="red", linestyle="--", label="criterion v=+1")
    ax.set_xlabel("pulse amplitude")
    ax.set_ylabel("peak of v")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
