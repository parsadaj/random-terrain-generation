import numpy as np


def bilinear_interpolation(x, y, g00, g10, g01, g11):
    """
    Bilinear interpolation between four points.
    """
    x1 = g00 * (1 - x) + g10 * x
    x2 = g01 * (1 - x) + g11 * x
    return x1 * (1 - y) + x2 * y

def bicubic_interpolation(x, y, g00, g10, g01, g11):
    """
    Bicubic interpolation between four points using the S-curve function s(x) = -2x^3 + 3x^2.
    """
    def s(x):
        return -2 * x**3 + 3 * x**2

    x1 = g00 * (1 - s(x)) + g10 * s(x)
    x2 = g01 * (1 - s(x)) + g11 * s(x)
    return x1 * (1 - s(y)) + x2 * s(y)



# def generate_random_terrain(size, scale, interpolation='bilinear'):
#     """
#     Generate a random terrain heightmap using interpolated noise.
    
#     Args:
#         size (int): Size of the terrain heightmap.
#         scale (int): Scale factor for the random lattice.
#         interpolation (str): Type of interpolation ('bilinear' or 'bicubic').
    
#     Returns:
#         numpy.ndarray: Terrain heightmap.
#     """
#     bl_terrain = np.zeros((size, size))
#     bc_terrain = np.zeros((size, size))
#     coarse_size = size // scale + 1
    
#     # Generate random lattice
#     coarse_terrain = np.random.rand(coarse_size, coarse_size)
    
#     # Interpolate between lattice points
#     for i in range(coarse_size-1):
#         for j in range(coarse_size-1):
#             i0 = i * scale
#             i1 = (i + 1) * scale
#             j0 = j * scale
#             j1 = (j + 1) * scale
            
#             g00 = coarse_terrain[i, j]
#             g10 = coarse_terrain[i + 1, j] #if i + 1 < coarse_size else coarse_terrain[0, j]
#             g01 = coarse_terrain[i, j + 1] #if j + 1 < coarse_size else coarse_terrain[i, 0]
#             g11 = coarse_terrain[i + 1, j + 1] #if i + 1 < coarse_size and j + 1 < coarse_size else coarse_terrain[0, 0]
            
#             for x in range(i0, i1):
#                 for y in range(j0, j1):
#                     x_ratio = (x - i0) / scale
#                     y_ratio = (y - j0) / scale
                    
#                     bl_terrain[x, y] = bilinear_interpolation(x_ratio, y_ratio, g00, g10, g01, g11)
#                     bc_terrain[x, y] = bicubic_interpolation(x_ratio, y_ratio, g00, g10, g01, g11)
    
#     return bl_terrain, bc_terrain



# def generate_gradient_noise(size, scale, interpolation='bilinear'):
#     """
#     Generate a random terrain heightmap using gradient noise (Perlin noise).

#     Args:
#         size (int): Size of the terrain heightmap.
#         scale (int): Scale factor for the random lattice.
#         interpolation (str): Type of interpolation ('bilinear' or 'bicubic').

#     Returns:
#         numpy.ndarray: Terrain heightmap.
#     """
#     bl_terrain = np.zeros((size, size))
#     bc_terrain = np.zeros((size, size))
#     coarse_size = size // scale
    
#     # Generate random gradients
#     gradients = np.random.rand(coarse_size + 1, coarse_size + 1, 2) * 2 - 1
    
#     # Calculate heights from gradients
#     for i in range(coarse_size):
#         for j in range(coarse_size):
#             i0 = i * scale
#             i1 = (i + 1) * scale
#             j0 = j * scale
#             j1 = (j + 1) * scale
            
#             for x in range(i0, i1):
#                 for y in range(j0, j1):
#                     x_ratio = (x - i0) / scale
#                     y_ratio = (y - j0) / scale
                    
#                     g00 = gradients[i, j]
#                     g10 = gradients[i + 1, j]
#                     g01 = gradients[i, j + 1]
#                     g11 = gradients[i + 1, j + 1]
                    
#                     h00 = np.dot(g00, [x_ratio, y_ratio])
#                     h10 = np.dot(g10, [x_ratio - 1, y_ratio])
#                     h01 = np.dot(g01, [x_ratio, y_ratio - 1])
#                     h11 = np.dot(g11, [x_ratio - 1, y_ratio - 1])
#                     bl_terrain[x, y] = bilinear_interpolation(x_ratio, y_ratio, h00, h10, h01, h11)
#                     bc_terrain[x, y] = bicubic_interpolation(x_ratio, y_ratio, h00, h10, h01, h11)
    
#     return bl_terrain, bc_terrain


def generate_random_terrain_value(size, lattice_size, random_seed=43):
    """
    Generate a random terrain heightmap using interpolated noise.
    
    Args:
        size (int): Size of the terrain heightmap.
        lattice_size (int): size of the lattice.
    
    Returns:
        numpy.ndarray: Terrain heightmap.
    """
    
    bl_terrain = np.zeros((size, size)) # for bilinear
    bc_terrain = np.zeros((size, size)) # for bicubic
    

    n_lattice_points = size // lattice_size + 1
    np.random.seed(random_seed)
    lattice_heights = np.random.rand(n_lattice_points, n_lattice_points)
    lattice_heights.shape


    # Interpolate between lattice points
    for i in range(n_lattice_points-1):
        for j in range(n_lattice_points-1):
            i0 = i * lattice_size
            i1 = (i + 1) * lattice_size
            j0 = j * lattice_size
            j1 = (j + 1) * lattice_size
            
            g00 = lattice_heights[i, j]
            g10 = lattice_heights[i + 1, j] #if i + 1 < coarse_size else coarse_terrain[0, j]
            g01 = lattice_heights[i, j + 1] #if j + 1 < coarse_size else coarse_terrain[i, 0]
            g11 = lattice_heights[i + 1, j + 1] #if i + 1 < coarse_size and j + 1 < coarse_size else coarse_terrain[0, 0]
            
            for x in range(i0, i1):
                for y in range(j0, j1):
                    x_ratio = (x - i0) / lattice_size
                    y_ratio = (y - j0) / lattice_size
                    
                    bl_terrain[x, y] = bilinear_interpolation(x_ratio, y_ratio, g00, g10, g01, g11)
                    bc_terrain[x, y] = bicubic_interpolation(x_ratio, y_ratio, g00, g10, g01, g11)
    
    return bl_terrain, bc_terrain



def generate_random_terrain_gradient(size, lattice_size, random_seed=43):
    """
    Generate a random terrain heightmap using gradient noise (Perlin noise).

    Args:
        size (int): Size of the terrain heightmap.
        lattice_size (int): size of the lattice.

    Returns:
        numpy.ndarray: Terrain heightmap.
    """
    bl_terrain = np.zeros((size, size)) # for bilinear
    bc_terrain = np.zeros((size, size)) # for bicubic
    
    # Generate random gradients
    n_lattice_points = size // lattice_size + 1
    np.random.seed(random_seed)
    gradients = np.random.rand(n_lattice_points, n_lattice_points, 2) * 3 - 1.5
    gradients.min(), gradients.max(), gradients.mean(), gradients.shape
    
    # Calculate heights from gradients
    for i in range(n_lattice_points-1):
        for j in range(n_lattice_points-1):
            i0 = i * lattice_size
            i1 = (i + 1) * lattice_size
            j0 = j * lattice_size
            j1 = (j + 1) * lattice_size
            
            g00 = gradients[i, j]
            g10 = gradients[i + 1, j] #if i + 1 < coarse_size else coarse_terrain[0, j]
            g01 = gradients[i, j + 1] #if j + 1 < coarse_size else coarse_terrain[i, 0]
            g11 = gradients[i + 1, j + 1] #if i + 1 < coarse_size and j + 1 < coarse_size else coarse_terrain[0, 0]
            
            for x in range(i0, i1):
                for y in range(j0, j1):
                    x_ratio = (x - i0) / lattice_size
                    y_ratio = (y - j0) / lattice_size
                    
                    h00 = np.dot(g00, [x_ratio, y_ratio])
                    h10 = np.dot(g10, [x_ratio - 1, y_ratio])
                    h01 = np.dot(g01, [x_ratio, y_ratio - 1])
                    h11 = np.dot(g11, [x_ratio - 1, y_ratio - 1])
                    
                    bl_terrain[x, y] = bilinear_interpolation(x_ratio, y_ratio, h00, h10, h01, h11)
                    bc_terrain[x, y] = bicubic_interpolation(x_ratio, y_ratio, h00, h10, h01, h11)
        

        
    return bl_terrain, bc_terrain



def generate_fractal_terrain(size, lattice_size, noise_fn, base_freq, num_octaves, random_seed):
    """
    Generate a fractal terrain heightmap using 1/f noise.

    Args:
        size (int): Size of the terrain heightmap.
        base_freq (float): Base frequency for the lowest-frequency noise.
        num_octaves (int): Number of octaves (frequency scales) to use.
        scale (int): Scale factor for the random lattice.
        interpolation (str): Type of interpolation ('bilinear' or 'bicubic').

    Returns:
        numpy.ndarray: Fractal terrain heightmap.
    """
    terrain_bl = np.zeros((size, size))
    terrain_bc = np.zeros((size, size))
    freq = base_freq
    
    for octave in range(num_octaves):
        noise_bl, noise_bc = noise_fn(size, int(lattice_size/freq), random_seed=random_seed + octave)
        terrain_bc += noise_bc / (2 ** octave)
        terrain_bl += noise_bl / (2 ** octave)
        freq *= 2
    
    return terrain_bl, terrain_bc