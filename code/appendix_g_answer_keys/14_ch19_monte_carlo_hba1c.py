"""
Answer key Ch. 19 — Ex. 6 (Challenge): Monte Carlo of the HbA1c trajectory.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


N = 1000
t = np.linspace(0, 112, 50)              # 16 weeks in days


def cenario(H0: float, Hinf_med: float, Hinf_sd: float,
            tau_med: float = 60, tau_sd: float = 10) -> np.ndarray:
    rng = np.random.default_rng(0)
    Hinf = rng.normal(Hinf_med, Hinf_sd, N)
    tau = rng.normal(tau_med, tau_sd, N)
    return Hinf[:, None] + (H0 - Hinf[:, None]) * np.exp(-t[None, :]/tau[:, None])


def main() -> None:
    A = cenario(9.1, 9.0, 0.3)               # keep current regimen
    B = cenario(9.1, 7.0, 0.4)               # +GLP-1

    i12 = int(np.argmin(np.abs(t - 84)))     # ~12 weeks
    for M, nome in [(A, "A (keep)"), (B, "B (+GLP-1)")]:
        p5, p95 = np.percentile(M[:, -1], [5, 95])
        print(f"{nome}: median 12 wk {np.median(M[:, i12]):.2f}%  "
              f"16 wk {np.median(M[:, -1]):.2f}%  band 16 wk {p5:.2f}–{p95:.2f}  "
              f"P(H ≤ 7%) = {np.mean(M[:, -1] <= 7.0):.0%}")
    # A: ~9.0%, band ~8.6–9.4, P = 0%;  B: ~7.5% (12 wk), ~7.3% (16 wk),
    # band ~6.7–7.9, P ≈ 20% (16–20%, depending on the seed)

    fig, ax = plt.subplots()
    for M, nome, cor in [(A, "keep", "C0"), (B, "+GLP-1", "C1")]:
        ax.plot(t/7, np.median(M, axis=0), color=cor, label=f"{nome} (median)")
        ax.fill_between(t/7,
                        np.percentile(M, 5, axis=0),
                        np.percentile(M, 95, axis=0),
                        color=cor, alpha=0.2)
    ax.axhline(7.0, color="red", linestyle="--", label="target 7%")
    ax.set_xlabel("weeks")
    ax.set_ylabel("HbA1c (%)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
