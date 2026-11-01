"""
PK/PD of antimicrobials — extracting T>MIC and Cmax/MIC from C(t).

Compares two drugs: A (beta-lactam, time-dependent) and B
(aminoglycoside, concentration-dependent).

Chapter 15: Neurophysiology, immunology and infection — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def simular_doses_repetidas(C0: float, ke: float, tau: float,
                            n_doses: int, t_eval: np.ndarray) -> np.ndarray:
    """Sum of successive IV bolus curves (superposition principle)."""
    C = np.zeros_like(t_eval)
    for n in range(n_doses):
        t_relativo = t_eval - n * tau
        ativa = t_relativo >= 0
        C[ativa] += C0 * np.exp(-ke * t_relativo[ativa])
    return C


def main() -> None:
    MIC = 2.0
    total_time = 24.0
    t = np.linspace(0, total_time, 5000)

    # A: beta-lactam, t1/2 = 1.5 h, dose every 8 h
    keA = np.log(2) / 1.5
    CA = simular_doses_repetidas(C0=20.0, ke=keA, tau=8.0,
                                  n_doses=3, t_eval=t)

    # B: aminoglycoside, t1/2 = 2 h, single daily dose
    keB = np.log(2) / 2.0
    CB = simular_doses_repetidas(C0=50.0, ke=keB, tau=24.0,
                                  n_doses=1, t_eval=t)

    # Pseudocode: simulate C(t) and extract t > MIC for A and Cmax/MIC for B
    t_above_MIC = np.mean(CA > MIC)                # for A (uniform t)
    ratio_cmax = max(CB) / MIC                      # for B

    print(f"T>MIC (fraction) for A = {t_above_MIC:.2%}")
    print(f"Cmax/MIC for B = {ratio_cmax:.1f}")

    fig, ax = plt.subplots()
    ax.plot(t, CA, label="A (beta-lactam)")
    ax.plot(t, CB, label="B (aminoglycoside)")
    ax.axhline(MIC, color="red", linestyle="--", label="MIC")
    ax.set_xlabel("t (h)")
    ax.set_ylabel("C (µg/mL)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
