import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Paths
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Paths & Winding Number
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    class Path:
        def __init__(self, path):
            if isinstance(path, Path):
                self._fns = path._fns[:]
            elif callable(path):
                self._fns = [path]
            elif isinstance(path, list):
                self._fns = sum([Path(p)._fns for p in path], [])
            else:
                raise TypeError(f"{path} is not a path.")

        def __or__(self, other):
            return Path([self, other])

        def reverse(self):
            return Path([lambda t: fn(1.0 - t) for fn in reversed(self._fns)])

        def __call__(self, t):
            n = len(self._fns)
            t = np.asarray(t)
            scalar = t.ndim == 0
            t = np.atleast_1d(t)
            result = np.zeros_like(t, dtype=complex)
            for i, fn in enumerate(self._fns):
                lower = i / n
                upper = (i + 1) / n
                if i == n - 1:
                    mask = (lower <= t) & (t <= upper)
                else:
                    mask = (lower <= t) & (t < upper)
                t_scaled = (t[mask] - lower) * n
                result[mask] = fn(t_scaled)
            if scalar:
                result = result[0]
            return result

        def transform(self, f):
            return Path([lambda t, fn=fn: f(fn(t)) for fn in self._fns])

        def integral(self, f, n=1000):
            t = np.linspace(0.0, 1.0, n, endpoint=False)
            s = 0.0j
            dt = 1.0 / n
            for i, fn in enumerate(self._fns):
                path_t = fn(t)
                dpath_t = fn(t + dt) - path_t
                ds = sum(f(path_t) * dpath_t)
                s += ds
            return s

        # TODO: keep the same (current) color. Try "phantom" call?
        def plot(self, n=1000, **kwargs):
            t = np.linspace(0.0, 1.0, n)
            dt = 1.0 / n
            kwargs.setdefault("color", "k")

            for fn in self._fns:
                vals = fn(t)
                line = plt.plot(vals.real, vals.imag, **kwargs)
                color = kwargs.get("color") or line[0].get_color()
                z_tangent = (fn(0.5 + dt / 2) - fn(0.5 - dt / 2)) / dt
                angle_deg = np.degrees(
                    np.angle(z_tangent)
                )  
                plt.plot(
                    fn(0.5).real,
                    fn(0.5).imag,
                    marker=(
                        3,
                        0,
                        angle_deg - 90,
                    ),  # Triangle marker rotated to tangent direction
                    markersize=10,
                    color=color,
                )

        def delta_arg(path, a=0.0, n=1000):
            def f(z):
                return 1.0 / (z - a)

            i = path.integral(f, n)
            return i.imag

        def winding_number(path, a, n=1000):  # Assumption: the path is closed
            w = path.delta_arg(a, n)
            return int(round(w / 2 / np.pi))


    def circle(c=0j, r=1.0, arg0=0.0, arg1=2 * np.pi):
        def _gamma(t):
            return r * np.exp(1j * (arg0 + (arg1 - arg0) * t)) + c

        return Path(_gamma)


    def line(z0=0, z1=1):
        def _gamma(t):
            return (1 - t) * z0 + t * z1

        return Path(_gamma)
    return Path, circle, line


@app.cell
def _(circle, plt):
    circle().plot()
    plt.axis("equal")
    plt.grid(True)
    plt.gcf()
    return


@app.cell
def _(circle):
    def f(z):
        return 1.0 / z


    circle().integral(f)
    return


@app.cell
def _():
    return


@app.cell
def _(circle):
    circle().winding_number(0.0)
    return


@app.cell
def _(circle, np):
    circle(arg0=0.0, arg1=6 * np.pi).winding_number(0.0)
    return


@app.cell
def _(circle):
    circle(c=0.5).winding_number(0.0)
    return


@app.cell
def _(circle):
    circle(c=-1.5).winding_number(0.0)
    return


@app.cell
def _(circle):
    circle(c=0.5j, r=0.25)
    return


@app.cell
def _(circle):
    circle(c=0.5j, r=0.25).reverse()
    return


@app.cell
def _(circle, line, np, plt):
    theta = np.pi / 6
    pac_man = (
        line(0.0, np.exp(1j * theta))
        | circle(arg0=theta, arg1=2 * np.pi - theta)
        | line(np.exp(-1j * theta), 0.0)
        | circle(c=0.5j, r=0.25).reverse()
    )
    pac_man.plot()
    points = [1.0 + 0.0j, -0.5 + 0.0j, 0.0 + 0.5j]
    for i, point in enumerate(points):
        # plt.plot(point.real, point.imag, "+", label=f"point {i+1}")
        wn = pac_man.winding_number(point)
        plt.text(
            point.real,
            point.imag,
            f"{wn}",
            horizontalalignment="center",
            verticalalignment="center",
        )
    plt.axis("equal")
    plt.grid(True)
    plt.title("Winding Numbers & Pac-Man")
    plt.gcf()
    return pac_man, points


@app.cell
def _(pac_man, points):
    for _i, _point in enumerate(points):
        print(f"Point {_i + 1}, winding number: {pac_man.winding_number(_point)}")
    return


@app.cell
def _(line, plt):
    square = (
        line(1 - 1j, 1 + 1j)
        | line(1 + 1j, -1 + 1j)
        | line(-1 + 1j, -1 - 1j)
        | line(-1 - 1j, 1 - 1j)
    )

    square.plot()
    plt.grid(True)
    plt.axis("square")
    plt.gcf()
    return (square,)


@app.cell
def _(square):
    square.winding_number(0.0)  # bug!
    return


@app.cell
def _(square):
    (square | square).winding_number(0.0)
    return


@app.cell
def _(square):
    -square.winding_number(0.0)
    return


@app.cell
def _(square):
    square.winding_number(0.95 + 0.95j)
    return


@app.cell
def _(square):
    square.winding_number(a=1.05 + 0.95j)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Grids
    """)
    return


@app.cell
def _(Path, circle, exp, line):
    def grid(xs, ys):
        paths = []
        x_min, x_max = (xs[0], xs[-1])
        y_min, y_max = (ys[0], ys[-1])
        for x in xs:
            paths.append(line(x + 1j * y_min, x + 1j * y_max))
        for y in ys:
            paths.append(line(x_min + 1j * y, x_max + 1j * y))
        return Path(paths)


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
        return Path(paths)
    return (grid,)


@app.cell
def _(grid, np, plt):
    def _():
        rg = grid(xs=np.linspace(0.0, 1.0, 6), ys=np.linspace(0.0, 1, 6))
        pg = rg.transform(lambda z : 1 / (z + 1))
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
        plt.sca(ax1)
        rg.plot()
        ax1.axis("equal")
        plt.sca(ax2)
        pg.plot()
        ax2.axis("equal")
        return fig
    _()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
