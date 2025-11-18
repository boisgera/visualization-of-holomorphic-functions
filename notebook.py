import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Domain coloring
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import colormaps
    return colormaps, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Source:

      - Title:   Scientific Visualisation - Python & Matplotlib
      - Author:  Nicolas P. Rougier
      - URL:     https://github.com/rougier/scientific-visualization-book
      - License: BSD
    """)
    return


@app.function
def Joukowsky(z):
    return 0.5 * (z + 1.0 / z)


@app.cell
def _(np, plt):
    def _(
        f=Joukowsky,
        domain=[-2, 2, -1.5, 1.5],
        width=8.0,
        n=2048,
        title="Joukowsky transform",
    ):
        xmin, xmax, ymin, ymax = domain
        X, Y = np.meshgrid(
            np.linspace(xmin, xmax, 2048),
            np.linspace(ymin, ymax, 2048),
        )
        wh_ratio = (xmax - xmin) / (ymax - ymin)
        Z = X + 1j * Y
        W = f(Z)
        plt.figure(figsize=(width, width / wh_ratio))

        plt.contour(
            X,
            Y,
            W.real - np.round(W.real),
            levels=[0.0],
            colors="black",
            linewidths=0.5,
        )
        plt.contour(
            X,
            Y,
            W.imag - np.round(W.imag),
            levels=[0.0],
            colors="black",
            linestyles="dotted",
            linewidths=0.5,
        )
        if title:
            plt.title(title)
        plt.axis("equal")
        return plt.gcf()


    _()
    return


@app.cell
def _(np, plt):
    def _(
        f=Joukowsky,
        domain=[-2, 2, -1.5, 1.5],
        width=8.0,
        n=2048,
        title="Joukowsky transform",
    ):
        xmin, xmax, ymin, ymax = domain
        X, Y = np.meshgrid(
            np.linspace(xmin, xmax, 2048),
            np.linspace(ymin, ymax, 2048),
        )
        wh_ratio = (xmax - xmin) / (ymax - ymin)
        Z = X + 1j * Y
        W = f(Z)
        L = np.log2(np.abs(W))
        A = np.angle(W) / (2 * np.pi / 4)
    
        plt.figure(figsize=(width, width / wh_ratio))
        plt.contour(
            X,
            Y,
            L - np.round(L),
            levels=[0.0],
            colors="black",
            linewidths=0.5,
        )
        plt.contour(
            X,
            Y,
            A - np.round(A),
            levels=[0.0],
            linestyles="dotted",
            colors="black",
            linewidths=0.5,
        )
        if title:
            plt.title(title)
        plt.axis("equal")
        return plt.gcf()


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Colormaps
    """)
    return


@app.cell
def _(colormaps):
    colormaps["viridis"]
    return


@app.cell
def _(colormaps, np, plt):
    def show_colormap_RGB(colormap):
        if isinstance(colormap, str):
            colormap = colormaps[colormap]
        u = np.linspace(0.0, 1.0, 1024)
        RGBA = colormap(u)  # float64, but discretised (8-bit)
        RGB = RGBA[:, :3]
        fig = plt.figure(figsize=(8, 4.5))
        plt.plot(u, RGB[:, 0], color="red")
        plt.plot(u, RGB[:, 1], color="green")
        plt.plot(u, RGB[:, 2], color="blue")
        plt.grid(True)
        return fig

    show_colormap_RGB("viridis")
    return (show_colormap_RGB,)


@app.cell
def _(colormaps):
    colormaps["twilight"]
    return


@app.cell
def _(show_colormap_RGB):
    show_colormap_RGB("twilight")
    return


@app.cell
def _(colormaps):
    colormaps["twilight_shifted"]
    return


@app.cell
def _(show_colormap_RGB):
    show_colormap_RGB("twilight_shifted")
    return


@app.cell
def _(np, plt):
    def _(
        f=Joukowsky,
        domain=[-2, 2, -1.5, 1.5],
        width=8.0,
        n=2048,
        title="Joukowsky transform",
    ):
        xmin, xmax, ymin, ymax = domain
        X, Y = np.meshgrid(
            np.linspace(xmin, xmax, 2048),
            np.linspace(ymin, ymax, 2048),
        )
        wh_ratio = (xmax - xmin) / (ymax - ymin)
        Z = X + 1j * Y
        W = f(Z)
        L = np.log2(np.abs(W))
        A = np.angle(W) / (2 * np.pi)
    
        plt.figure(figsize=(width, width / wh_ratio))
        ax = plt.gca()
        ax.set_facecolor("white")
        im = ax.imshow(
            A,
            extent=domain,
            interpolation="nearest",
            cmap="twilight_shifted",
            rasterized=True,
            alpha=0.9,
            vmin = -0.5,
            vmax = +0.5,
        )
        plt.contour(
            X,
            Y,
            L - np.round(L),
            levels=[0.0],
            colors="black",
            linewidths=0.5,
        )
        if title:
            plt.title(title)
        plt.axis("equal")
        return plt.gcf()

    _()
    return


@app.cell
def _(np, plt):
    def _(
        f=Joukowsky,
        domain=[-2, 2, -1.5, 1.5],
        vmin=-2,
        vmax=+2,
        width=8.0,
        n=2048,
        title="Joukowsky transform",
    ):
        xmin, xmax, ymin, ymax = domain
        X, Y = np.meshgrid(
            np.linspace(xmin, xmax, 2048),
            np.linspace(ymin, ymax, 2048),
        )
        wh_ratio = (xmax - xmin) / (ymax - ymin)
        Z = X + 1j * Y
        W = f(Z)
        L = np.log2(np.abs(W))
        A = np.angle(W) / (2 * np.pi / 4) 
    
        plt.figure(figsize=(width, width / wh_ratio))
        ax = plt.gca()
        ax.set_facecolor("white")
        im = ax.imshow(
            L,
            extent=domain,
            interpolation="nearest",
            cmap="viridis",
            rasterized=True,
            alpha=0.9,
            vmin=vmin,
            vmax=vmax,
        )
        plt.contour(
            X,
            Y,
            A - np.round(A),
            levels=[0.0],
            colors="black",
            linewidths=0.5,
        )
        if title:
            plt.title(title)
        plt.axis("equal")
        return plt.gcf()

    _()
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi):
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = _Z
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _A,
        interpolation="nearest",
        cmap="twilight_shifted",
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi):
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = _Z**2
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _A,
        interpolation="nearest",
        cmap="twilight_shifted",
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi):
    # TODO:
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = 1 / (_Z - 1)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _A,
        interpolation="nearest",
        cmap="twilight_shifted",
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, savefig):
    # TODO:
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = (_Z + 1) ** 2 / (_Z - 1)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _A,
        interpolation="nearest",
        cmap="twilight_shifted",
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    savefig("image.png")
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi):
    # TODO:
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = 0.5 * (_Z + 1 / _Z)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _A,
        interpolation="nearest",
        cmap="twilight_shifted",
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi):
    # TODO:
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = 0.5 * (_Z + 1 / _Z)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _L,
        interpolation="nearest",
        cmap="hot",
        vmin=-3,
        vmax=3,
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(angle, exp, figure, gca, gcf, linspace, log2, meshgrid, pi):
    # TODO:
    _T = linspace(-0.1, 0.1, 4096)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = exp(1 / _Z)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _A,
        interpolation="nearest",
        cmap="twilight_shifted",
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5, alpha=0)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5, alpha=0)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, sin):
    # TODO:
    _T = linspace(-0.1, 0.1, 4096)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = sin(1 / _Z)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    figure(figsize=(16, 16))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(
        _A,
        interpolation="nearest",
        cmap="twilight_shifted",
        rasterized=True,
        alpha=1.0,
    )
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5, alpha=0)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5, alpha=0)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()  # "twilight", #"twilight", #"Spectral",
    return


@app.cell
def _(
    angle,
    clf,
    colorspacious,
    figure,
    gca,
    gcf,
    linspace,
    log2,
    meshgrid,
    ones_like,
    pi,
    shape,
    zeros,
):
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = (_Z - 1) ** 2 / (_Z + 1)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    J_3 = ones_like(_A, dtype=float)
    _C = ones_like(_A, dtype=float)
    _h = _A
    _JCh = zeros(shape(_A) + (3,))
    _JCh[:, :, 0] = 90.0 * J_3
    _JCh[:, :, 1] = 90.0 * _C
    _JCh[:, :, 2] = _h / pi * 180.0
    _RGB = colorspacious.cspace_convert(_JCh, "JCh", "sRGB1")
    clf()
    _ = figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(_RGB, interpolation="nearest", rasterized=True, alpha=1.0)
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.contour(_L - round(_L), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()
    return


@app.cell
def _(
    angle,
    clf,
    colorspacious,
    figure,
    gca,
    gcf,
    linspace,
    log2,
    meshgrid,
    ones_like,
    pi,
    shape,
    zeros,
):
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = _Z
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    J_4 = ones_like(_A, dtype=float)
    _C = abs(_W) / (1 + abs(_W))
    _h = _A
    _JCh = zeros(shape(_A) + (3,))
    _JCh[:, :, 0] = 90.0
    _JCh[:, :, 1] = 90.0
    _JCh[:, :, 2] = _h / pi * 180.0
    _RGB = colorspacious.cspace_convert(_JCh, "JCh", "sRGB1")
    clf()
    _ = figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(_RGB, interpolation="nearest", rasterized=True, alpha=1.0)
    _ax.contour(_An - round(_An), [0.0], colors="black", linewidths=0.5)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()
    return


@app.cell
def _(colormaps):
    cm = colormaps["twilight_shifted"]
    cm
    return (cm,)


@app.cell
def _(cm):
    cm([[[0.0], [0.5], [1.0]]])
    return


@app.cell
def _(
    angle,
    clf,
    cm,
    colorspacious,
    figure,
    gca,
    gcf,
    linspace,
    log2,
    meshgrid,
    pi,
    shape,
    zeros,
):
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = 0.5 * (_Z + 1 / _Z)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    _RGBA = cm(0.5 + 0.5 * _A / pi)
    _RGB = _RGBA[:, :, :3]
    _JCh = colorspacious.cspace_convert(_RGB, "sRGB1", "JCh")
    J_5 = _JCh[:, :, 0]
    _C = _JCh[:, :, 1]
    _h = _JCh[:, :, 2]
    _JCh = zeros(shape(_A) + (3,))
    _JCh[:, :, 0] = J_5 * abs(_W) / (1.0 + abs(_W))
    _JCh[:, :, 1] = _C
    _JCh[:, :, 2] = _h
    _RGB = colorspacious.cspace_convert(_JCh, "JCh", "sRGB1")
    clf()
    _ = figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(_RGB, interpolation="nearest", rasterized=True, alpha=1.0)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()
    return


@app.cell
def _(
    angle,
    clf,
    cm,
    colorspacious,
    figure,
    gca,
    gcf,
    linspace,
    log2,
    meshgrid,
    pi,
    shape,
    zeros,
):
    _T = linspace(-2.5, 2.5, 1024)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    _W = 0.5 * (_Z + 1 / _Z)
    _A = angle(_W)
    _N = 2
    _An = _A / 2 / pi * _N
    _L = log2(abs(_W))
    _RGBA = cm(0.5 + 0.5 * _A / pi)
    _RGB = _RGBA[:, :, :3]
    _JCh = colorspacious.cspace_convert(_RGB, "sRGB1", "JCh")
    J_6 = _JCh[:, :, 0]
    _C = _JCh[:, :, 1]
    _h = _JCh[:, :, 2]
    _JCh = zeros(shape(_A) + (3,))
    _JCh[:, :, 0] = J_6 * abs(_W) / (1.0 + abs(_W))
    _JCh[:, :, 1] = _C
    _JCh[:, :, 2] = _h
    _RGB = colorspacious.cspace_convert(_JCh, "JCh", "sRGB1")
    clf()
    _ = figure(figsize=(8, 8))
    _ax = gca()
    _ax.set_facecolor("white")
    _im = _ax.imshow(_RGB, interpolation="nearest", rasterized=True, alpha=1.0)
    _ax.set_xticks([])
    _ax.set_yticks([])
    gcf()
    return


if __name__ == "__main__":
    app.run()
