"""
Quick guide — NumPy: arrays, vectorization, indexing and reductions.

Appendix B: Quick Guide to Scientific Python — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def secao_criar_arrays() -> None:
    # Creating arrays
    a = np.array([1.0, 2.0, 3.0])             # 1D
    M = np.array([[1, 2], [3, 4]])             # 2D
    zeros = np.zeros((3, 4))                   # 3×4 of zeros
    ones = np.ones(10)                         # 1D of ones
    grade = np.linspace(0, 10, 100)            # 100 points between 0 and 10
    seq = np.arange(0, 10, 0.5)                # step 0.5
    print(a.shape, M.shape, zeros.shape, ones.shape, grade.shape, seq.shape)


def secao_operacoes_vetorizadas() -> None:
    # Vectorized operations
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x) + 0.5*np.cos(2*x)            # operation on the whole array
    norma = np.sqrt(x**2 + y**2)               # element-wise
    print(f"y[0]={y[0]:.4f}  norma[0]={norma[0]:.4f}")


def secao_indexacao() -> None:
    # Indexing and slicing
    a = np.array([1.0, 2.0, 3.0])
    M = np.array([[1, 2], [3, 4]])
    print(a[0], a[-1])                         # first, last
    print(M[0, :], M[:, 1])                    # row 0, column 1
    print(M[0:2, :])                           # first two rows
    mascara = a > 1.5
    a[mascara] = 0                             # conditional assignment
    print(a)


def secao_reducoes() -> None:
    # Reductions
    a = np.array([1.0, 2.0, 3.0, 4.0])
    M = np.array([[1.0, 2.0], [3.0, 4.0]])
    print(a.mean(), a.std(), a.sum())
    print(M.mean(axis=0))                      # mean of each column
    print(np.argmax(a), np.argmin(a))          # indices of max/min


def main() -> None:
    secao_criar_arrays()
    secao_operacoes_vetorizadas()
    secao_indexacao()
    secao_reducoes()


if __name__ == "__main__":
    main()
