import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre

def radial_probability_density(r, n, l, Z=1):
    """
    Calculates the radial probability density for the hydrogen atom.

    Args:
    r (float or np.ndarray): Radial distance from the nucleus.
    n (int): Principal quantum number.
    l (int): Azimuthal quantum number.
    Z (int): Atomic number (1 for hydrogen).

    Returns:
    np.ndarray: Radial probability density.
    """
    # Constants
    a0 = 0.529e-10  # Bohr radius in meters

    # Radial part of the wave function
    if n == 1 and l == 0:
        R = 2 * (Z / a0)**(3/2) * np.exp(-Z * r / a0)
    elif n == 2 and l == 0:
        R = (1 / (2 * np.sqrt(2))) * (Z / a0)**(3/2) * (2 - Z * r / a0) * np.exp(-Z * r / (2 * a0))
    elif n == 2 and l == 1:
        R = (1 / (2 * np.sqrt(6))) * (Z / a0)**(3/2) * (Z * r / a0) * np.exp(-Z * r / (2 * a0))
    elif n == 3 and l == 0:
        R = (2 / (81 * np.sqrt(3))) * (Z / a0)**(3/2) * (27 - 18 * Z * r / a0 + 2 * (Z * r / a0)**2) * np.exp(-Z * r / (3 * a0))
    elif n == 3 and l == 1:
        R = (8 / (27 * np.sqrt(6))) * (Z / a0)**(3/2) * (1 - Z * r / (6 * a0)) * (Z * r / a0) * np.exp(-Z * r / (3 * a0))
    elif n == 3 and l == 2:
        R = (4 / (81 * np.sqrt(30))) * (Z / a0)**(3/2) * (Z * r / a0)**2 * np.exp(-Z * r / (3 * a0))
    elif n == 4 and l == 0:
        R = (1 / (96 * np.sqrt(5))) * (Z / a0)**(3/2) * (96 - 72 * Z * r / a0 + 12 * (Z * r / a0)**2 - (Z * r / a0)**3) * np.exp(-Z * r / (4 * a0))
    elif n == 4 and l == 1:
        R = (1 / (96 * np.sqrt(15))) * (Z / a0)**(3/2) * (24 - 4 * Z * r / a0) * (Z * r / a0) * np.exp(-Z * r / (4 * a0))
    elif n == 4 and l == 2:
        R = (1 / (384 * np.sqrt(5))) * (Z / a0)**(3/2) * (8 - Z * r / a0) * (Z * r / a0)**2 * np.exp(-Z * r / (4 * a0))
    elif n == 4 and l == 3:
        R = (1 / (768 * np.sqrt(35))) * (Z / a0)**(3/2) * (Z * r / a0)**3 * np.exp(-Z * r / (4 * a0))
    else:
        raise NotImplementedError("Only states up to n=4 are implemented.")

    # Radial probability density
    P = (r**2) * (R**2)
    return P

def plot_probability_density():
    """
    Plots the radial probability density for the hydrogen atom for the first four energy levels.
    """
    # Radial distances from 0 to 20 Bohr radii
    r = np.linspace(0, 20 * 0.529e-10, 1000)

    # Plotting for the first four energy levels
    for n in range(1, 5):
        P = radial_probability_density(r, n, 0)
        plt.plot(r, P, label=f'n={n}, l=0')

    plt.title('Radial Probability Density for Hydrogen Atom')
    plt.xlabel('Radial Distance (m)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

# Execute the function to plot the probability density
if __name__ == "__main__":
    plot_probability_density()
