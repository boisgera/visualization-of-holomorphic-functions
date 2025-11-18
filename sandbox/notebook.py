import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Visualization of analytic functions
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    TODO:
      - plots & contours
      - start 3D plots with real and imag, urk, not very useful.
      - vectorisation
      - tricks with integer (non-labelled) contours
      - exploration with real, imag. Use IFT & conformal transform to explain what we see (90° angles) ?
      - then modulus, log-modulus, angle, etc.
    """)
    return


@app.cell
def _():
    import time
    return


@app.cell
def _():
    from numpy import (
        angle,
        clip,
        cos,
        exp,
        linspace,
        log,
        log2,
        logspace,
        meshgrid,
        ones_like,
        pi,
        round,
        shape,
        sqrt,
        sin,
        vectorize,
        zeros,
    )
    from matplotlib import colormaps
    from matplotlib.pyplot import (
        axis,
        clf,
        contour,
        figure,
        fill,
        gca,
        gcf,
        grid,
        plot,
        quiver,
        savefig,
        streamplot,
        subplots,
        subplots_adjust,
        xlim,
        ylim,
    )
    from matplotlib.animation import FuncAnimation, PillowWriter
    from IPython.display import Image
    import colorspacious
    return (
        FuncAnimation,
        PillowWriter,
        angle,
        axis,
        clf,
        clip,
        colormaps,
        colorspacious,
        contour,
        cos,
        exp,
        figure,
        fill,
        gca,
        gcf,
        grid,
        linspace,
        log,
        log2,
        logspace,
        meshgrid,
        ones_like,
        pi,
        plot,
        quiver,
        round,
        savefig,
        shape,
        sin,
        sqrt,
        streamplot,
        subplots,
        subplots_adjust,
        vectorize,
        xlim,
        ylim,
        zeros,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Paths & Winding Number
    """)
    return


@app.cell
def _(linspace, plot, vectorize):
    def path_concat(*paths):
        @vectorize
        def path(t):
            n = len(paths)
            _i = int(n * t)
            s = n * t - _i
            if s == 0.0 and _i > 0:
                _i, s = (_i - 1, 1.0)
            return paths[_i](s)

        return path


    def path_plot(path, n=1000, *args, **kwargs):
        t = linspace(0.0, 1.0, n)
        _path_t = path(t)
        plot(_path_t.real, _path_t.imag, *args, **kwargs)
    return path_concat, path_plot


@app.cell
def _(exp, pi):
    def circle(c=0j, r=1.0, arg0=0.0, arg1=2 * pi):
        def _gamma(t):
            return r * exp(1j * (arg0 + (arg1 - arg0) * t)) + c

        return _gamma


    def line(z0=0, z1=1):
        def _gamma(t):
            return (1 - t) * z0 + t * z1

        return _gamma
    return circle, line


@app.cell
def _(axis, circle, grid, line, path_concat, path_plot, pi):
    _path = path_concat(
        line(-1 - 1j, -1j),
        circle(arg0=-pi / 2, arg1=pi / 2),
        line(1j, 1j - 1),
    )
    path_plot(_path)
    axis("equal")
    grid(True)
    return


@app.cell
def _(linspace):
    def integral(f, path, n=1000):
        t = linspace(0.0, 1.0, n, endpoint=False)
        dt = 1.0 / n
        path_t = path(t)
        dpath_t = path(t + dt) - path(t)
        return sum(f(path(t)) * dpath_t)
    return (integral,)


@app.cell
def _(circle, integral, pi):
    def f(z):
        return 1.0 / z


    integral(f, circle()) / (2 * pi * 1j)
    return


@app.cell
def _(integral, pi, round):
    def arg_var(path, a=0.0, n=1000):
        def f(z):
            return 1.0 / (z - a)

        i = integral(f, path, n)
        return i.imag


    def winding_number(path, a=0.0, n=1000):  # Assumption: the path is closed
        w = arg_var(path, a, n)
        return int(round(w / (2 * pi)))
    return (winding_number,)


@app.cell
def _(circle, winding_number):
    winding_number(circle())
    return


@app.cell
def _(circle, pi, winding_number):
    winding_number(circle(arg1=6 * pi))
    return


@app.cell
def _(circle, winding_number):
    winding_number(circle(c=0.5))
    return


@app.cell
def _(circle, winding_number):
    winding_number(circle(c=-1.5))
    return


@app.cell
def _(axis, grid, line, linspace, path_concat, plot):
    square = path_concat(
        line(1 - 1j, 1 + 1j),
        line(1 + 1j, -1 + 1j),
        line(-1 + 1j, -1 - 1j),
        line(-1 - 1j, 1 - 1j),
    )

    t = linspace(0.0, 1.0, 1000)
    square_t = square(t)
    plot(square_t.real, square_t.imag)
    grid(True)
    axis("square")
    return (square,)


@app.cell
def _(square, winding_number):
    winding_number(square)
    return


@app.cell
def _(path_concat, square, winding_number):
    winding_number(path_concat(square, square))
    return


@app.cell
def _(square, winding_number):
    winding_number(lambda t: square(1.0 - t))
    return


@app.cell
def _(square, winding_number):
    winding_number(square, a=0.95 + 0.95j)
    return


@app.cell
def _(square, winding_number):
    winding_number(square, a=1.05 + 0.95j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conformal Mappings
    """)
    return


@app.cell
def _(circle, exp, line):
    def grid_1(xs, ys):
        paths = []
        x_min, x_max = (xs[0], xs[-1])
        y_min, y_max = (ys[0], ys[-1])
        for x in xs:
            paths.append(line(x + 1j * y_min, x + 1j * y_max))
        for y in ys:
            paths.append(line(x_min + 1j * y, x_max + 1j * y))
        return paths


    def polar_grid(rs, thetas, c=0.0 + 0j):
        paths = []
        r_min, r_max = (rs[0], rs[-1])
        theta_min, theta_max = (thetas[0], thetas[-1])
        for r in rs:
            paths.append(circle(r=r, arg0=theta_min, arg1=theta_max, c=c))
        for _theta in thetas:
            paths.append(
                line(r_min * exp(1j * _theta) + c, r_max * exp(1j * _theta) + c)
            )
        return paths
    return grid_1, polar_grid


@app.cell
def _(gcf, grid_1, linspace, subplots):
    def f_1(z):
        return 1 / (z + 2)


    paths = grid_1(xs=linspace(-1, 1, 11), ys=linspace(-1, 1, 11))
    t_1 = linspace(0.0, 1.0, 1000)
    _fig, (ax1, ax2) = subplots(1, 2, figsize=(8, 4.5))
    for _path in paths:
        _path_t = _path(t_1)
        _f_path_t = f_1(_path_t)
        ax1.plot(_path_t.real, _path_t.imag, color="C0")
        ax2.plot(_f_path_t.real, _f_path_t.imag, color="C1")
    ax1.axis("equal")
    ax2.axis("equal")
    gcf()
    return


@app.cell
def _(gcf, linspace, logspace, pi, polar_grid, subplots):
    def f_2(z):
        return 1 / (z + 2)


    paths_1 = polar_grid(
        rs=logspace(-10, 0, 11, base=2), thetas=linspace(0, 2 * pi, 11)
    )
    t_2 = linspace(0.0, 1.0, 1000)
    _fig, (ax1_1, ax2_1) = subplots(1, 2, figsize=(8, 4.5))
    for _path in paths_1:
        _path_t = _path(t_2)
        _f_path_t = f_2(_path_t)
        ax1_1.plot(_path_t.real, _path_t.imag, color="C0")
        ax2_1.plot(_f_path_t.real, _f_path_t.imag, color="C1")
    ax1_1.axis("equal")
    ax2_1.axis("equal")
    gcf()
    return


@app.cell
def _(exp, gcf, linspace, logspace, pi, polar_grid, subplots):
    def f_3(z):
        return exp(z)


    paths_2 = polar_grid(
        rs=logspace(-10, 0, 11, base=2), thetas=linspace(0, 2 * pi, 11)
    )
    t_3 = linspace(0.0, 1.0, 1000)
    _fig, (ax1_2, ax2_2) = subplots(1, 2, figsize=(8, 4.5))
    for _path in paths_2:
        _path_t = _path(t_3)
        _f_path_t = f_3(_path_t)
        ax1_2.plot(_path_t.real, _path_t.imag, color="C0")
        ax2_2.plot(_f_path_t.real, _f_path_t.imag, color="C1")
    ax1_2.axis("equal")
    gcf()
    return


@app.cell
def _(gcf, grid_1, linspace, subplots):
    def f_4(z):
        return (z - 2) * (z + 2)


    paths_3 = grid_1(xs=linspace(-1, 1, 11), ys=linspace(-1, 1, 11))
    t_4 = linspace(0.0, 1.0, 1000)
    _fig, (ax1_3, ax2_3) = subplots(1, 2, figsize=(8, 4.5))
    for _path in paths_3:
        _path_t = _path(t_4)
        _f_path_t = f_4(_path_t)
        ax1_3.plot(_path_t.real, _path_t.imag, color="C0")
        ax2_3.plot(_f_path_t.real, _f_path_t.imag, color="C1")
    ax1_3.axis("equal")
    ax2_3.axis("equal")
    gcf()
    return ax1_3, ax2_3


@app.cell
def _(gcf, grid_1, linspace, subplots):
    def f_5(z):
        return (z - 0.5) * (z + 0.5)


    paths_4 = grid_1(xs=linspace(-1, 1, 11), ys=linspace(-1, 1, 11))
    t_5 = linspace(0.0, 1.0, 1000)
    _fig, _axes = subplots(5, 5, figsize=(12, 12))
    _axes = [_ax for l in _axes for _ax in l]
    for _i, _ax in enumerate(_axes):
        for _path in paths_4:
            _path_t = _path(t_5)
            _alpha = _i / (len(_axes) - 1)
            _f_path_t = (1 - _alpha) * _path_t + _alpha * f_5(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="C0")
            _ax.set_xticks([])
            _ax.set_yticks([])
            _ax.axis("square")
    gcf()
    return


@app.cell
def _(gcf, grid_1, linspace, subplots):
    def f_6(z):
        return z**4


    paths_5 = grid_1(xs=linspace(-1, 1, 11), ys=linspace(-1, 1, 11))
    t_6 = linspace(0.0, 1.0, 1000)
    _fig, _axes = subplots(3, 3, figsize=(12, 12))
    _axes = [_ax for l in _axes for _ax in l]
    for _i, _ax in enumerate(_axes):
        for _path in paths_5:
            _path_t = _path(t_6)
            _alpha = _i / (len(_axes) - 1)
            _f_path_t = (1 - _alpha) * _path_t + _alpha * f_6(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="C0")
            _ax.set_xticks([])
            _ax.set_yticks([])
            _ax.axis("square")
    gcf()
    return


@app.cell
def _(exp, gcf, grid_1, linspace, subplots):
    def f_7(z):
        return exp(z)


    paths_6 = grid_1(xs=linspace(-1, 1, 11), ys=linspace(-1, 1, 11))
    t_7 = linspace(0.0, 1.0, 1000)
    _fig, _axes = subplots(5, 5, figsize=(12, 12))
    _axes = [_ax for l in _axes for _ax in l]
    for _i, _ax in enumerate(_axes):
        for _path in paths_6:
            _path_t = _path(t_7)
            _alpha = _i / (len(_axes) - 1)
            _f_path_t = (1 - _alpha) * _path_t + _alpha * f_7(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="C0")
            _ax.set_xticks([])
            _ax.set_yticks([])
            _ax.axis("square")
    gcf()
    return


@app.cell
def _(gcf, grid_1, linspace, log, subplots):
    def f_8(z):
        return log(z)


    paths_7 = grid_1(xs=linspace(1, 2, 11), ys=linspace(-1, 1, 11))
    t_8 = linspace(0.0, 1.0, 1000)
    _fig, _axes = subplots(5, 5, figsize=(12, 12))
    _axes = [_ax for l in _axes for _ax in l]
    for _i, _ax in enumerate(_axes):
        for _path in paths_7:
            _path_t = _path(t_8)
            _alpha = _i / (len(_axes) - 1)
            _f_path_t = (1 - _alpha) * _path_t + _alpha * f_8(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="C0")
            _ax.set_xticks([])
            _ax.set_yticks([])
            _ax.axis("square")
    gcf()
    return


@app.cell
def _(gcf, linspace, log, logspace, pi, polar_grid, subplots):
    def f_9(z):
        return log(z)


    paths_8 = polar_grid(
        rs=logspace(-1, 1, 5), thetas=linspace(-3 * pi / 4, 3 * pi / 4, 11)
    )
    t_9 = linspace(0.0, 1.0, 1000)
    _fig, _axes = subplots(3, 3, figsize=(12, 12))
    _axes = [_ax for l in _axes for _ax in l]
    for _i, _ax in enumerate(_axes):
        for _path in paths_8:
            _path_t = _path(t_9)
            _alpha = _i / (len(_axes) - 1)
            _f_path_t = (1 - _alpha) * _path_t + _alpha * f_9(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="C0")
            _ax.set_xticks([])
            _ax.set_yticks([])
            _ax.axis("square")
    gcf()
    return


@app.cell
def _(gcf, grid_1, linspace, sin, subplots):
    def f_10(z):
        return sin(z)


    paths_9 = grid_1(xs=linspace(1, 2, 11), ys=linspace(-1, 1, 11))
    t_10 = linspace(0.0, 1.0, 1000)
    _fig, _axes = subplots(5, 5, figsize=(12, 12))
    _axes = [_ax for l in _axes for _ax in l]
    for _i, _ax in enumerate(_axes):
        for _path in paths_9:
            _path_t = _path(t_10)
            _alpha = _i / (len(_axes) - 1)
            _f_path_t = (1 - _alpha) * _path_t + _alpha * f_10(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="C0")
            _ax.set_xticks([])
            _ax.set_yticks([])
            _ax.axis("square")
    gcf()
    return (t_10,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations
    """)
    return


@app.cell
def _(
    FuncAnimation,
    PillowWriter,
    clip,
    gcf,
    linspace,
    log,
    logspace,
    pi,
    polar_grid,
    subplots,
    t_10,
):
    def f_11(z):
        return log(z)


    paths_10 = polar_grid(
        rs=logspace(-1, 1, 5), thetas=linspace(-3 * pi / 4, 3 * pi / 4, 11)
    )
    _T = 5.0
    _FPS = 24
    _ss = linspace(-0.5, 1.5, 3 * 24)
    _fig, _ax = subplots(figsize=(12, 12))


    def _func(s):
        _ax.clear()
        for _path in paths_10:
            _path_t = _path(t_10)
            s = clip(s, 0.0, 1.0)
            _f_path_t = (1 - s) * _path_t + s * f_11(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="k")
            _ax.set_xticks([])
            _ax.set_yticks([])
            _ax.axis("square")
            _ax.set_xlim([-10, 10])
            _ax.set_ylim([-10, 10])
            _ax.axis("off")


    _writer = PillowWriter(fps=_FPS)
    _anim = FuncAnimation(_fig, _func, frames=_ss)
    _anim.save("movie.gif", writer=_writer)
    gcf()
    return


@app.cell
def _(mo):
    mo.image("movie.gif")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Joukowsky

    The circle is always the unit centered circle, the J transform is parametric and adjusts.
    """)
    return


@app.cell
def _(ax1_3, circle, gcf, linspace, pi, polar_grid, subplots):
    _gamma = circle()
    paths_11 = polar_grid(
        rs=linspace(1.0, 2.0, 5), thetas=linspace(0, 2 * pi, 8 + 1)
    )
    _fig, _axes = subplots()
    _fig.set_figwidth(12)
    t_11 = linspace(0.0, 1.0, 10000)
    color = "C1"
    for _path in paths_11:
        _path_t = _path(t_11)
        _axes.plot(_path_t.real, _path_t.imag, color="grey", lw=1)
    _axes.fill(_gamma(t_11).real, _gamma(t_11).imag, color=color, alpha=0.25)
    _axes.plot(_gamma(t_11).real, _gamma(t_11).imag, color=color, lw=2)
    _axes.set_xticks([])
    ax1_3.set_yticks([])
    _axes.axis("equal")
    _axes.axis("off")
    gcf()
    return paths_11, t_11


@app.cell
def _(ax2_3, circle, exp, gcf, paths_11, pi, subplots, t_11):
    a = 1.2
    _theta = -pi / 16
    b = 1 - a * exp(1j * _theta)


    def Joukowsky(z):
        w = a * z + b
        return 0.5 * (w + 1.0 / w)


    J = Joukowsky
    _gamma = circle()
    _J_gamma = lambda t: J(_gamma(t))
    _fig, _ax = subplots()
    _fig.set_figwidth(12)
    color_1 = "C1"
    for _path in paths_11:
        _J_path_t = J(_path(t_11))
        _ax.plot(_J_path_t.real, _J_path_t.imag, color="grey", lw=1)
    _ax.plot(_J_gamma(t_11).real, _J_gamma(t_11).imag, color=color_1, lw=2)
    _ax.fill(_J_gamma(t_11).real, _J_gamma(t_11).imag, color=color_1, alpha=0.25)
    _ax.set_xticks([])
    ax2_3.set_yticks([])
    _ax.axis("equal")
    _ax.axis("off")
    gcf()
    return (color_1,)


@app.cell
def _(
    FuncAnimation,
    PillowWriter,
    clip,
    color_1,
    exp,
    gcf,
    linspace,
    pi,
    polar_grid,
    subplots,
    subplots_adjust,
    t_11,
):
    a_1 = 1.2
    _theta = -pi / 16
    b_1 = 1 - a_1 * exp(1j * _theta)


    def Joukowsky_1(z):
        w = a_1 * z + b_1
        return 0.5 * (w + 1.0 / w)


    f_12 = J_1 = Joukowsky_1
    paths_12 = polar_grid(
        rs=linspace(1.0, 2.0, 5), thetas=linspace(0, 2 * pi, 8 + 1)
    )
    _FPS = 24
    _ss = linspace(0.0 - 1.0, 3.0 + 1.0, 3 * 24)
    _fig, _ax = subplots(figsize=(8, 6))


    def _func(s):
        _ax.clear()
        for _path in paths_12:
            _path_t = _path(t_11)
            sr = clip(s, 0.0, 3.0) / 3.0
            _f_path_t = (1 - sr) * _path_t + sr * f_12(_path_t)
            _ax.plot(_f_path_t.real, _f_path_t.imag, color="k")
            _ax.set_xticks([])
            _ax.set_yticks([])
        _path = paths_12[0]
        _path_t = _path(t_11)
        sr = clip(s, 0.0, 3.0) / 3.0
        _f_path_t = (1 - sr) * _path_t + sr * f_12(_path_t)
        _ax.plot(_f_path_t.real, _f_path_t.imag, color=color_1, lw=2)
        _ax.fill(_f_path_t.real, _f_path_t.imag, color=color_1, alpha=0.25)
        _ax.axis("square")
        _ax.set_xlim([-2, 2])
        _ax.set_ylim([-1.5, 1.5])
        subplots_adjust(left=0, bottom=0, right=1, top=1)
        _ax.axis("off")


    _writer = PillowWriter(fps=_FPS)
    _anim = FuncAnimation(_fig, _func, frames=_ss)
    _anim.save("Joukowsky.gif", writer=_writer)
    gcf()
    return


@app.cell
def _(mo):
    mo.image("Joukowsky.gif")
    return


@app.cell
def _(circle, exp, gcf, linspace, pi, polar_grid, savefig, subplots):
    _gamma = circle()
    paths_13 = polar_grid(
        rs=linspace(1.0, 2.0, 5), thetas=linspace(0, 2 * pi, 8 + 1)
    )
    _fig, (ax1_4, ax2_4) = subplots(1, 2, figsize=(12, 8))
    t_12 = linspace(0.0, 1.0, 10000)
    _axes = ax1_4
    color_2 = "C1"
    for _path in paths_13:
        _path_t = _path(t_12)
        _axes.plot(_path_t.real, _path_t.imag, color="grey", lw=1)
    _axes.fill(_gamma(t_12).real, _gamma(t_12).imag, color=color_2, alpha=0.25)
    _axes.plot(_gamma(t_12).real, _gamma(t_12).imag, color=color_2, lw=2)
    _ax = ax2_4
    a_2 = 1.2
    _theta = -pi / 16
    b_2 = 1 - a_2 * exp(1j * _theta)


    def Joukowsky_2(z):
        w = a_2 * z + b_2
        return 0.5 * (w + 1.0 / w)


    J_2 = Joukowsky_2
    _gamma = circle()
    _J_gamma = lambda t: J_2(_gamma(t))
    color_2 = "C1"
    for _path in paths_13:
        _J_path_t = J_2(_path(t_12))
        _ax.plot(_J_path_t.real, _J_path_t.imag, color="grey", lw=1)
    _ax.plot(_J_gamma(t_12).real, _J_gamma(t_12).imag, color=color_2, lw=2)
    _ax.fill(_J_gamma(t_12).real, _J_gamma(t_12).imag, color=color_2, alpha=0.25)
    _ax.set_xticks([])
    ax2_4.set_yticks([])
    _ax.axis("equal")
    _ax.axis("off")
    _axes.set_xticks([])
    ax1_4.set_yticks([])
    _axes.axis("equal")
    _axes.axis("off")
    savefig("Joukowsky-1.png")
    gcf()
    return J_2, a_2, b_2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Flows

    ### 🚧 Question

    Show that the 2D continuously differentiable steady 🏷️ **flow** (or 🏷️ **velocity field**)*

    $$
    \vec{v} = \left[
    \begin{array}{c}
    v_x \\
    v_y
    \end{array}
    \right]
    $$

    is irrotational and incompressible if and only if the 🏷️ **complex velocity** $f$ defined by

    $$
    f(x+iy) := v_x(x, y) -i v_y(x,y)
    $$

    is holomorphic.

    ### 🔓 Solution

    The flow is irrotational and incompressible if and only if

    $$
    \vec{\nabla} \wedge \vec{v}
    = \partial_x v_y - \partial_y v_x = 0
    = 0
    \; \text{ and } \;
    \vec{\nabla} \cdot \vec{v} = \partial_x v_x + \partial_y v_y = 0.
    $$

    On the other hand, the Cauchy-Riemann equations for $f$ are

    $$
    \partial_x v_x = \partial_y (-v_y)
    \; \text{ and } \;
    \partial_x (-v_y) = - \partial_y v_y.
    $$

    These sets of equations are identical. Therefore, the flow $\vec{v}$ is irrotational if and only its complex velocity $f$ is holomorphic.
    ◼️
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Boundary Condition

    ### 🚧 Question

    We will assume that a velocity field $\vec{f}$ defined on (an open neighbourghood of) the closed unit $D$ disk should be tangent to the disk on every point of the boundary. How does this condition translate to the complex velocity ?

    ### 🔓 Solution

    On the disk boundary, the velocity should be orthogonal to the disk outer normal

    $$
    \left[
    \begin{array}{c}
    v_x \\
    v_y
    \end{array}
    \right]
    \perp
    \left[
    \begin{array}{c}
    \cos \theta \\
    \sin \theta
    \end{array}
    \right].
    $$

    or equivalently, via the scalar product

    $$
    v_x \cos \theta + v_y \sin \theta = 0.
    $$

    We may rewrite this equation as

    $$
    \Re \left((v_x - i v_y) (\cos \theta + i \sin \theta) \right) = \Re \left(f(e^{i\theta}) e^{i\theta}\right) = 0.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🚧 Question

    Show that for any real constants $U$ and $C$, the complex velocity

    $$
    f(z) = U - \frac{U}{z^2} + \frac{C}{i 2\pi} \frac{1}{z}, \; z \in \mathbb{C}^*
    $$

    satisfies the boundary condition. What does represent the parameter $U$ physically?

    ### 🔓 Solution

    When $z=e^{i\theta}$, we get

    $$
    f(e^{i\theta}) = U + U e^{-i2\theta} + \frac{C}{i2\pi} e^{-i\theta}
    = \left(2 U \sin \theta + \frac{C}{2\pi} \right) \frac{e^{-i\theta}}{i}.
    $$

    Therefore

    $$
    \Re \left(f(e^{i\theta}) e^{i\theta}\right)
    =
    \Re \left(\left(2 U \sin \theta + \frac{C}{2\pi} \right) \frac{1}{i}\right)
    = 0.
    $$

    When $|z|$ is large, $f(z) \approx U$, thus $v_x \approx U$ and $v_y \approx 0$. Thus, $U$ represent the velocity (which is horizontal) far from the disk.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Circulation

    ### 🚧 Question

    Physicists define the 🏷️ **circulation** of the flow around the closed path $\gamma = (\gamma_x, \gamma_y)$ as
    the real number.

    $$
    \int_\gamma \vec{v} \cdot d \vec{\ell} = \int_0^1 \left( v_x(\gamma(s)) \gamma'_x(s) + v_y(\gamma(s)) \gamma'_y(s) \right) \, ds
    $$

    Can you compute the circulation using a line integral and the complex velocity associated to the flow?
    Show that as long as $\gamma$ makes 1 turn around the unit disk, the value of the circulation is the same.
    Compute it when $f(z) = U - \frac{U}{z^2} + \frac{C}{i 2\pi}$ and interpret the parameter $C$.

    ### 🔓 Solution

    We have

    $$
    \int_0^1 \left( v_x(\gamma(s)) \gamma'_x(s) - (-v_y(\gamma(s))) \gamma'_y(s) \right) \, ds
    =
    \int_0^1 \Re \left( f(\gamma(s)) \gamma'(s)\right) ds
    = \Re \int_0^1 f(\gamma(s)) \gamma'(s) ds
    = \Re \int_{\gamma} f(z) \, dz.
    $$

    If two paths $\gamma$ and $\mu$ turn around -- say $0$ -- the same number of times, since $f$ is holomorphic, the associated line integral is identical and so is the circulation. When $f(z) = U - \frac{U}{z^2} + \frac{C}{i 2\pi}\frac{1}{z}$, with $\gamma = [\circlearrowleft]$, we end up with

    $$
    \int_{[\circlearrowleft]} f(z) \, dz
    =
    \int_{[\circlearrowleft]} U - \frac{U}{z^2} + \frac{C}{i 2\pi}\frac{1}{z} \, dz
    =
    U\left(\int_{[\circlearrowleft]} 1 - \frac{1}{z^2} \, dz \right)
    +
    C \left(\frac{1}{i2\pi}\int_{[\circlearrowleft]} \frac{dz}{z}\right).
    $$

    Since $1 - 1/z$ has a primitive, the first integral is zero and it follows that

    $$
    \int_{[\circlearrowleft]} f(z) \, dz
    = C \times \mathrm{Res}\left(z \mapsto \frac{1}{z}, 0\right) = C.
    $$

    In other words, $C$ is the circulation of the flow around the disk.
    """)
    return


@app.cell
def _(axis, cos, figure, fill, gcf, linspace, meshgrid, pi, plot, quiver, sin):
    U = 1
    _C = 0


    def f_13(z):
        return U - U / (z * z) + _C / (2j * pi) / z


    def v(function):
        def v_(X, Y):
            function_xy = function(X + 1j * Y)
            return (function_xy.real, -function_xy.imag)
        return v_


    figure(figsize=(12, 12))
    _xs = _ys = linspace(-3.0, 3.0, 20)
    _X, _Y = meshgrid(_xs, _ys)
    _Vx, _Vy = v(f_13)(_X, _Y) * (_X * _X + _Y * _Y >= 1.0)
    quiver(_X, _Y, _Vx, _Vy, color="grey")
    color_3 = "C1"
    _theta = linspace(0, 2 * pi, 1000)
    fill(cos(_theta), sin(_theta), color="white")
    fill(cos(_theta), sin(_theta), color="C1", alpha=0.25)
    plot(cos(_theta), sin(_theta), color="C1", lw=2)
    axis("square")
    axis("off")
    gcf()
    return f_13, v


@app.cell
def _(
    axis,
    cos,
    f_13,
    figure,
    fill,
    gcf,
    linspace,
    meshgrid,
    pi,
    plot,
    sin,
    streamplot,
    v,
):
    figure(figsize=(12, 12))
    _xs = _ys = linspace(-3.0, 3.0, 100)
    _X, _Y = meshgrid(_xs, _ys)
    _Vx, _Vy = v(f_13)(_X, _Y) * (_X * _X + _Y * _Y >= 1.0)
    streamplot(_X, _Y, _Vx, _Vy, color="grey")
    _theta = linspace(0, 2 * pi, 1000)
    color_4 = "C1"
    fill(cos(_theta), sin(_theta), color="white")
    fill(cos(_theta), sin(_theta), color="C1", alpha=0.25)
    plot(cos(_theta), sin(_theta), color="C1", lw=2)
    axis("square")
    axis("off")
    gcf()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Joukowsky Transformation and its inverse

    $$
    w = J(z) = \frac{1}{2}\left(z + \frac{1}{z}\right)
    $$

    $$
    z^2 - 2w z + 1 = 0
    $$

    $$
    \Delta = 4w^2 - 4 = 4(w^2 - 1)
    $$

    $$
    z = \frac{2w \pm \sqrt{\Delta}}{2} = w \pm \sqrt{w^2-1}
    $$

    If we take into account the pretransformation $z \mapsto a z + b$, the inverse is

    $$
    z = \frac{w \pm \sqrt{w^2-1} - b}{a}
    $$
    """)
    return


@app.cell
def _(a_2, b_2, sqrt, vectorize):
    @vectorize
    def J_inv(w):
        s = sqrt(w * w - 1)
        z1 = (w + s - b_2) / a_2
        z2 = (w - s - b_2) / a_2
        if abs(z1) >= 1.0:
            return z1
        else:
            return z2
    return (J_inv,)


@app.cell
def _(a_2, b_2):
    def dJ(z):
        v = a_2 * z + b_2
        return 0.5 * (1 - 1 / (v * v)) * a_2
    return (dJ,)


@app.cell
def _(J_inv, dJ, f_13, vectorize):
    @vectorize
    def g(w):
        z = J_inv(w)
        return f_13(z) / dJ(z)
    return (g,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mapping of the complex velocity

    We admit (without proof) that for every point $w$ around the airfoil, there is a single $z$ around the unit disk such that $J(z) = w$.

    ### 🚧 Question

    Show that the complex velocity $g$ defined around the airfoil by

    $$
    g(w) := \frac{f(z)}{J'(z)}
    $$

    satisfies the tangential boundary conditions around the airfoil.

    ### 🔓 Solution

    The complex velocity $f$ satisfies on the boundary of the unit disk the condition

    $$
    \Re \left(f(z) n(z)\right)  =0
    $$

    where $n(e^{i\theta}) = e^{i\theta}$ is a normal to the boundary of the disk. Now, a normal to the airfoil is given by $J'(z) n(z)$ and thus,

    $$
    \Re \left(g(w) J'(z) n(z)\right) = \Re \left(\frac{f(z)}{J'(z)} J'(z) n(z)\right)
    =
    \Re \left(f(z) n(z)\right) = 0.
    $$

    Thus, the velocity $\overline{g(w)}$ is tangent to the airfoil as expected.
    """)
    return


@app.cell
def _(
    J_2,
    J_inv,
    axis,
    circle,
    figure,
    fill,
    g,
    gcf,
    linspace,
    meshgrid,
    plot,
    savefig,
    streamplot,
):
    _gamma = circle()
    _J_gamma = lambda t: J_2(_gamma(t))
    t_13 = linspace(0.0, 1.0, 1000)
    _fig = figure()
    _fig.set_figwidth(12)
    color_5 = "C1"
    fill(_J_gamma(t_13).real, _J_gamma(t_13).imag, color="white", zorder=10)
    fill(
        _J_gamma(t_13).real,
        _J_gamma(t_13).imag,
        color=color_5,
        alpha=0.25,
        zorder=20,
    )
    plot(_J_gamma(t_13).real, _J_gamma(t_13).imag, color=color_5, zorder=30)


    def v_1(function):
        def v_(X, Y):
            function_xy = function(X + 1j * Y)
            return (function_xy.real, -function_xy.imag)

        return v_


    _xs = linspace(-2.0, 2.0, 100)
    _ys = linspace(-1.0, 1.0, 100)
    _X, _Y = meshgrid(_xs, _ys)
    mask = abs(J_inv(_X + 1j * _Y)) >= 1.0
    _Vx, _Vy = v_1(g)(_X, _Y) * mask
    streamplot(_X, _Y, _Vx, _Vy, density=(1, 0.5), color="grey", zorder=-10)
    axis("tight")
    axis("equal")
    axis("off")
    savefig("flow.png")
    gcf()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Domain Coloring
    """)
    return


@app.cell
def _():
    def Joukowsky_3(z):
        return 0.5 * (z + 1.0 / z)


    def f_14(Z):
        return _Z
    return (Joukowsky_3,)


@app.cell
def _(
    Joukowsky_3,
    axis,
    contour,
    figure,
    gca,
    gcf,
    linspace,
    meshgrid,
    round,
    xlim,
    ylim,
):
    _T = linspace(-2.5, 2.5, 2048)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    f_15 = Joukowsky_3
    _W = f_15(_Z)
    figure(figsize=(8, 8))
    xlim(-2.5, 2.5)
    ylim(-2.5, 2.5)
    contour(
        _X,
        _Y,
        _W.real - round(_W.real),
        levels=[0.0],
        colors="black",
        linewidths=0.5,
    )
    contour(
        _X,
        _Y,
        _W.imag - round(_W.imag),
        levels=[0.0],
        colors="black",
        linewidths=0.5,
    )
    axis("equal")
    _ax = gca()
    gcf()
    return


@app.cell
def _(
    Joukowsky_3,
    angle,
    axis,
    contour,
    figure,
    gca,
    gcf,
    linspace,
    log,
    meshgrid,
    pi,
    round,
    xlim,
    ylim,
):
    _T = linspace(-2.5, 2.5, 2048)
    _X, _Y = meshgrid(_T, _T)
    _Z = _X + 1j * _Y
    f_16 = Joukowsky_3
    _W = f_16(_Z)
    _L = log(abs(_W))
    _N = 2
    _A = angle(_W) / pi * _N
    figure(figsize=(8, 8))
    xlim(-2.5, 2.5)
    ylim(-2.5, 2.5)
    contour(_X, _Y, _L - round(_L), levels=[0.0], colors="black", linewidths=0.5)
    contour(_X, _Y, _A - round(_A), levels=[0.0], colors="black", linewidths=0.5)
    axis("equal")
    _ax = gca()
    gcf()
    return


@app.cell
def _(colormaps, gcf, linspace, plot, twightlight):
    colormap = twilight = colormaps["twilight_shifted"]
    u = linspace(0.0, 1.0, 1024)
    _RGBA = colormap(u)  # float64, but discretised (8-bit)
    _RGB = _RGBA[:, :3]
    plot(u, _RGB[:, 0], color="red")
    plot(u, _RGB[:, 1], color="green")
    plot(u, _RGB[:, 2], color="blue")


    def shifted_twilight(u):
        return twightlight(u - 0.5 % 1)


    # NOTA: we can deliver a RBGA array to imshow, that works! 👍
    gcf()
    return


@app.cell
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, round):
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
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, round):
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
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, round):
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
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, round, savefig):
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
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, round):
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
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, round):
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
def _(angle, exp, figure, gca, gcf, linspace, log2, meshgrid, pi, round):
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
def _(angle, figure, gca, gcf, linspace, log2, meshgrid, pi, round, sin):
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
    round,
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
    round,
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


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
