"""
Physical constants and conversion factors used throughout the volume.

Appendix C: Tables of Physical, Chemical and Physiological Parameters — Volume 4
of "The Principle of Action" (Nadson Brito Gondim).

Teaching-value notice: the parameters listed are typical values, chosen
so that the simulations of the volume produce recognizable and didactically
useful curves. They are not an individual recommendation of dose, of
management or of clinical modeling.

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


# C.1 — Physical Constants and Conversions
CONSTANTES_FISICAS: dict[str, dict[str, str | float]] = {
    "c":   {"nome": "speed of light in vacuum",       "valor": 2.998e8,  "unidade": "m/s"},
    "h":   {"nome": "Planck constant",                "valor": 6.626e-34, "unidade": "J.s"},
    "hbar":{"nome": "h / 2π",                          "valor": 1.055e-34, "unidade": "J.s"},
    "kB":  {"nome": "Boltzmann constant",             "valor": 1.381e-23, "unidade": "J/K"},
    "R":   {"nome": "gas constant",                   "valor": 8.314,     "unidade": "J/(mol.K)"},
    "NA":  {"nome": "Avogadro number",                "valor": 6.022e23,  "unidade": "/mol"},
    "G":   {"nome": "gravitational constant",         "valor": 6.674e-11, "unidade": "N.m^2/kg^2"},
    "eps0":{"nome": "vacuum permittivity",            "valor": 8.854e-12, "unidade": "F/m"},
    "e":   {"nome": "elementary charge",              "valor": 1.602e-19, "unidade": "C"},
}


def main() -> None:
    for simbolo, dados in CONSTANTES_FISICAS.items():
        print(f"{simbolo:5s} = {dados['valor']:.3e} {dados['unidade']}  ({dados['nome']})")


if __name__ == "__main__":
    main()
