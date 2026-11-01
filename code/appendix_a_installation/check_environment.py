"""
check_environment.py — checks the installation of the volume's scientific packages.

The single source of truth for the list of dependencies is the
`requirements.txt` file at the root of the repository. This script reads that
file, extracts the names (ignoring comments, blank lines and version
specifiers) and tries to import each package, reporting the installed
version or a warning when the package is missing.

Appendix A: Installing and Configuring the Environment — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path


# Mapping: name in requirements -> Python import name (when they differ).
NOME_IMPORT: dict[str, str] = {
    "scikit-learn": "sklearn",
    "scikit-image": "skimage",
    "pyyaml": "yaml",
    "Pillow": "PIL",
    "ipykernel": "ipykernel",
    "jupyter": "jupyter_core",  # umbrella package; 'jupyter_core' is more reliable to import
}

# Optional packages — absence produces a warning, not an error.
OPCIONAIS: set[str] = {"jupyter", "ipykernel"}


def localizar_requirements() -> Path:
    """Walks up the directories from the script until it finds requirements.txt."""
    atual = Path(__file__).resolve().parent
    for candidato in [atual, *atual.parents]:
        alvo = candidato / "requirements.txt"
        if alvo.is_file():
            return alvo
    raise FileNotFoundError("requirements.txt not found starting from "
                            f"{Path(__file__).resolve()}")


def ler_pacotes(requirements: Path) -> list[str]:
    """Extracts only the package names (without version) from requirements.txt."""
    pacotes: list[str] = []
    for linha in requirements.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        # split at any version comparator (>=, ==, >, <, ~=, !=)
        nome = re.split(r"[<>=!~\s]", linha, maxsplit=1)[0].strip()
        if nome:
            pacotes.append(nome)
    return pacotes


def versao_de(modulo) -> str:
    """Tries to extract the version of an imported module."""
    for atributo in ("__version__", "VERSION", "version"):
        if hasattr(modulo, atributo):
            valor = getattr(modulo, atributo)
            if callable(valor):
                try:
                    valor = valor()
                except Exception:
                    continue
            return str(valor)
    return "(unknown version)"


def main() -> None:
    print(f"Python       {sys.version.split()[0]}")
    print(f"{'-' * 40}")

    requirements = localizar_requirements()
    pacotes = ler_pacotes(requirements)

    faltando_obrigatorios: list[str] = []
    for pacote in pacotes:
        nome_import = NOME_IMPORT.get(pacote, pacote.replace("-", "_"))
        try:
            modulo = importlib.import_module(nome_import)
        except ImportError as erro:
            etiqueta = "OPTIONAL" if pacote in OPCIONAIS else "MISSING"
            print(f"[{etiqueta}] {pacote:<14} ({erro})")
            if pacote not in OPCIONAIS:
                faltando_obrigatorios.append(pacote)
            continue
        print(f"{pacote:<14} {versao_de(modulo)}")

    # minimal functional test
    import numpy as np
    x = np.linspace(0, 1, 5)
    y = np.exp(-x)
    assert y.shape == (5,)

    print(f"{'-' * 40}")
    if faltando_obrigatorios:
        print("Missing required packages:", ", ".join(faltando_obrigatorios))
        print(f"Install with: pip install -r {requirements}")
        sys.exit(1)
    print("Environment ready.")


if __name__ == "__main__":
    main()
