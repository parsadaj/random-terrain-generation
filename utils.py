import matplotlib.pyplot as plt
import numpy as np

def visualize_terrain(terrain, cmap='terrain', title="Random"):
    """
    Visualize the terrain heightmap using matplotlib.
    
    Args:
        terrain (numpy.ndarray): Terrain heightmap.
        cmap (str, optional): Colormap to use for visualization. Default is 'terrain'.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(terrain, cmap=cmap, vmin=0, vmax=1)
    ax.set_title(f'{title} Noise')
    # ax.set_xticks([])
    # ax.set_yticks([])
    fig.colorbar(im, ax=ax)
    plt.show()



def visualize_3d_terrain(terrain, cmap='terrain', elev=45, azim=45, title="Random"):
    """
    Visualize the terrain heightmap in 3D using matplotlib.
    
    Args:
        terrain (numpy.ndarray): Terrain heightmap.
        cmap (str, optional): Colormap to use for visualization. Default is 'terrain'.
        elev (float, optional): Elevation angle for the 3D view. Default is 45 degrees.
        azim (float, optional): Azimuth angle for the 3D view. Default is 45 degrees.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(terrain.shape[0])
    y = np.arange(terrain.shape[1])
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, terrain, cmap=cmap, rstride=1, cstride=1, linewidth=0, antialiased=False)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Elevation')
    ax.set_title(f'{title} Terrain')

    ax.view_init(elev=elev, azim=azim)
    plt.show()
