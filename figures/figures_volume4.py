#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
figures_volume4.py — Generates the technical figures of Volume 4
COMPUTATIONALLY, with Matplotlib. Same visual identity as the other volumes:
each figure is an exact, reproducible and version-controlled drawing, described by code.

Usage:
    python figures/figures_volume4.py            # generates all of them
    python figures/figures_volume4.py fig-01 ... # generates only the given ones

Output: figures/output/fig-NN-slug.png
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

RAIZ = Path(__file__).resolve().parent.parent
# Figures are saved to figures/output/ (created automatically; ignored by .gitignore)
IMG = RAIZ / "figures" / "output"

# Visual identity of the series (identical to Volumes 1 to 3)
NAVY = "#1b2a4a"
ACCENT = "#2f6fdb"
SOFT = "#98a4ba"
FILL = "#dce6f5"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "text.color": NAVY,
    "axes.edgecolor": NAVY,
    "axes.labelcolor": NAVY,
    "axes.unicode_minus": False,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "mathtext.fontset": "dejavusans",
})


def salvar(fig, slug: str) -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    destino = IMG / f"{slug}.png"
    fig.savefig(destino, dpi=200, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"  generated {destino.relative_to(RAIZ)}")


# ==========================================================================
# Chapter 1 — Development environment and project organization
# ==========================================================================
def fig01():
    """The anatomy of a reproducible simulation project."""
    fig, ax = plt.subplots(figsize=(9.8, 5.4))

    def caixa(cx, cy, w, h, texto, cor="white", fonte=11.0):
        ax.add_patch(FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0,rounding_size=0.12",
            facecolor=cor, edgecolor=SOFT, linewidth=1.3, zorder=3))
        ax.text(cx, cy, texto, ha="center", va="center", fontsize=fonte,
                color=NAVY, zorder=4)

    # inputs (left)
    entradas = [
        (2.0, 5.4, "Environment\n(pinned versions)"),
        (2.0, 3.6, "Code\n(scripts and notebooks)"),
        (2.0, 1.8, "Data"),
    ]
    for cx, cy, txt in entradas:
        caixa(cx, cy, 2.9, 1.25, txt, fonte=10.0)

    # run (center)
    caixa(6.4, 3.6, 2.5, 1.5, "Run", cor=FILL, fonte=12.5)

    # outputs (right)
    caixa(10.7, 4.5, 2.5, 1.25, "Figures", fonte=11.0)
    caixa(10.7, 2.7, 2.5, 1.25, "Report", fonte=11.0)

    seta = dict(arrowstyle="-|>", color=ACCENT, lw=2.0, mutation_scale=15)
    for cx, cy, _ in entradas:
        ax.annotate("", xy=(6.4 - 1.25, 3.6), xytext=(cx + 1.45, cy),
                    arrowprops=seta)
    for cy in (4.5, 2.7):
        ax.annotate("", xy=(10.7 - 1.25, cy), xytext=(6.4 + 1.25, 3.6),
                    arrowprops=seta)

    # version-control band
    ax.add_patch(FancyBboxPatch(
        (0.4, -0.65), 12.1, 0.95,
        boxstyle="round,pad=0,rounding_size=0.1",
        facecolor=FILL, edgecolor=SOFT, linewidth=1.2, zorder=2))
    ax.text(6.45, -0.18, "version control (Git) — records and versions the "
            "environment, the code and the data", ha="center", va="center",
            fontsize=10, color=NAVY, zorder=4)

    ax.text(6.45, 6.5, "a single command reruns the whole chain",
            ha="center", va="center", fontsize=10.5, color=SOFT)

    ax.set_xlim(0, 13.0)
    ax.set_ylim(-1.1, 6.9)
    ax.set_aspect("equal")
    ax.axis("off")
    salvar(fig, "fig-01-projeto-reproduzivel")


# ==========================================================================
# Chapter 2 — Essential numerical methods
# ==========================================================================
def fig02():
    """The same ODE solved by Euler: stable step × unstable step."""
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(9.8, 4.8))
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=13)

    # --- Panel A: small, stable step ---
    te = np.linspace(0, 10, 400)
    h = 0.5
    tA = np.arange(0, 10.01, h)
    yA = (1 - h) ** np.arange(len(tA))
    axA.annotate("", xy=(10.8, 0), xytext=(0, 0), arrowprops=seta)
    axA.annotate("", xy=(0, 1.32), xytext=(0, 0), arrowprops=seta)
    axA.plot(te, np.exp(-te), color=ACCENT, lw=2.8, zorder=3,
             label="exact solution")
    axA.plot(tA, yA, color=NAVY, lw=1.7, ls=(0, (5, 3)), marker="o", ms=5,
             zorder=4, label="Euler ($h=0.5$)")
    axA.set_title("small step: follows the solution", fontsize=10.5,
                  color=NAVY, pad=10)
    axA.text(10.8, -0.07, "$t$", ha="right", va="top", fontsize=10,
             color=NAVY)
    axA.text(-0.25, 1.32, "$y$", ha="right", va="top", fontsize=10,
             color=NAVY)
    axA.legend(loc="upper center", frameon=False, fontsize=8.5)
    axA.set_xlim(-1.4, 11.6)
    axA.set_ylim(-0.28, 1.5)
    axA.axis("off")

    # --- Panel B: step too large, unstable ---
    teB = np.linspace(0, 14, 400)
    hB = 2.3
    tB = np.arange(0, 14.01, hB)
    yB = (1 - hB) ** np.arange(len(tB))
    axB.plot([0, 14.5], [0, 0], color=SOFT, lw=0.9, zorder=1)
    axB.annotate("", xy=(15.4, 0), xytext=(0, 0), arrowprops=seta)
    axB.annotate("", xy=(0, 6.6), xytext=(0, -6.6), arrowprops=seta)
    axB.plot(teB, np.exp(-teB), color=ACCENT, lw=2.8, zorder=3,
             label="exact solution")
    axB.plot(tB, yB, color=NAVY, lw=1.7, ls=(0, (5, 3)), marker="o", ms=5,
             zorder=4, label="Euler ($h=2.3$)")
    axB.set_title("step too large: unstable", fontsize=10.5,
                  color=NAVY, pad=10)
    axB.text(15.4, -0.5, "$t$", ha="right", va="top", fontsize=10,
             color=NAVY)
    axB.text(-0.5, 6.6, "$y$", ha="right", va="top", fontsize=10,
             color=NAVY)
    axB.legend(loc="lower left", frameon=False, fontsize=8.5)
    axB.set_xlim(-2.0, 16.4)
    axB.set_ylim(-7.6, 7.8)
    axB.axis("off")

    fig.tight_layout(pad=1.4)
    salvar(fig, "fig-02-edo-euler")


# ==========================================================================
# Chapter 3 — Modeling, validation and reproducibility
# ==========================================================================
def fig03():
    """Calibration and validation: the adequate model × the overfitted model."""
    fig, ax = plt.subplots(figsize=(9.0, 5.4))

    # reproducible synthetic data
    rng = np.random.default_rng(42)
    x = np.array([0.5, 1.3, 2.0, 2.9, 3.7, 4.5, 5.4, 6.2, 7.1, 7.9, 8.7])
    y_true = 2.0 + 1.3 * x - 0.07 * x ** 2
    y = y_true + rng.normal(0, 0.55, size=x.size)

    idx_cal = np.array([0, 1, 3, 4, 6, 8, 10])
    idx_val = np.array([2, 5, 7, 9])
    x_cal, y_cal = x[idx_cal], y[idx_cal]
    x_val, y_val = x[idx_val], y[idx_val]

    # fits using only the calibration points
    coef_bom = np.polyfit(x_cal, y_cal, 2)
    coef_sobre = np.polyfit(x_cal, y_cal, 6)
    xs = np.linspace(0.2, 9.05, 600)
    y_bom = np.polyval(coef_bom, xs)
    y_sobre = np.polyval(coef_sobre, xs)

    # axes as arrows
    k = dict(arrowstyle="-|>", color=NAVY, lw=1.6, mutation_scale=15)
    ax.annotate("", xy=(9.4, 0), xytext=(0, 0), arrowprops=k)
    ax.annotate("", xy=(0, 13.5), xytext=(0, 0), arrowprops=k)

    # curves
    ax.plot(xs, y_sobre, color=NAVY, lw=2.0, ls=(0, (6, 4)), zorder=3,
            label="overfitted model")
    ax.plot(xs, y_bom, color=ACCENT, lw=2.8, zorder=4,
            label="adequate model")

    # points
    ax.plot(x_cal, y_cal, "o", color=NAVY, ms=9, zorder=6,
            label="calibration data")
    ax.plot(x_val, y_val, "o", markerfacecolor="white",
            markeredgecolor=NAVY, markeredgewidth=1.8, ms=10, zorder=6,
            label="validation data")

    # axis labels
    ax.text(9.4, -0.5, "input variable", ha="right", va="top",
            fontsize=10.5, color=NAVY)
    ax.text(-0.2, 13.5, "measured quantity", ha="right", va="top",
            rotation=90, fontsize=10.5, color=NAVY)

    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=2,
              frameon=False, fontsize=9.5)
    ax.set_xlim(-1.4, 10.0)
    ax.set_ylim(-2.4, 14.5)
    ax.axis("off")
    salvar(fig, "fig-03-calibracao-validacao")


# ==========================================================================
# Chapter 4 — Computational classical mechanics
# ==========================================================================
def fig04():
    """The harmonic oscillator: trajectory x(t) and phase portrait."""
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(9.6, 4.8))
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=13)

    t = np.linspace(0, 4 * np.pi, 500)
    x = np.cos(t)
    v = -np.sin(t)

    # --- Panel A: x(t) ---
    axA.annotate("", xy=(13.6, 0), xytext=(0, 0), arrowprops=seta)
    axA.annotate("", xy=(0, 1.45), xytext=(0, -1.45), arrowprops=seta)
    axA.plot([0, 13.4], [1.0, 1.0], color=SOFT, lw=0.8, ls=(0, (2, 3)),
             zorder=1)
    axA.plot([0, 13.4], [-1.0, -1.0], color=SOFT, lw=0.8, ls=(0, (2, 3)),
             zorder=1)
    axA.plot(t, x, color=ACCENT, lw=2.8, zorder=3)
    axA.set_title("$x(t)$ — periodic oscillation", fontsize=10.5,
                  color=NAVY, pad=10)
    axA.text(13.6, -0.18, "$t$", ha="right", va="top", fontsize=11,
             color=NAVY)
    axA.text(-0.4, 1.45, "$x$", ha="right", va="top", fontsize=11,
             color=NAVY)
    axA.text(-0.2, 1.0, "+1", ha="right", va="center", fontsize=9,
             color=SOFT)
    axA.text(-0.2, -1.0, "$-1$", ha="right", va="center", fontsize=9,
             color=SOFT)
    axA.set_xlim(-1.8, 14.6)
    axA.set_ylim(-1.7, 1.7)
    axA.axis("off")

    # --- Panel B: phase portrait ---
    axB.annotate("", xy=(1.55, 0), xytext=(-1.55, 0), arrowprops=seta)
    axB.annotate("", xy=(0, 1.55), xytext=(0, -1.55), arrowprops=seta)
    axB.plot(x, v, color=ACCENT, lw=2.8, zorder=3)
    axB.plot([1.0], [0.0], "o", color=NAVY, ms=9, zorder=5)
    axB.annotate("start\n$(1,\\,0)$", xy=(1.0, 0.0), xytext=(1.05, 0.8),
                 fontsize=9, color=NAVY,
                 arrowprops=dict(arrowstyle="-|>", color=SOFT, lw=1.2,
                                 mutation_scale=11))
    axB.set_title("phase portrait — energy conserved", fontsize=10.5,
                  color=NAVY, pad=10)
    axB.text(1.55, -0.1, "$x$", ha="right", va="top", fontsize=11,
             color=NAVY)
    axB.text(-0.08, 1.55, "$v$", ha="right", va="top", fontsize=11,
             color=NAVY)
    axB.set_xlim(-1.85, 1.85)
    axB.set_ylim(-1.85, 1.85)
    axB.set_aspect("equal")
    axB.axis("off")

    fig.tight_layout(pad=1.4)
    salvar(fig, "fig-04-oscilador-harmonico")


# ==========================================================================
# Chapter 5 — Lagrangian, Hamiltonian and phase space
# ==========================================================================
def fig05():
    """Energy conservation: Verlet (symplectic) × Euler (not symplectic)."""
    fig, ax = plt.subplots(figsize=(9.0, 5.2))

    h = 0.1
    n_steps = 200
    t = np.arange(n_steps + 1) * h

    # Forward Euler
    x_e = np.zeros(n_steps + 1)
    v_e = np.zeros(n_steps + 1)
    x_e[0], v_e[0] = 1.0, 0.0
    for i in range(n_steps):
        x_e[i + 1] = x_e[i] + h * v_e[i]
        v_e[i + 1] = v_e[i] - h * x_e[i]
    E_e = 0.5 * v_e ** 2 + 0.5 * x_e ** 2

    # Velocity Verlet
    x_v = np.zeros(n_steps + 1)
    v_v = np.zeros(n_steps + 1)
    x_v[0], v_v[0] = 1.0, 0.0
    for i in range(n_steps):
        a_n = -x_v[i]
        x_v[i + 1] = x_v[i] + h * v_v[i] + 0.5 * h ** 2 * a_n
        a_novo = -x_v[i + 1]
        v_v[i + 1] = v_v[i] + 0.5 * h * (a_n + a_novo)
    E_v = 0.5 * v_v ** 2 + 0.5 * x_v ** 2

    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.6, mutation_scale=15)
    ax.annotate("", xy=(21.5, 0), xytext=(0, 0), arrowprops=seta)
    ax.annotate("", xy=(0, 4.5), xytext=(0, 0), arrowprops=seta)

    ax.plot([0, 21], [0.5, 0.5], color=SOFT, lw=1.0, ls=(0, (5, 4)),
            zorder=1)
    ax.text(20.7, 0.62, "exact energy  $E = 0.5$", ha="right",
            va="bottom", fontsize=9, color=SOFT)

    ax.plot(t, E_e, color=NAVY, lw=2.4, ls=(0, (6, 4)), zorder=3,
            label="forward Euler (not symplectic)")
    ax.plot(t, E_v, color=ACCENT, lw=2.8, zorder=4,
            label="Verlet (symplectic)")

    ax.text(21.5, -0.18, "time  $t$", ha="right", va="top", fontsize=10.5,
            color=NAVY)
    ax.text(-0.45, 4.5, "energy  $E(t)$", ha="right", va="top",
            rotation=90, fontsize=10.5, color=NAVY)
    ax.plot([-0.18, 0], [0.5, 0.5], color=NAVY, lw=1.3)
    ax.text(-0.35, 0.5, "0.5", ha="right", va="center", fontsize=9,
            color=SOFT)

    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=2,
              frameon=False, fontsize=10)
    ax.set_xlim(-2.8, 23)
    ax.set_ylim(-0.6, 4.7)
    ax.axis("off")
    salvar(fig, "fig-05-energia-simpletico")


# ==========================================================================
# Chapter 6 — Relativity, fields and electromagnetism
# ==========================================================================
def fig06():
    """1D wave equation by finite differences (scalar FDTD, CFL = 0.5)."""
    fig, ax = plt.subplots(figsize=(9.4, 5.4))

    # parameters
    L = 10.0
    Nx = 401
    x = np.linspace(0.0, L, Nx)
    dx = L / (Nx - 1)
    c = 1.0
    dt = 0.5 * dx / c                # CFL = 0.5 (stable)
    sigma = 0.5
    alpha = (c * dt / dx) ** 2

    # initial condition: centered Gaussian pulse, zero initial velocity
    u_prev = np.exp(-((x - L / 2) / sigma) ** 2)

    # first step (with du/dt(0) = 0)
    u_curr = np.zeros_like(u_prev)
    u_curr[1:-1] = (u_prev[1:-1] + 0.5 * alpha *
                    (u_prev[2:] - 2 * u_prev[1:-1] + u_prev[:-2]))
    u_curr[0] = 0.0
    u_curr[-1] = 0.0

    # time instants to store
    tempos = [0.0, 1.5, 3.0, 4.5]
    snapshots = {0.0: u_prev.copy()}

    n_max = int(tempos[-1] / dt) + 2
    for n in range(1, n_max + 1):
        u_next = np.zeros_like(u_curr)
        u_next[1:-1] = (2 * u_curr[1:-1] - u_prev[1:-1] + alpha *
                        (u_curr[2:] - 2 * u_curr[1:-1] + u_curr[:-2]))
        u_next[0] = 0.0
        u_next[-1] = 0.0
        u_prev = u_curr
        u_curr = u_next
        t_now = n * dt
        for t_alvo in tempos[1:]:
            if t_alvo not in snapshots and abs(t_now - t_alvo) < dt / 2:
                snapshots[t_alvo] = u_curr.copy()

    # plot waterfall
    offsets = {0.0: 0.0, 1.5: 1.3, 3.0: 2.6, 4.5: 3.9}
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=13)
    ax.annotate("", xy=(L + 1.0, 0), xytext=(-0.2, 0), arrowprops=seta)
    ax.text(L + 1.0, -0.18, "$x$", ha="right", va="top", fontsize=11,
            color=NAVY)

    for t_snap in tempos:
        u_snap = snapshots[t_snap]
        off = offsets[t_snap]
        ax.plot([0, L], [off, off], color=SOFT, lw=0.6, ls=(0, (2, 3)),
                zorder=1)
        ax.plot(x, u_snap + off, color=ACCENT, lw=2.4, zorder=3)
        rotulo = f"$t = {t_snap:.1f}$"
        ax.text(-0.5, off + 0.5, rotulo, ha="right", va="center",
                fontsize=10, color=NAVY)

    ax.text(L / 2, -0.6, "initial Gaussian pulse  ($t = 0$)", ha="center",
            va="top", fontsize=9, color=SOFT)
    ax.text(L / 2, offsets[4.5] + 1.3,
            "two traveling waves: one to the left, one to the right "
            "($\\Delta t \\cdot c / \\Delta x = 0.5$)",
            ha="center", va="center", fontsize=9, color=SOFT)

    ax.set_xlim(-2.5, L + 1.5)
    ax.set_ylim(-0.9, 5.6)
    ax.axis("off")
    salvar(fig, "fig-06-equacao-onda")


# ==========================================================================
# Chapter 7 — Computational quantum mechanics
# ==========================================================================
def fig07():
    """The first eigenstates of the quantum harmonic oscillator."""
    fig, ax = plt.subplots(figsize=(8.8, 5.4))

    x = np.linspace(-4.5, 4.5, 600)
    V = 0.5 * x ** 2

    # Hermite polynomials (physicists') for n = 0, 1, 2, 3
    Hn = [
        np.ones_like(x),
        2 * x,
        4 * x ** 2 - 2,
        8 * x ** 3 - 12 * x,
    ]
    fat = [1, 1, 2, 6]
    fator_amp = 0.5

    # potential
    ax.plot(x, V, color=NAVY, lw=2.4, zorder=4)
    ax.text(3.05, 4.65, "$V(x) = \\frac{1}{2}\\, x^2$", ha="left",
            va="center", fontsize=10, color=NAVY)

    # eigenstates
    for n in range(4):
        E_n = n + 0.5
        norm = 1.0 / np.sqrt(2 ** n * fat[n] * np.sqrt(np.pi))
        psi = norm * Hn[n] * np.exp(-x ** 2 / 2)
        ax.plot([-4.7, 4.7], [E_n, E_n], color=SOFT, lw=0.9,
                ls=(0, (3, 3)), zorder=1)
        ax.plot(x, fator_amp * psi + E_n, color=ACCENT, lw=2.2, zorder=3)
        ax.text(4.9, E_n, f"$n={n}$,  $E={2*n+1}/2$", ha="left",
                va="center", fontsize=9.5, color=NAVY)

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(4.8, 0), xytext=(-4.8, 0), arrowprops=seta)
    ax.annotate("", xy=(0, 4.9), xytext=(0, -0.5), arrowprops=seta)
    ax.text(4.8, -0.15, "$x$", ha="right", va="top", fontsize=11,
            color=NAVY)
    ax.text(-0.15, 4.9, "energy (in units of $\\hbar\\omega$)", ha="right",
            va="top", rotation=90, fontsize=10, color=NAVY)

    ax.set_xlim(-6.4, 8.0)
    ax.set_ylim(-0.8, 5.2)
    ax.axis("off")
    salvar(fig, "fig-07-oscilador-quantico")


# ==========================================================================
# Chapter 8 — Molecular structure and potential energy
# ==========================================================================
def fig08():
    """Lennard-Jones potential: the shape of the nonbonded interaction."""
    fig, ax = plt.subplots(figsize=(8.6, 5.4))

    sigma, eps = 1.0, 1.0
    r = np.linspace(0.95, 3.0, 700)
    V = 4 * eps * ((sigma / r) ** 12 - (sigma / r) ** 6)
    r_min = 2 ** (1.0 / 6.0) * sigma     # ≈ 1.1225

    # axes as arrows
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(3.2, 0), xytext=(0.82, 0), arrowprops=seta)
    ax.annotate("", xy=(0.82, 1.45), xytext=(0.82, -1.45), arrowprops=seta)

    # curve
    ax.plot(r, V, color=ACCENT, lw=2.8, zorder=4)

    # sigma marker (crossing V = 0)
    ax.plot([sigma, sigma], [0.0, -0.10], color=SOFT, lw=0.9,
            ls=(0, (3, 3)), zorder=2)
    ax.text(sigma, -0.15, "$\\sigma$", ha="center", va="top", fontsize=12,
            color=NAVY)

    # r_min marker
    ax.plot([r_min, r_min], [-eps, 0.06], color=SOFT, lw=0.9,
            ls=(0, (3, 3)), zorder=2)
    ax.plot([r_min], [-eps], "o", color=NAVY, ms=6, zorder=5)
    ax.text(r_min, 0.12, "$r_{\\mathrm{min}}$", ha="center", va="bottom",
            fontsize=11, color=NAVY)

    # epsilon depth
    ax.plot([r_min, 2.45], [-eps, -eps], color=SOFT, lw=0.7,
            ls=(0, (2, 3)), zorder=2)
    ax.annotate("", xy=(2.4, 0.0), xytext=(2.4, -eps),
                arrowprops=dict(arrowstyle="<|-|>", color=SOFT, lw=1.3,
                                mutation_scale=11))
    ax.text(2.5, -eps / 2, "$\\varepsilon$", ha="left", va="center",
            fontsize=12, color=NAVY)

    # axis labels
    ax.text(3.2, -0.07, "$r$", ha="right", va="top", fontsize=11,
            color=NAVY)
    ax.text(0.78, 1.45, "$V(r)$", ha="right", va="top", rotation=90,
            fontsize=11, color=NAVY)

    # title / formula
    ax.text(2.0, 1.32,
            "Lennard-Jones:  "
            "$V(r) = 4\\varepsilon\\left[(\\sigma/r)^{12} - "
            "(\\sigma/r)^{6}\\right]$",
            ha="center", va="center", fontsize=10.5, color=NAVY)

    # "repulsion" / "attraction" annotations — placed away from the curve
    ax.text(0.99, 1.05, "repulsion\n($r^{-12}$)", ha="left", va="center",
            fontsize=9, color=NAVY)
    ax.text(2.7, -1.35, "van der Waals attraction  ($r^{-6}$)",
            ha="center", va="center", fontsize=9, color=NAVY)

    ax.set_xlim(0.5, 3.4)
    ax.set_ylim(-1.7, 1.7)
    ax.axis("off")
    salvar(fig, "fig-08-lennard-jones")


# ==========================================================================
# Chapter 9 — Reaction pathways, free energy and kinetics
# ==========================================================================
def fig09():
    """Canonical reaction profile: minima, barrier and transition state."""
    from scipy.interpolate import CubicSpline
    fig, ax = plt.subplots(figsize=(9.4, 5.6))

    s_key = np.array([0.0, 1.0, 2.0, 3.5, 5.0, 6.5, 8.0, 9.0, 10.0])
    E_key = np.array([1.5, -1.5, -3.0, -1.0, 1.5, -2.5, -5.0, -3.5, -1.5])
    cs = CubicSpline(s_key, E_key)
    s = np.linspace(0, 10, 600)
    E = cs(s)

    E_react = -3.0
    E_TS = 1.5
    E_prod = -5.0
    base = -7.0

    # axes as arrows
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(10.8, base), xytext=(-0.3, base), arrowprops=seta)
    ax.annotate("", xy=(-0.3, 3.5), xytext=(-0.3, base - 0.3), arrowprops=seta)

    # curve
    ax.plot(s, E, color=ACCENT, lw=2.8, zorder=3)

    # stationary points
    ax.plot([2.0], [E_react], "o", color=NAVY, ms=7, zorder=5)
    ax.text(2.0, E_react - 0.6, "reactants", ha="center", va="top",
            fontsize=10, color=NAVY)

    ax.plot([5.0], [E_TS], "o", color=NAVY, ms=7, zorder=5)
    ax.text(5.0, E_TS + 0.4, "transition state", ha="center",
            va="bottom", fontsize=10, color=NAVY)

    ax.plot([8.0], [E_prod], "o", color=NAVY, ms=7, zorder=5)
    ax.text(8.0, E_prod - 0.6, "products", ha="center", va="top",
            fontsize=10, color=NAVY)

    # E_a bracket
    s_Ea = 3.2
    ax.plot([2.0, s_Ea], [E_react, E_react], color=SOFT, lw=0.7,
            ls=(0, (2, 3)), zorder=2)
    ax.plot([5.0, s_Ea], [E_TS, E_TS], color=SOFT, lw=0.7, ls=(0, (2, 3)),
            zorder=2)
    ax.annotate("", xy=(s_Ea, E_TS), xytext=(s_Ea, E_react),
                arrowprops=dict(arrowstyle="<|-|>", color=SOFT, lw=1.4,
                                mutation_scale=11))
    ax.text(s_Ea - 0.2, (E_TS + E_react) / 2, "$E_a$", ha="right",
            va="center", fontsize=13, color=NAVY)

    # Delta E bracket
    s_dE = 10.5
    ax.plot([2.0, s_dE], [E_react, E_react], color=SOFT, lw=0.7,
            ls=(0, (2, 3)), zorder=2)
    ax.plot([8.0, s_dE], [E_prod, E_prod], color=SOFT, lw=0.7,
            ls=(0, (2, 3)), zorder=2)
    ax.annotate("", xy=(s_dE, E_prod), xytext=(s_dE, E_react),
                arrowprops=dict(arrowstyle="<|-|>", color=SOFT, lw=1.4,
                                mutation_scale=11))
    ax.text(s_dE + 0.2, (E_react + E_prod) / 2, "$\\Delta E$", ha="left",
            va="center", fontsize=13, color=NAVY)

    # axis labels
    ax.text(10.8, base - 0.3, "reaction coordinate  $s$", ha="right",
            va="top", fontsize=10.5, color=NAVY)
    ax.text(-0.4, 3.5, "energy  $E(s)$", ha="right", va="top",
            rotation=90, fontsize=10.5, color=NAVY)

    ax.set_xlim(-1.7, 12.6)
    ax.set_ylim(base - 1.0, 4.0)
    ax.axis("off")
    salvar(fig, "fig-09-perfil-reacao")


# ==========================================================================
# Chapter 10 — Enzyme kinetics and biochemical networks
# ==========================================================================
def fig10():
    """Michaelis-Menten and Hill curves: hyperbola × sigmoid."""
    fig, ax = plt.subplots(figsize=(9.0, 5.4))

    S = np.linspace(0, 8.0, 600)
    Vmax = 1.0
    Km = 1.0
    v_mm = Vmax * S / (Km + S)
    v_hill = Vmax * S ** 2.5 / (Km ** 2.5 + S ** 2.5)

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(8.7, 0), xytext=(-0.3, 0), arrowprops=seta)
    ax.annotate("", xy=(-0.3, 1.32), xytext=(-0.3, -0.05), arrowprops=seta)

    # reference lines
    ax.plot([0, 8.4], [Vmax, Vmax], color=SOFT, lw=0.8, ls=(0, (3, 3)),
            zorder=1)
    ax.text(8.3, Vmax + 0.04, "$V_{\\max}$", ha="right", va="bottom",
            fontsize=10, color=SOFT)

    ax.plot([0, 8.4], [Vmax / 2, Vmax / 2], color=SOFT, lw=0.8,
            ls=(0, (3, 3)), zorder=1)
    ax.text(8.3, Vmax / 2 + 0.03, "$V_{\\max}/2$", ha="right", va="bottom",
            fontsize=9, color=SOFT)

    ax.plot([Km, Km], [0, Vmax / 2 + 0.04], color=SOFT, lw=0.8,
            ls=(0, (3, 3)), zorder=1)
    ax.text(Km, -0.04, "$K_m$", ha="center", va="top", fontsize=11,
            color=NAVY)

    # curves
    ax.plot(S, v_mm, color=ACCENT, lw=2.8, zorder=3,
            label="Michaelis–Menten  ($n=1$)")
    ax.plot(S, v_hill, color=NAVY, lw=2.4, ls=(0, (6, 3)), zorder=3,
            label="cooperative Hill  ($n=2.5$)")

    # axis labels
    ax.text(8.7, -0.07, "$[S]$", ha="right", va="top", fontsize=12,
            color=NAVY)
    ax.text(-0.45, 1.32, "$v$", ha="right", va="top", rotation=90,
            fontsize=12, color=NAVY)

    ax.legend(loc="lower right", bbox_to_anchor=(0.98, 0.10),
              frameon=False, fontsize=10)
    ax.set_xlim(-1.1, 9.6)
    ax.set_ylim(-0.22, 1.45)
    ax.axis("off")
    salvar(fig, "fig-10-mm-hill")


# ==========================================================================
# Chapter 11 — Drug-receptor interaction and molecular pharmacology
# ==========================================================================
def fig11():
    """Dose-response curves: agonist, competitive × noncompetitive antagonism."""
    fig, ax = plt.subplots(figsize=(9.4, 5.4))

    log_D = np.linspace(-3.0, 3.0, 700)
    D = 10 ** log_D
    EC50 = 1.0

    E_ag = D / (EC50 + D)
    E_comp = D / (10.0 * EC50 + D)      # competitive antagonist (EC50 × 10)
    E_nc = 0.5 * D / (EC50 + D)         # noncompetitive antagonist (Emax × 0.5)

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(3.8, 0), xytext=(-3.3, 0), arrowprops=seta)
    ax.annotate("", xy=(-3.3, 1.32), xytext=(-3.3, -0.05), arrowprops=seta)

    # reference lines
    ax.plot([-3.0, 3.6], [1.0, 1.0], color=SOFT, lw=0.8, ls=(0, (3, 3)),
            zorder=1)
    ax.text(3.6, 1.04, "$E_{\\max}$", ha="right", va="bottom",
            fontsize=10, color=SOFT)
    ax.plot([-3.0, 3.6], [0.5, 0.5], color=SOFT, lw=0.8, ls=(0, (3, 3)),
            zorder=1)
    ax.plot([0, 0], [0, 0.55], color=SOFT, lw=0.8, ls=(0, (3, 3)),
            zorder=1)
    ax.text(0, -0.06, "$\\mathrm{EC}_{50}$", ha="center", va="top",
            fontsize=11, color=NAVY)

    # curves
    ax.plot(log_D, E_ag, color=ACCENT, lw=2.8, zorder=4,
            label="agonist alone")
    ax.plot(log_D, E_comp, color=NAVY, lw=2.4, ls=(0, (6, 3)), zorder=3,
            label="$+$ competitive antagonist")
    ax.plot(log_D, E_nc, color=NAVY, lw=2.4, ls=(0, (2, 2)), zorder=3,
            label="$+$ noncompetitive antagonist")

    # axis labels
    ax.text(3.8, -0.08, "$\\log_{10}\\,[D]/\\mathrm{EC}_{50}$",
            ha="right", va="top", fontsize=11, color=NAVY)
    ax.text(-3.05, 1.32, "$E/E_{\\max}$", ha="left", va="top",
            fontsize=12, color=NAVY)

    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.78),
              frameon=False, fontsize=9.5)
    ax.set_xlim(-4.2, 4.4)
    ax.set_ylim(-0.22, 1.45)
    ax.axis("off")
    salvar(fig, "fig-11-dose-resposta")


# ==========================================================================
# Chapter 12 — Computational pharmacokinetics and pharmacodynamics
# ==========================================================================
def fig12():
    """Repeated oral doses: accumulation, steady state, window."""
    fig, ax = plt.subplots(figsize=(9.8, 5.6))

    ka, ke = 1.5, 0.3
    F, V, dose, tau = 1.0, 1.0, 100.0, 6.0
    n_doses = 6

    t = np.linspace(0, n_doses * tau + 4, 1500)
    coef = F * dose * ka / (V * (ka - ke))

    C = np.zeros_like(t)
    for i in range(n_doses):
        tr = t - i * tau
        bateman = coef * (np.exp(-ke * tr) - np.exp(-ka * tr))
        C += np.where(tr >= 0, bateman, 0.0)

    Cmin_ter, Cmax_ter = 12.0, 90.0
    t_lim = n_doses * tau + 4
    y_max = float(np.max(C)) * 1.18

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(t_lim + 2, 0), xytext=(-2.0, 0), arrowprops=seta)
    ax.annotate("", xy=(-2.0, y_max), xytext=(-2.0, -8), arrowprops=seta)

    # therapeutic window
    ax.fill_between([0, t_lim], Cmin_ter, Cmax_ter, color=FILL, alpha=0.55,
                    zorder=1)
    ax.text(t_lim + 0.3, (Cmin_ter + Cmax_ter) / 2,
            "therapeutic\nwindow", ha="left", va="center",
            fontsize=9.5, color=NAVY)

    # concentration curve
    ax.plot(t, C, color=ACCENT, lw=2.6, zorder=3)

    # dose markers
    for i in range(n_doses):
        td = i * tau
        ax.plot([td, td], [-6, -1.5], color=NAVY, lw=2.0, zorder=3)
    ax.text(n_doses * tau / 2 - 1.5, -10,
            "oral doses separated by  $\\tau$", ha="center", va="top",
            fontsize=10, color=SOFT)

    # steady state
    ax.annotate("steady state",
                xy=(n_doses * tau - 1.0, 78.0),
                xytext=(n_doses * tau + 5, y_max * 0.88),
                arrowprops=dict(arrowstyle="->", color=SOFT, lw=1.2),
                fontsize=9.5, color=NAVY, ha="left", va="center")

    # axis labels
    ax.text(t_lim + 2, -3, "time", ha="right", va="top", fontsize=11,
            color=NAVY)
    ax.text(-2.6, y_max, "$C(t)$", ha="right", va="top", fontsize=12,
            color=NAVY)

    ax.set_xlim(-6.5, t_lim + 14)
    ax.set_ylim(-14, y_max + 5)
    ax.axis("off")
    salvar(fig, "fig-12-doses-repetidas")


# ==========================================================================
# Chapter 13 — Cardiovascular and respiratory systems
# ==========================================================================
def fig13():
    """Windkessel: blood pressure, normotensive × hypertensive."""
    from scipy.integrate import solve_ivp
    fig, ax = plt.subplots(figsize=(9.6, 5.4))

    T_cyc, t_sys, SV = 0.9, 0.3, 70.0
    n_cyc = 4
    t_max = n_cyc * T_cyc

    def Q(t):
        tt = t % T_cyc
        if tt < t_sys:
            return (np.pi * SV / (2 * t_sys)) * np.sin(np.pi * tt / t_sys)
        return 0.0

    def winds(t, P, R, Cw):
        return (Q(t) - P / R) / Cw

    t_eval = np.linspace(0, t_max, 2000)

    # Normotensive
    sol_n = solve_ivp(winds, [0, t_max], [80.0], args=(1.3, 1.2),
                      t_eval=t_eval, max_step=0.005)
    P_n = sol_n.y[0]

    # Hypertensive (↑R, ↓C)
    sol_h = solve_ivp(winds, [0, t_max], [110.0], args=(1.7, 0.7),
                      t_eval=t_eval, max_step=0.005)
    P_h = sol_h.y[0]

    y_max = 210.0

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(t_max + 0.4, 0), xytext=(-0.2, 0), arrowprops=seta)
    ax.annotate("", xy=(-0.2, y_max), xytext=(-0.2, -10), arrowprops=seta)

    # curves
    ax.plot(t_eval, P_n, color=ACCENT, lw=2.6, zorder=3,
            label="normotensive  (normal $R$, $C$)")
    ax.plot(t_eval, P_h, color=NAVY, lw=2.4, ls=(0, (6, 3)), zorder=3,
            label="hypertensive  ($\\uparrow R$, $\\downarrow C$)")

    # systole markers
    for i in range(n_cyc):
        ts = i * T_cyc + t_sys / 2
        ax.plot([i * T_cyc, i * T_cyc], [-8, -2], color=NAVY, lw=1.4,
                zorder=3)
    ax.text(t_max / 2, -16, "successive cardiac cycles",
            ha="center", va="top", fontsize=10, color=SOFT)

    # axis labels
    ax.text(t_max + 0.4, -5, "time (s)", ha="right", va="top",
            fontsize=10.5, color=NAVY)
    ax.text(-0.3, y_max, "$P(t)$  (mmHg)", ha="right", va="top",
            fontsize=11, color=NAVY)

    # 80 and 120 ticks on the y axis (left)
    for y in (80, 120):
        ax.plot([-0.32, -0.2], [y, y], color=NAVY, lw=1.2)
        ax.text(-0.42, y, f"{y}", ha="right", va="center",
                fontsize=9, color=SOFT)

    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.set_xlim(-1.1, t_max + 1.0)
    ax.set_ylim(-22, y_max + 5)
    ax.axis("off")
    salvar(fig, "fig-13-windkessel")


# ==========================================================================
# Chapter 14 — Renal, metabolic and endocrine systems
# ==========================================================================
def fig14():
    """OGTT: glucose and insulin in a normal individual × type 2 diabetes."""
    from scipy.interpolate import CubicSpline
    fig, (axG, axI) = plt.subplots(2, 1, figsize=(9.4, 7.0))

    t_pts = np.array([0, 15, 30, 60, 90, 120, 150, 180])
    G_n = np.array([5.0, 6.5, 7.3, 7.0, 6.0, 5.5, 5.1, 5.0])
    G_d = np.array([8.0, 10.5, 12.5, 13.5, 13.0, 12.0, 11.0, 10.0])
    I_n = np.array([5.0, 35.0, 55.0, 55.0, 35.0, 20.0, 12.0, 8.0])
    I_d = np.array([10.0, 14.0, 20.0, 28.0, 34.0, 33.0, 28.0, 22.0])

    t = np.linspace(0, 180, 500)
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)

    # --- glucose panel ---
    axG.annotate("", xy=(198, 0), xytext=(-5, 0), arrowprops=seta)
    axG.annotate("", xy=(-5, 17.5), xytext=(-5, -1), arrowprops=seta)

    axG.plot([0, 198], [11.1, 11.1], color=SOFT, lw=0.9, ls=(0, (3, 3)),
             zorder=1)
    axG.text(198, 11.5, "11.1 mmol/L  (2-h diabetes threshold)",
             ha="right", va="bottom", fontsize=8.5, color=SOFT)

    cs_Gn = CubicSpline(t_pts, G_n)
    cs_Gd = CubicSpline(t_pts, G_d)
    axG.plot(t, cs_Gn(t), color=ACCENT, lw=2.6, zorder=3, label="normal")
    axG.plot(t, cs_Gd(t), color=NAVY, lw=2.4, ls=(0, (6, 3)), zorder=3,
             label="type 2 diabetes")
    axG.plot(t_pts, G_n, "o", color=ACCENT, ms=5, zorder=4)
    axG.plot(t_pts, G_d, "o", color=NAVY, ms=5, zorder=4)

    axG.text(198, -0.7, "time (min)", ha="right", va="top", fontsize=10,
             color=NAVY)
    axG.text(2, 17.5, "glucose (mmol/L)", ha="left", va="top",
             fontsize=10, color=NAVY)
    axG.legend(loc="upper right", bbox_to_anchor=(0.96, 0.95),
               frameon=False, fontsize=10)
    axG.set_xlim(-25, 222)
    axG.set_ylim(-2.5, 18.5)
    axG.axis("off")

    # --- insulin panel ---
    axI.annotate("", xy=(198, 0), xytext=(-5, 0), arrowprops=seta)
    axI.annotate("", xy=(-5, 75), xytext=(-5, -3), arrowprops=seta)

    cs_In = CubicSpline(t_pts, I_n)
    cs_Id = CubicSpline(t_pts, I_d)
    axI.plot(t, cs_In(t), color=ACCENT, lw=2.6, zorder=3)
    axI.plot(t, cs_Id(t), color=NAVY, lw=2.4, ls=(0, (6, 3)), zorder=3)
    axI.plot(t_pts, I_n, "o", color=ACCENT, ms=5, zorder=4)
    axI.plot(t_pts, I_d, "o", color=NAVY, ms=5, zorder=4)

    axI.text(198, -3.0, "time (min)", ha="right", va="top", fontsize=10,
             color=NAVY)
    axI.text(2, 75, "insulin ($\\mu$U/mL)", ha="left", va="top",
             fontsize=10, color=NAVY)
    axI.set_xlim(-25, 222)
    axI.set_ylim(-10, 80)
    axI.axis("off")

    fig.tight_layout(pad=1.5)
    salvar(fig, "fig-14-glicose-insulina")


# ==========================================================================
# Chapter 15 — Neurophysiology, immunology and infection
# ==========================================================================
def fig15():
    """FitzHugh-Nagumo: subthreshold × suprathreshold stimulus."""
    from scipy.integrate import solve_ivp
    fig, ax = plt.subplots(figsize=(9.8, 5.4))

    a_, b_, eps_ = 0.7, 0.8, 0.08

    def I_pulse(t, amp, t0=5.0, dur=1.0):
        return amp if t0 <= t <= t0 + dur else 0.0

    def fn(t, y, amp):
        v, w = y
        return [v - v ** 3 / 3 - w + I_pulse(t, amp),
                eps_ * (v + a_ - b_ * w)]

    v_rest, w_rest = -1.1994, -0.6243
    t_eval = np.linspace(0, 50, 2000)

    sol_sub = solve_ivp(fn, [0, 50], [v_rest, w_rest], args=(0.6,),
                        t_eval=t_eval, max_step=0.05)
    sol_sup = solve_ivp(fn, [0, 50], [v_rest, w_rest], args=(1.2,),
                        t_eval=t_eval, max_step=0.05)

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(53, v_rest), xytext=(-2.5, v_rest),
                arrowprops=seta)
    ax.annotate("", xy=(-2.5, 2.6), xytext=(-2.5, -2.6), arrowprops=seta)

    # resting line
    ax.plot([0, 53], [v_rest, v_rest], color=SOFT, lw=0.8,
            ls=(0, (2, 3)), zorder=1)
    ax.text(53, v_rest - 0.18, "resting potential",
            ha="right", va="top", fontsize=9, color=SOFT)

    # curves
    ax.plot(t_eval, sol_sub.y[0], color=ACCENT, lw=2.4, ls=(0, (6, 3)),
            zorder=3, label="subthreshold stimulus")
    ax.plot(t_eval, sol_sup.y[0], color=NAVY, lw=2.6, zorder=3,
            label="suprathreshold stimulus (fires an AP)")

    # stimulus marker
    ax.plot([5.0, 6.0], [-2.0, -2.0], color=NAVY, lw=3.0, zorder=3)
    ax.annotate("stimulus (1 s)", xy=(5.5, -2.0), xytext=(13.0, -2.4),
                arrowprops=dict(arrowstyle="->", color=SOFT, lw=1.0),
                fontsize=9, color=NAVY)

    # axis labels
    ax.text(53, -2.85, "time", ha="right", va="top", fontsize=10.5,
            color=NAVY)
    ax.text(-2.0, 2.6, "$v(t)$  (membrane potential)", ha="left",
            va="top", fontsize=10, color=NAVY)

    ax.legend(loc="upper right", bbox_to_anchor=(0.98, 0.95),
              frameon=False, fontsize=10)
    ax.set_xlim(-6, 56)
    ax.set_ylim(-3.2, 3.0)
    ax.axis("off")
    salvar(fig, "fig-15-potencial-acao")


# ==========================================================================
# Chapter 16 — Cancer, targeted therapies and radiotherapy
# ==========================================================================
def fig16():
    """Linear-quadratic model: tumor (α/β=10) × late-responding tissue (α/β=3)."""
    fig, ax = plt.subplots(figsize=(9.4, 5.4))

    d = np.linspace(0, 10, 600)
    a_t, b_t = 0.30, 0.030      # tumor / acute: α/β = 10 Gy
    a_n, b_n = 0.15, 0.050      # late:           α/β = 3 Gy
    S_t = np.exp(-a_t * d - b_t * d ** 2)
    S_n = np.exp(-a_n * d - b_n * d ** 2)

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(11.5, 0), xytext=(-0.3, 0), arrowprops=seta)
    ax.annotate("", xy=(-0.3, 1.22), xytext=(-0.3, -0.05), arrowprops=seta)

    # line S = 1
    ax.plot([0, 11.5], [1.0, 1.0], color=SOFT, lw=0.8, ls=(0, (2, 3)),
            zorder=1)
    ax.text(-0.45, 1.0, "1.0", ha="right", va="center",
            fontsize=9, color=SOFT)

    # curves
    ax.plot(d, S_t, color=ACCENT, lw=2.8, zorder=3,
            label="tumor / acute  ($\\alpha/\\beta = 10$ Gy)")
    ax.plot(d, S_n, color=NAVY, lw=2.4, ls=(0, (6, 3)), zorder=3,
            label="late-responding tissue  ($\\alpha/\\beta = 3$ Gy)")

    # conventional 2 Gy
    S_t_2 = float(np.exp(-a_t * 2 - b_t * 4))
    S_n_2 = float(np.exp(-a_n * 2 - b_n * 4))
    ax.plot([2, 2], [0, max(S_t_2, S_n_2)], color=SOFT, lw=0.7,
            ls=(0, (2, 3)), zorder=2)
    ax.plot([2], [S_t_2], "o", color=ACCENT, ms=6, zorder=5)
    ax.plot([2], [S_n_2], "o", color=NAVY, ms=6, zorder=5)
    ax.text(2, -0.08, "2 Gy\n(conventional)", ha="center", va="top",
            fontsize=9, color=NAVY)

    # axis labels
    ax.text(11.5, -0.06, "dose per fraction  $d$ (Gy)", ha="right",
            va="top", fontsize=10.5, color=NAVY)
    ax.text(0.2, 1.22, "surviving fraction  $S(d)$", ha="left",
            va="top", fontsize=10, color=NAVY)

    ax.legend(loc="upper right", bbox_to_anchor=(0.98, 0.86),
              frameon=False, fontsize=10)
    ax.set_xlim(-1.7, 12.8)
    ax.set_ylim(-0.22, 1.35)
    ax.axis("off")
    salvar(fig, "fig-16-linear-quadratico")


# ==========================================================================
# Chapter 17 — Bioimaging and clinical data
# ==========================================================================
def fig17():
    """Filtering a noisy image: phantom, noise, Gaussian."""
    from scipy.ndimage import gaussian_filter
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.7))

    nx, ny = 160, 160
    x = np.linspace(-1, 1, nx)
    y = np.linspace(-1, 1, ny)
    X, Y = np.meshgrid(x, y)

    # elliptical body
    phantom = ((X / 0.78) ** 2 + (Y / 0.92) ** 2 < 1).astype(float) * 0.45
    # tumor (denser)
    phantom += (((X - 0.22) ** 2 + (Y - 0.10) ** 2) < 0.040).astype(float) * 0.40
    # ventricle (less dense)
    phantom -= (((X + 0.30) ** 2 + (Y + 0.20) ** 2) < 0.030).astype(float) * 0.30

    # Gaussian noise
    rng = np.random.default_rng(42)
    ruido = phantom + rng.normal(0, 0.10, phantom.shape)

    # Gaussian filtering
    filtrado = gaussian_filter(ruido, sigma=1.5)

    titulos = ["original phantom", "with noise",
               "Gaussian filtering  ($\\sigma = 1.5$)"]
    imagens = [phantom, ruido, filtrado]

    for ax, img, tit in zip(axes, imagens, titulos):
        ax.imshow(img, cmap="gray", vmin=-0.15, vmax=0.95,
                  origin="lower", extent=(-1, 1, -1, 1))
        ax.set_title(tit, fontsize=10.5, color=NAVY, pad=8)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(SOFT)
            spine.set_linewidth(0.8)

    fig.tight_layout(pad=0.8)
    salvar(fig, "fig-17-bioimagem")


# ==========================================================================
# Chapter 18 — Integrated cases in quantitative medicine
# ==========================================================================
def fig18():
    """Intensified diabetes treatment: 24 h, no treatment → metformin → +GLP-1."""
    from scipy.interpolate import PchipInterpolator
    fig, ax = plt.subplots(figsize=(9.8, 5.4))

    t_key = np.array(
        [0.0, 3.0, 6.0, 7.0, 8.5, 10.5, 12.0, 13.5, 16.5, 19.0, 20.5,
         23.0, 24.0])
    G_u = np.array(
        [11.0, 10.8, 10.5, 10.5, 14.5, 11.5, 11.0, 14.0, 11.0, 11.0,
         14.2, 11.5, 11.0])
    G_m = np.array(
        [8.0, 7.7, 7.5, 7.5, 11.5, 8.5, 8.0, 11.0, 8.0, 8.0, 11.0, 8.5,
         8.0])
    G_f = np.array(
        [6.0, 5.7, 5.5, 5.5, 8.5, 6.5, 6.0, 8.0, 6.0, 6.0, 8.0, 6.2,
         6.0])

    cs_u = PchipInterpolator(t_key, G_u)
    cs_m = PchipInterpolator(t_key, G_m)
    cs_f = PchipInterpolator(t_key, G_f)

    t = np.linspace(0, 24, 600)

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(25.5, 0), xytext=(-0.7, 0), arrowprops=seta)
    ax.annotate("", xy=(-0.7, 18.0), xytext=(-0.7, -1.0), arrowprops=seta)

    # glycemic target range (4-10 mmol/L)
    ax.fill_between([0, 25], 4, 10, color=FILL, alpha=0.45, zorder=1)
    ax.text(0.5, 9.5, "target range  (4–10 mmol/L)", ha="left", va="top",
            fontsize=9, color=NAVY)

    # meal markers
    for tm, rotulo in [(7, "breakfast"), (12, "lunch"), (19, "dinner")]:
        ax.plot([tm], [-1.6], marker="v", color=NAVY, ms=8, zorder=3)
        ax.text(tm, -2.2, rotulo, ha="center", va="top", fontsize=8.5,
                color=SOFT)

    # curves
    ax.plot(t, cs_u(t), color=NAVY, lw=2.2, ls=(0, (2, 2)), zorder=3,
            label="without intensified treatment")
    ax.plot(t, cs_m(t), color=NAVY, lw=2.4, ls=(0, (6, 3)), zorder=3,
            label="+ metformin")
    ax.plot(t, cs_f(t), color=ACCENT, lw=2.8, zorder=4,
            label="+ metformin + GLP-1 agonist")

    # axis labels
    ax.text(25.5, -0.8, "time (h)", ha="right", va="top", fontsize=10.5,
            color=NAVY)
    ax.text(0.5, 18.0, "glucose (mmol/L)", ha="left", va="top",
            fontsize=10, color=NAVY)

    ax.legend(loc="upper right", bbox_to_anchor=(0.96, 0.99),
              frameon=False, fontsize=9.5)
    ax.set_xlim(-3, 30)
    ax.set_ylim(-3.5, 20)
    ax.axis("off")
    salvar(fig, "fig-18-diabetes-intensificacao")


# ==========================================================================
# Chapter 19 — Prototype of a physiological digital twin
# ==========================================================================
def fig19():
    """Digital twin: forecast of two scenarios with uncertainty bands."""
    from scipy.interpolate import PchipInterpolator
    fig, ax = plt.subplots(figsize=(9.6, 5.4))

    # past: serial HbA1c measurements
    rng = np.random.default_rng(7)
    t_past = np.array([-8.0, -6.0, -4.0, -2.0, 0.0])
    a1c_past_true = np.array([9.0, 9.1, 9.0, 9.2, 9.1])
    a1c_past = a1c_past_true + rng.normal(0, 0.15, 5)

    # future
    tf = np.linspace(0, 16, 240)
    # Scenario A: current regimen (oscillates around 9)
    a1c_A = 9.0 + 0.10 * np.sin(tf / 3.5)
    band_A = 0.40 * np.ones_like(tf)
    # Scenario B: intensification (asymptotic decline to 7)
    a1c_B = 9.0 + (7.0 - 9.0) * (1 - np.exp(-tf / 8.4))
    band_B = 0.55 * (1 - np.exp(-tf / 9.0)) + 0.15

    # axes
    seta = dict(arrowstyle="-|>", color=NAVY, lw=1.5, mutation_scale=14)
    ax.annotate("", xy=(17.5, 5), xytext=(-10, 5), arrowprops=seta)
    ax.annotate("", xy=(-10, 11.4), xytext=(-10, 4.7), arrowprops=seta)

    # target — label in the past, away from the scenario B curve
    ax.plot([-9, 17], [7.0, 7.0], color=SOFT, lw=0.8, ls=(0, (3, 3)),
            zorder=1)
    ax.text(-8.8, 7.15, "target  (7.0 %)", ha="left", va="bottom",
            fontsize=9, color=NAVY)

    # past/future divider
    ax.plot([0, 0], [5, 10.8], color=SOFT, lw=0.8, ls=(0, (2, 3)),
            zorder=1)
    ax.text(0, 10.95, "today", ha="center", va="bottom", fontsize=9,
            color=SOFT)

    # past/forecast labels
    ax.text(-4.5, 4.8, "past", ha="center", va="top", fontsize=9,
            color=SOFT)
    ax.text(8.0, 4.8, "forecast", ha="center", va="top", fontsize=9,
            color=SOFT)

    # scenario A — band + line
    ax.fill_between(tf, a1c_A - band_A, a1c_A + band_A, color=NAVY,
                    alpha=0.15, zorder=2)
    ax.plot(tf, a1c_A, color=NAVY, lw=2.2, ls=(0, (6, 3)), zorder=3,
            label="scenario A: current regimen  (median ± 90 %)")

    # scenario B — band + line
    ax.fill_between(tf, a1c_B - band_B, a1c_B + band_B, color=ACCENT,
                    alpha=0.22, zorder=2)
    ax.plot(tf, a1c_B, color=ACCENT, lw=2.6, zorder=4,
            label="scenario B: intensification  (median ± 90 %)")

    # past: fit and points
    cs_past = PchipInterpolator(t_past, a1c_past)
    t_pf = np.linspace(-8, 0, 80)
    ax.plot(t_pf, cs_past(t_pf), color=NAVY, lw=1.5, zorder=3)
    ax.plot(t_past, a1c_past, "o", color=NAVY, ms=7, zorder=5,
            label="past measurements")

    # axis labels
    ax.text(17.5, 4.85, "weeks from today", ha="right",
            va="top", fontsize=10, color=NAVY)
    ax.text(-9.7, 11.4, "HbA1c  (%)", ha="left", va="top", fontsize=10,
            color=NAVY)

    ax.legend(loc="upper right", bbox_to_anchor=(0.97, 0.95),
              frameon=False, fontsize=9.5)
    ax.set_xlim(-12.5, 19)
    ax.set_ylim(4.2, 11.8)
    ax.axis("off")
    salvar(fig, "fig-19-gemeo-digital")


# ==========================================================================
# Chapter 20 — Real-world data, interoperability and security
# ==========================================================================
def fig20():
    """Clinical data flow: sources → integration → models, under the LGPD."""
    fig, ax = plt.subplots(figsize=(10.0, 5.6))

    def caixa(cx, cy, w, h, texto, cor="white", fonte=10):
        ax.add_patch(FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0,rounding_size=0.12",
            facecolor=cor, edgecolor=SOFT, linewidth=1.3, zorder=3))
        ax.text(cx, cy, texto, ha="center", va="center", fontsize=fonte,
                color=NAVY, zorder=4)

    # sources (left)
    fontes = [
        (1.7, 5.5, "EHR"),
        (1.7, 4.0, "DICOM"),
        (1.7, 2.5, "laboratory"),
        (1.7, 1.0, "vital signs"),
    ]
    for cx, cy, t in fontes:
        caixa(cx, cy, 2.0, 0.9, t, fonte=10.5)

    # integration and anonymization (center)
    caixa(5.5, 4.2, 2.6, 1.2, "integration\n(HL7 / FHIR)", cor=FILL,
          fonte=10)
    caixa(5.5, 2.0, 2.6, 1.2, "anonymization /\npseudonymization",
          cor=FILL, fonte=10)

    # repository and models (right)
    caixa(9.0, 4.2, 2.6, 1.2, "centralized clinical\nrepository",
          fonte=10)
    caixa(9.0, 2.0, 2.6, 1.2, "models, dashboards,\ndecision support",
          fonte=10)

    # arrows from sources → integration
    seta = dict(arrowstyle="-|>", color=ACCENT, lw=1.7, mutation_scale=14)
    for cx, cy, _ in fontes:
        ax.annotate("", xy=(5.5 - 1.3, 4.2), xytext=(cx + 1.05, cy),
                    arrowprops=seta)

    # integration → anonymization
    ax.annotate("", xy=(5.5, 2.0 + 0.6), xytext=(5.5, 4.2 - 0.6),
                arrowprops=seta)

    # anonymization → repository
    ax.annotate("", xy=(9.0 - 1.3, 4.2), xytext=(5.5 + 1.3, 2.0),
                arrowprops=seta)

    # repository → models
    ax.annotate("", xy=(9.0, 2.0 + 0.6), xytext=(9.0, 4.2 - 0.6),
                arrowprops=seta)

    # LGPD base band
    ax.add_patch(FancyBboxPatch(
        (0.5, -0.4), 10.0, 0.95,
        boxstyle="round,pad=0,rounding_size=0.1",
        facecolor=FILL, edgecolor=SOFT, linewidth=1.2, zorder=2))
    ax.text(5.5, 0.05,
            "LGPD (Brazil's Law 13,709/2018) — sensitive health data — "
            "consent, purpose, security, audit",
            ha="center", va="center", fontsize=9.5, color=NAVY)

    ax.text(5.5, 6.7, "clinical data flow: from sources to decision "
            "support", ha="center", va="center", fontsize=10.5, color=SOFT)

    ax.set_xlim(0, 11)
    ax.set_ylim(-1.0, 7.2)
    ax.axis("off")
    salvar(fig, "fig-20-fluxo-dados")


# ==========================================================================
# Chapter 21 — Validation, regulation and clinical responsibility
# ==========================================================================
def fig21():
    """Discrimination is not calibration: ROC × calibration plot."""
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(9.8, 4.6))

    # --- Painel A: ROC ---
    fpr = np.linspace(0, 1, 250)
    tpr = 1 - (1 - fpr) ** (17 / 3)   # AUC = k/(k+1) = 0.85
    axA.plot([0, 1], [0, 1], color=SOFT, lw=0.9, ls=(0, (3, 3)),
             zorder=1)
    axA.fill_between(fpr, tpr, fpr, color=ACCENT, alpha=0.12, zorder=2)
    axA.plot(fpr, tpr, color=ACCENT, lw=2.8, zorder=3)
    axA.text(0.55, 0.18, "AUROC $\\approx 0.85$", ha="center",
             va="bottom", fontsize=11, color=NAVY)
    axA.set_xlim(-0.04, 1.04)
    axA.set_ylim(-0.04, 1.04)
    axA.set_xlabel("1 $-$ specificity", fontsize=10, color=NAVY)
    axA.set_ylabel("sensitivity", fontsize=10, color=NAVY)
    axA.set_title("discrimination (ROC) — looks good",
                  fontsize=10.5, color=NAVY, pad=8)

    # --- Panel B: calibration ---
    p_bin = np.array([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75,
                      0.85, 0.95])
    obs = np.array([0.08, 0.18, 0.27, 0.34, 0.42, 0.50, 0.57, 0.63,
                    0.68, 0.72])
    axB.plot([0, 1], [0, 1], color=SOFT, lw=0.9, ls=(0, (3, 3)),
             zorder=1, label="ideal calibration")
    axB.plot(p_bin, obs, "o-", color=NAVY, lw=2.0, ms=7, zorder=3,
             label="observed model")
    axB.set_xlim(0, 1)
    axB.set_ylim(0, 1)
    axB.set_xlabel("predicted probability", fontsize=10, color=NAVY)
    axB.set_ylabel("observed frequency", fontsize=10, color=NAVY)
    axB.set_title("calibration — systematically off",
                  fontsize=10.5, color=NAVY, pad=8)
    axB.legend(loc="upper left", frameon=False, fontsize=9.5)

    for ax in (axA, axB):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(NAVY)
        ax.spines["bottom"].set_color(NAVY)
        ax.tick_params(colors=NAVY, labelsize=9)
        ax.set_aspect("equal")

    fig.tight_layout(pad=1.2)
    salvar(fig, "fig-21-discriminacao-calibracao")


# ==========================================================================
# Chapter 22 — Usability, adoption and perspectives — closing of the series
# ==========================================================================
def fig22():
    """The four-volume series *The Principle of Action* in a single arc."""
    fig, ax = plt.subplots(figsize=(10.4, 5.8))

    volumes = [
        (2.0,  "Volume 1", "Mathematics:\nfrom logic to calculus",
         "language"),
        (4.8,  "Volume 2", "Physics:\nfrom the oscillator to Maxwell",
         "principle"),
        (7.6,  "Volume 3", "Medicine:\nmodel ⟷ evidence",
         "humility"),
        (10.4, "Volume 4", "Computational modeling:\nthe model that runs",
         "operation"),
    ]

    for cx, titulo, sub, papel in volumes:
        ax.add_patch(FancyBboxPatch(
            (cx - 1.25, 3.0), 2.5, 2.1,
            boxstyle="round,pad=0,rounding_size=0.15",
            facecolor="white", edgecolor=SOFT, linewidth=1.4, zorder=3))
        ax.text(cx, 4.78, titulo, ha="center", va="top", fontsize=11.5,
                color=NAVY)
        ax.text(cx, 4.25, sub, ha="center", va="top", fontsize=9.2,
                color=NAVY)
        ax.text(cx, 3.40, papel, ha="center", va="top", fontsize=9,
                color=SOFT, style="italic")

    # arrows between volumes
    seta = dict(arrowstyle="-|>", color=ACCENT, lw=2.0, mutation_scale=14)
    for cx1, cx2 in [(2.0, 4.8), (4.8, 7.6), (7.6, 10.4)]:
        ax.annotate("", xy=(cx2 - 1.3, 4.05), xytext=(cx1 + 1.3, 4.05),
                    arrowprops=seta)

    # Principle of Action band
    ax.add_patch(FancyBboxPatch(
        (0.6, 1.0), 11.2, 1.4,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor=FILL, edgecolor=SOFT, linewidth=1.3, zorder=2))
    ax.text(6.2, 1.85, "Principle of Action — the variational thread",
            ha="center", va="center", fontsize=12, color=NAVY)
    ax.text(6.2, 1.35,
            "from the stationary trajectory to the free-energy minimum, "
            "from Feynman's integral to the digital twin",
            ha="center", va="center", fontsize=9, color=SOFT,
            style="italic")

    # dashed lines linking the volumes to the band
    for cx, *_ in volumes:
        ax.plot([cx, cx], [3.0, 2.40], color=SOFT, lw=0.9,
                ls=(0, (2, 3)), zorder=1)

    ax.text(6.2, 5.55, "The Principle of Action — architecture of the four volumes",
            ha="center", va="center", fontsize=10.5, color=SOFT)

    ax.set_xlim(0.0, 12.4)
    ax.set_ylim(0.4, 5.9)
    ax.axis("off")
    salvar(fig, "fig-22-tetralogia")


FIGURAS = {"fig-01": fig01, "fig-02": fig02, "fig-03": fig03,
           "fig-04": fig04, "fig-05": fig05, "fig-06": fig06,
           "fig-07": fig07, "fig-08": fig08, "fig-09": fig09,
           "fig-10": fig10, "fig-11": fig11, "fig-12": fig12,
           "fig-13": fig13, "fig-14": fig14, "fig-15": fig15,
           "fig-16": fig16, "fig-17": fig17, "fig-18": fig18,
           "fig-19": fig19, "fig-20": fig20, "fig-21": fig21,
           "fig-22": fig22}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    alvos = sys.argv[1:]
    print("=== Computational generation of the Volume 4 figures (Matplotlib) ===")
    feitas = 0
    for chave, fn in FIGURAS.items():
        if alvos and not any(a.startswith(chave) for a in alvos):
            continue
        fn()
        feitas += 1
    print(f"\n{feitas} figure(s) generated with Matplotlib.")


if __name__ == "__main__":
    main()
