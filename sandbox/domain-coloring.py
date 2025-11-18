"""
Source: 

  - Title:   Scientific Visualisation - Python & Matplotlib
  - Author:  Nicolas P. Rougier
  - URL:     https://github.com/rougier/scientific-visualization-book
  - License: BSD
"""

from numpy import *
import matplotlib.pyplot as plt

# from matplotlib.patheffects import Stroke, Normal


def normalize(Z):
    zmin, zmax = Z.min(), Z.max()
    return (Z - zmin) / (zmax - zmin)


T = linspace(-2.5, 2.5, 2048)
X, Y = meshgrid(T, T)
Z = X + 1j * Y
Z = Z + 1 / Z
A = normalize(angle(Z))
N = normalize(abs(Z)) * 2 * pi * 200


fig = plt.figure(figsize=(8, 8))
e = 0.001
ax = fig.add_axes([e, e, 1 - 2 * e, 1 - 2 * e], frameon=True, facecolor="black")

ax.imshow(
    A,
    interpolation="bicubic",
    cmap="Spectral",
    rasterized=True,
    alpha=1 - (N < 1.5 * pi) * 0.25 * abs(cos(N % (pi / 2))) ** 2,
)
ax.contour(abs(Z.real - round(Z.real)), 1, colors="black", linewidths=0.25)
ax.contour(abs(Z.imag - round(Z.imag)), 1, colors="black", linewidths=0.25)


ax.set_xticks([])
ax.set_yticks([])
