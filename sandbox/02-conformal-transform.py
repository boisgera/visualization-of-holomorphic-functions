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
    # Conformal Maps
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(mo):
    mo.md(r"""
    ## Grids
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Maps
    """)
    return


@app.cell
def _(plt):
    def display_map(paths, f):
        f_paths = paths.transform(f)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
        plt.sca(ax1)
        paths.plot(color="C0")
        plt.sca(ax2)
        f_paths.plot(color="C1")
        ax1.axis("equal")
        ax2.axis("equal")
        return fig    
    return (display_map,)


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            xs=np.linspace(-1, 1, 11),
            ys=np.linspace(-1, 1, 11),
        ),
        lambda z: 1 / (z + 2),
    )
    return


@app.cell
def _(display_map, np, polar_grid):
    display_map(
        polar_grid(
            rs=np.logspace(-4, 0, 5, base=2),
            thetas=np.linspace(0, 2 * np.pi, 8 + 1),
        ),
        lambda z: 1 / (z + 2),
    )
    return


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            np.linspace(0, 1, 4),
            np.linspace(0, np.pi, 8 + 1),
        ),
        lambda z: np.exp(z),
    )
    return


@app.cell
def _(display_map, np, polar_grid):
    display_map(
        polar_grid(
            rs=np.logspace(-4, 0, 5, base=2),
            thetas=np.linspace(0, 2 * np.pi, 8 + 1),
        ),
        lambda z: np.exp(z),
    )
    return


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            np.linspace(-1, 1, 11),
            np.linspace(-1, 1, 11),
        ),
        lambda z: (z - 2) * (z + 2),
    )
    return


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            np.linspace(-1, 1, 11),
            np.linspace(-1, 1, 11),
        ),
        lambda z: (z - 0.5) * (z + 0.5)
    )
    return


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            np.linspace(-1, 1, 11),
            np.linspace(-1, 1, 11),
        ),
        lambda z: z**4
    )
    return


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            np.linspace(-1, 1, 11),
            np.linspace(-1, 1, 11),
        ),
        lambda z: np.exp(z)
    )
    return


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            np.linspace(1, 3, 11),
            np.linspace(-1, 1, 11),
        ),
        lambda z: np.log(z)
    )
    return


@app.cell
def _(display_map, np, polar_grid):
    display_map(
        polar_grid(
            rs=np.logspace(-1, 1, 5),
            thetas=np.linspace(-3 * np.pi / 4, 3 * np.pi / 4, 11),
        ),
        lambda z: np.log(z),
    )
    return


@app.cell
def _(display_map, grid, np):
    display_map(
        grid(
            np.linspace(-1, 1, 11),
            np.linspace(-1, 1, 11),
        ),
        lambda z: np.sin(z)
    )
    return


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
    display_map,
    gcf,
    grid,
    linspace,
    log,
    logspace,
    np,
    pi,
    polar_grid,
    subplots,
    t_10,
):
    display_map(
        grid(
            np.linspace(-1, 1, 11),
            np.linspace(-1, 1, 11),
        ),
        lambda z: np.exp(z)
    )

    def f_11(z):
        return log(z)

    # TODO: adapt; interpolate the transform. Probe the start and end to get the proper
    # axis bounds? Adapt with a slider (instead of a movie)?

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


@app.cell
def _():
    def Joukowsky_3(z):
        return 0.5 * (z + 1.0 / z)


    def f_14(Z):
        return _Z
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Appendix
    """)
    return


@app.cell
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
                line(r_min * np.exp(1j * _theta) + c, r_max * np.exp(1j * _theta) + c)
            )
        return Path(paths)
    return circle, grid, polar_grid


if __name__ == "__main__":
    app.run()
