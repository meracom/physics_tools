import numpy as np
import matplotlib.pyplot as plt

def horizontal_throw(v0, angle, height, g=9.81, t_max=10, num_points=1000):
    """
    Simulates the motion of a projectile in a gravitational field and plots the trajectory.

    Args:
    v0 (float): Initial velocity (m/s).
    angle (float): Launch angle in degrees.
    height (float): Initial height (m).
    g (float): Acceleration due to gravity (m/s^2). Default is 9.81 m/s^2.
    t_max (float): Maximum time to simulate (s). Default is 10 seconds.
    num_points (int): Number of points to calculate. Default is 1000.
    """
    # Convert angle to radians
    angle_rad = np.radians(angle)
    
    # Time array
    t = np.linspace(0, t_max, num_points)
    
    # Initial velocity components
    v0_x = v0 * np.cos(angle_rad)
    v0_y = v0 * np.sin(angle_rad)
    
    # Position calculations
    x = v0_x * t
    y = height + v0_y * t - 0.5 * g * t**2
    
    # Find the time when the projectile hits the ground
    t_ground = (v0_y + np.sqrt(v0_y**2 + 2 * g * height)) / g
    x_ground = v0_x * t_ground
    
    # Plot the trajectory
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Projectile Trajectory')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(0, x_ground)
    plt.ylim(0, max(height, max(y)))
    plt.title('Horizontal Throw in a Gravitational Field')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parameters for the horizontal throw
v0 = 1  # Initial velocity in m/s
angle = 0  # Launch angle in degrees
height = 2  # Initial height in meters

# Execute the function to simulate and plot the horizontal throw
if __name__ == "__main__":
    horizontal_throw(v0, angle, height)
