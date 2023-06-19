import matplotlib.pyplot as plt

A = 10
B = 25
C = 2.67


def delta_calculations(x, y, z):
    dx = (A * y - A * x)
    dy = (-x * z + B * x - y)
    dz = (x * y - C * z)
    return dx, dy, dz


def display_plot(x_list, z_list, name_of_method):
    plt.plot(x_list, z_list)
    plt.xlabel('x')
    plt.ylabel('z')
    plt.title(name_of_method)
    plt.show()


class Euler:
    def __init__(self, x, y, z, dt, iterations):
        x_list = []
        z_list = []
        for i in range(iterations):
            dx, dy, dz = delta_calculations(x, y, z)

            x += dx * dt
            y += dy * dt
            z += dz * dt

            x_list.append(x)
            z_list.append(z)

        display_plot(x_list, z_list, "Euler")


class Midpoint:
    def __init__(self, x, y, z, dt, iterations):
        x_list = []
        z_list = []
        for i in range(iterations):
            dx, dy, dz = delta_calculations(x, y, z)
            x_2 = x + 0.5 * dx * dt
            y_2 = y + 0.5 * dy * dt
            z_2 = z + 0.5 * dz * dt
            dx_2, dy_2, dz_2 = delta_calculations(x_2, y_2, z_2)

            x += dx_2 * dt
            y += dy_2 * dt
            z += dz_2 * dt

            x_list.append(x)
            z_list.append(z)

        display_plot(x_list, z_list, "Midpoint")


class RungeKutta:
    def __init__(self, x, y, z, dt, iterations):
        x_list = []
        z_list = []
        for i in range(iterations):
            k1x, k1y, k1z = delta_calculations(x, y, z)
            k2x, k2y, k2z = delta_calculations(x + 0.5 * k1x * dt, y + 0.5 * k1y * dt, z + 0.5 * k1z * dt)
            k3x, k3y, k3z = delta_calculations(x + 0.5 * k2x * dt, y + 0.5 * k2y * dt, z + 0.5 * k2z * dt)
            k4x, k4y, k4z = delta_calculations(x + k3x * dt, y + k3y * dt, z + k3z * dt)

            x += (k1x + 2 * k2x + 2 * k3x + k4x) * dt / 6
            y += (k1y + 2 * k2y + 2 * k3y + k4y) * dt / 6
            z += (k1z + 2 * k2z + 2 * k3z + k4z) * dt / 6

            x_list.append(x)
            z_list.append(z)

        display_plot(x_list, z_list, "RungeKutta")


Euler(1, 1, 1, 0.01, 5000)
Midpoint(1, 1, 1, 0.03, 5000)
RungeKutta(1, 1, 1, 0.03, 5000)
