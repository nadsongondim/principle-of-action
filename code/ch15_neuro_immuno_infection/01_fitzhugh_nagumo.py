"""
FitzHugh-Nagumo model — neuronal excitability with two stimuli compared.

Chapter 15: Neurophysiology, immunology and infection — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


a, b, eps = 0.7, 0.8, 0.08


def I_pulse(t: float, amp: float, t0: float = 5.0, dur: float = 1.0) -> float:
    return amp if t0 <= t <= t0 + dur else 0.0


def fn(t: float, y: np.ndarray, amp: float) -> list[float]:
    v, w = y
    return [v - v**3/3 - w + I_pulse(t, amp),
            eps*(v + a - b*w)]


def main() -> None:
    y0 = [-1.1994, -0.6243]                  # rest
    t_span = (0.0, 50.0)

    # small max_step: without it the adaptive step "skips" the 1-time-unit
    # pulse and v stays at rest for any amplitude.
    fig, ax = plt.subplots()
    for amp, rotulo, estilo in [(0.60, "subthreshold (0.60)", "--"),
                                 (1.20, "suprathreshold (1.20)", "-")]:
        sol = solve_ivp(fn, t_span, y0, args=(amp,), max_step=0.05)
        print(amp, sol.y[0].max())           # peak of v: ≈ -0.46 and ≈ 1.80
        ax.plot(sol.t, sol.y[0], estilo, label=rotulo)

    ax.set_xlabel("t")
    ax.set_ylabel("v(t)")
    ax.set_title("FitzHugh-Nagumo — firing threshold")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
