"""
Baseline state of the digital twin — assembling population priors.

Chapter 19: Prototype of a physiological digital twin — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


def cockcroft_gault(idade: float, peso_kg: float,
                    cr_serica: float, sexo: str) -> float:
    base = (140 - idade) * peso_kg / (72 * cr_serica)
    return base * (0.85 if sexo == 'F' else 1.0)


def calcular_SI_basal(hbA1c: float) -> float:
    """Simple heuristic: SI falls linearly with HbA1c above 5.5%."""
    return max(0.2, 1.0 - 0.15 * max(0.0, hbA1c - 5.5))


def estado_basal(idade: float, sexo: str, peso_kg: float,
                 cr_serica: float, hbA1c: float | None = None) -> dict:
    crcl = cockcroft_gault(idade, peso_kg, cr_serica, sexo)
    # population priors
    parametros = {
        'CL_renal':  crcl / 100.0,           # fraction of normal
        'V_dist':    0.6 * peso_kg,          # L (body water)
        'S_I':       calcular_SI_basal(hbA1c)
        if hbA1c else 1.0,
        # ... other priors
    }
    return parametros


def main() -> None:
    parametros = estado_basal(idade=62, sexo='F', peso_kg=72,
                              cr_serica=1.1, hbA1c=9.1)
    for chave, valor in parametros.items():
        print(f"  {chave} = {valor:.3f}")


if __name__ == "__main__":
    main()
