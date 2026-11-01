"""Smoke test: runs every .py script in the code/ directory to make sure
there is no ModuleNotFoundError, SyntaxError or ImportError.

Scripts that depend on external data are marked as xfail.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CODIGO = ROOT / "code"

# Scripts that depend on external data (must not run in a plain CI)
SCRIPTS_XFAIL: set[str] = {
    "03_fhir_query.py",                # requires a FHIR endpoint
    "15_ch20_index_dicom_folder.py",   # requires an external DICOM folder
}

SCRIPTS = sorted(p for p in CODIGO.rglob("*.py") if p.is_file())


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: str(p.relative_to(ROOT)))
def test_script_roda(script: Path) -> None:
    if script.name in SCRIPTS_XFAIL:
        pytest.xfail("depends on external data")
    env = {
        # non-interactive backend for matplotlib
        "MPLBACKEND": "Agg",
        # UTF-8 output: the scripts print symbols (≈, π, Δ) and the default
        # Windows console (cp1252) cannot encode them
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8",
    }
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True, text=True, timeout=60,
        encoding="utf-8", errors="replace",   # the child writes UTF-8
        env={**__import__("os").environ, **env},
    )
    assert result.returncode == 0, (
        f"{script.relative_to(ROOT)} failed:\n"
        f"STDOUT: {result.stdout[-500:]}\n"
        f"STDERR: {result.stderr[-500:]}"
    )
