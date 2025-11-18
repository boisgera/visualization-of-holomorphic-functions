import marimo

__generated_with = "0.17.8"
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
    ## Level sets with `contour`

    Documentation: <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html>
    """)
    return


@app.function
def f(x, y):
    return x ** 2 + 2.0 * x * y + 3.0 * y ** 2


@app.cell(hide_code=True)
def _(mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        plt.contour(X, Y, Z)
        plt.grid(True)
        return mo.center(fig)
    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By default each color represents a different value of the level set. The correspondance can be made explicit with a colorbar.
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        plt.contour(X, Y, Z)
        plt.colorbar()
        plt.grid(True)
        return mo.center(fig)
    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Alternatively, numeric labels can be used.
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        labels = plt.contour(X, Y, Z, colors="black")
        plt.gca().clabel(labels)
        plt.grid(True)
        return mo.center(fig)

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can select the levels of the contour curves manually if you want to display for example all the level curves with an integer value, but it's not obvious to specify this parameter if you don't know the range of the function in the domain beforehand.
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        labels = plt.contour(
            X,
            Y,
            Z,
            levels=range(6), # ⚠️ Here 11 is good enough for example.
            colors="black",
        )
        plt.gca().clabel(labels)
        plt.grid(True)
        return mo.center(fig)

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To solve this (if you don't need the numeric labels), draw the contour line of level 0 of `np.sin(np.pi * Z)` instead!
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)
        W = np.sin(np.pi * Z)
        fig = plt.figure()
        plt.contour(
            X,
            Y,
            W,
            levels=[0],
            colors="black",
        )
        plt.grid(True)
        return mo.center(fig)


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When it's appropriate, using a logarithmic scale for values can often be more informative (and visually pleasing!).
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)
        W = np.sin(np.pi * np.log(Z))
        fig = plt.figure()
        plt.contour(
            X,
            Y,
            W,
            levels=[0],
            colors="black",
        )
        plt.grid(True)
        return mo.center(fig)


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Value images with `imshow`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead of level sets, we can associate at each point the value of the function with a point on a given color scale, or **color maps**.
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        plt.imshow(Z, extent=[-2, 2, -1, 1])
        plt.colorbar()
        return mo.center(fig)

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The default colormap is `viridis`.
    """)
    return


@app.cell
def _(colormaps):
    colormaps["viridis"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Explore other colormaps if the default doesn't match your need!

    See <https://matplotlib.org/stable/users/explain/colors/colormaps.html>.
    """)
    return


@app.cell(hide_code=True)
def _(colormaps, mo, np, plt):
    def _():
        x = np.linspace(-2, 2, 1000)
        y = np.linspace(-1, 1, 1000)
        [X, Y] = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        plt.imshow(Z, extent=[-2, 2, -1, 1], cmap=colormaps["jet"])
        plt.colorbar()
        return mo.center(fig)

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Complex-valued functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Drawing the level sets of the real part (in blue) and the imaginary part (in red) of a function can result in pretty curves, but unfortunately it's not very informative.
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    def _(
        f = lambda z: z,
        domain=[-2, 2, -1.5, 1.5],
        width=8.0,
        n=2048,
        title=None,
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
            np.sin(np.pi * W.real),
            levels=[0.0],
            colors="blue",
            linewidths=1.0,
        )
        plt.contour(
            X,
            Y,
            np.sin(np.pi * W.imag),
            levels=[0.0],
            colors="red",
            linewidths=1.0,
        )
        if title:
            plt.title(title)
        plt.axis("equal")
        plt.grid(True)
        return plt.gcf()

    #_()
    #_(lambda z: (z - 1) ** 2 / (z + 1))
    _(lambda z: 0.5 * (z + 1 / z))
    #_(lambda z: np.sin(1 / z))
    return


@app.cell(hide_code=True)
def _(np, plt):
    def _(
        f=lambda z: z,
        domain=[-2, 2, -1.5, 1.5],
        width=8.0,
        n=1024,
        An=2, # this need to be even
        title=None,
    ):
        xmin, xmax, ymin, ymax = domain
        X, Y = np.meshgrid(
            np.linspace(xmin, xmax, n),
            np.linspace(ymin, ymax, n),
        )
        wh_ratio = (xmax - xmin) / (ymax - ymin)
        Z = X + 1j * Y
        W = f(Z)
        L = np.log2(np.abs(W))
        A = np.angle(W) / (2 * np.pi) * An

        plt.figure(figsize=(width, width / wh_ratio))
        plt.contour(
            X,
            Y,
            np.sin(np.pi * L),
            levels=[0.0],
            colors="black",
            linewidths=0.75,
        )
        plt.contour(
            X,
            Y,
            np.sin(np.pi * A),
            levels=[0.0],
            linestyles="dotted",
            colors="black",
            linewidths=0.75,
        )
        if title:
            plt.title(title)
        plt.axis("equal")
        return plt.gcf()

    #_(An=16)
    #_(lambda z: (z - 1) ** 2 / (z + 1), An=16)
    _(lambda z: 0.5 * (z + 1 / z), An=16)
    #_(lambda z: np.sin(1 / z), An=16)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can use some hybrid representation where contours are used for argument but color maps are used for the modulus.
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    def _(
        f=lambda z: z,
        domain=[-2, 2, -1.5, 1.5],
        vmin=-2,
        vmax=+2,
        width=8.0,
        n=2048,
        An=4,
        title=None,
    ):
        xmin, xmax, ymin, ymax = domain
        w = xmax - xmin
        h = ymax - ymin
        eps = 0.1
        x_xmin = xmin - w * eps/2
        x_xmax = xmax + w * eps/2
        x_ymin = ymin - h * eps/2
        x_ymax = ymax + h * eps/2
        x_domain = x_xmin, x_xmax, x_ymin, x_ymax
        X, Y = np.meshgrid(
            np.linspace(x_xmin, x_xmax, n),
            np.linspace(x_ymin, x_ymax, n),
        )

        Z = X + 1j * Y
        W = f(Z)
        L = np.log2(np.abs(W))
        A = np.angle(W) / (2 * np.pi) * An 

        wh_ratio = (xmax - xmin) / (ymax - ymin)
        plt.figure(figsize=(width, width / wh_ratio))
        ax = plt.gca()
        ax.set_facecolor("white")
        im = ax.imshow(
            L,
            extent=domain,
            interpolation="nearest",
            cmap="hot",
            rasterized=True,
            alpha=0.9,
            vmin=vmin,
            vmax=vmax,
        )
        plt.contour(
            X,
            Y,
            np.sin(np.pi * A),
            levels=[0.0],
            colors="black",
            linestyles="dotted",
            linewidths=0.5,
        )
        if title:
            plt.title(title)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        ax.set_aspect("equal", adjustable="box")
        return plt.gcf()

    #_(lambda z: z)
    #_(lambda z: (z - 1) ** 2 / (z + 1), An=16)
    _(lambda z: 0.5 * (z + 1 / z), An=16)
    #_(lambda z: np.sin(1 / z), An=16)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That's however rarely what is done since the resulting color images tend to be quite "flat" are there is a more informative representations. Instead we are going to use contours for the modulus and the colormap for the argument. The thing that needs to be adjusted is that we'd better select a cyclic colormap to avoid a visual discontinuity around $-\pi$. For example, we can pick `twilight` or even better, `twilight_shifted`.
    """)
    return


@app.cell
def _(colormaps):
    colormaps["twilight"]
    return


@app.cell
def _(colormaps):
    colormaps["twilight_shifted"]
    return


@app.cell(hide_code=True)
def _(np, plt):
    def _(
        f=lambda z: z,
        domain=[-2, 2, -1.5, 1.5],
        width=8.0,
        n=2048,
        title=None,
    ):
        xmin, xmax, ymin, ymax = domain
        w = xmax - xmin
        h = ymax - ymin
        eps = 0.1
        x_xmin = xmin - w * eps/2
        x_xmax = xmax + w * eps/2
        x_ymin = ymin - h * eps/2
        x_ymax = ymax + h * eps/2
        x_domain = x_xmin, x_xmax, x_ymin, x_ymax
        X, Y = np.meshgrid(
            np.linspace(x_xmin, x_xmax, n),
            np.linspace(x_ymin, x_ymax, n),
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
            extent=x_domain,
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
            np.sin(np.pi * L),
            levels=[0.0],
            colors="black",
            linewidths=0.5,
        )
        if title:
            plt.title(title)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        ax.set_aspect("equal", adjustable="box")
        return plt.gcf()

    #_(lambda z: z)
    #_(lambda z: (z - 1) ** 2 / (z + 1))
    _(lambda z: 0.5 * (z + 1 / z))
    #_(lambda z: np.sin(1 /z))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course you can also keep the argument contour lines if you want to!
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    def _(
        f=lambda z: z,
        domain=[-2, 2, -1.5, 1.5],
        width=8.0,
        n=2048,
        An=4,
        title=None,
    ):
        xmin, xmax, ymin, ymax = domain
        w = xmax - xmin
        h = ymax - ymin
        eps = 0.1
        x_xmin = xmin - w * eps/2
        x_xmax = xmax + w * eps/2
        x_ymin = ymin - h * eps/2
        x_ymax = ymax + h * eps/2
        x_domain = x_xmin, x_xmax, x_ymin, x_ymax
        X, Y = np.meshgrid(
            np.linspace(x_xmin, x_xmax, n),
            np.linspace(x_ymin, x_ymax, n),
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
            extent=x_domain,
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
            np.sin(np.pi * A * An),
            linestyles="dotted",
            levels=[0.0],
            colors="black",
            linewidths=0.5,
        )
        plt.contour(
            X,
            Y,
            np.sin(np.pi * L),
            levels=[0.0],
            colors="black",
            linewidths=0.5,
        )
        if title:
            plt.title(title)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        ax.set_aspect("equal", adjustable="box")
        return plt.gcf()

    #_(lambda z: z, An=16)
    #_(lambda z: (z - 1) ** 2 / (z + 1), An=16)
    _(lambda z: 0.5 * (z + 1 / z), An=16)
    #_(lambda z: np.sin(1 /z), An=16)
    return


if __name__ == "__main__":
    app.run()
