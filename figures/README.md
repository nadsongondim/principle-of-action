# Technical figures of Volume 4

This directory reproduces **all 22 technical figures** of *Volume 4 —
Unified Computational Modeling* of the series **The Principle of Action**.
The figures are entirely computational (Matplotlib) — each drawing is
described by version-controlled code, with no manual intervention.

## How to generate

From the root of the repository, with the dependencies in `requirements.txt`
installed:

```bash
# Generates all the figures of the volume
python figures/figures_volume4.py

# Generates only one or a few specific figures
python figures/figures_volume4.py fig-04
python figures/figures_volume4.py fig-04 fig-12 fig-17
```

The PNGs are saved by default to `figures/output/` (folder created
automatically; it is listed in `.gitignore`). The file names (slugs) are the
same as the image files of the book, which keep their original Portuguese
names.

## Figure map

| Slug | Chapter | Topic |
|---|---:|---|
| `fig-01-projeto-reproduzivel` | 1 | Anatomy of a reproducible simulation project |
| `fig-02-edo-euler` | 2 | ODE integration — explicit Euler |
| `fig-03-calibracao-validacao` | 3 | Calibration × cross-validation |
| `fig-04-oscilador-harmonico` | 4 | Harmonic oscillator — phase space |
| `fig-05-energia-simpletico` | 5 | Energy conservation in symplectic integrators |
| `fig-06-equacao-onda` | 6 | 1D wave equation — FDTD |
| `fig-07-oscilador-quantico` | 7 | Stationary states of the quantum oscillator |
| `fig-08-lennard-jones` | 8 | Lennard-Jones potential |
| `fig-09-perfil-reacao` | 9 | Reaction energy profile A → B → C |
| `fig-10-mm-hill` | 10 | Michaelis-Menten × Hill kinetics |
| `fig-11-dose-resposta` | 11 | Dose-response curves and antagonism |
| `fig-12-doses-repetidas` | 12 | Repeated-dose PK — steady state |
| `fig-13-windkessel` | 13 | Two-element Windkessel model |
| `fig-14-glicose-insulina` | 14 | Glucose-insulin dynamics (Bergman minimal model) |
| `fig-15-potencial-acao` | 15 | Action potential — FitzHugh-Nagumo |
| `fig-16-linear-quadratico` | 16 | Linear-quadratic model in radiotherapy |
| `fig-17-bioimagem` | 17 | Bioimage processing pipeline |
| `fig-18-diabetes-intensificacao` | 18 | Clinical case — intensification in diabetes |
| `fig-19-gemeo-digital` | 19 | Architecture of a patient digital twin |
| `fig-20-fluxo-dados` | 20 | FHIR flow / clinical interoperability |
| `fig-21-discriminacao-calibracao` | 21 | Discrimination × calibration of predictive models |
| `fig-22-tetralogia` | 22 | Map of the four-volume series |

## Visual identity

The series palette is coded at the top of `figures_volume4.py`:

```python
NAVY   = "#1b2a4a"   # text and outlines
ACCENT = "#2f6fdb"   # highlight
SOFT   = "#98a4ba"   # auxiliary elements
FILL   = "#dce6f5"   # fills
```

Typeface: DejaVu Sans (available by default in Matplotlib).
