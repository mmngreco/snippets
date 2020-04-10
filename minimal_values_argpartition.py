'''Example.
'''
import numpy as np
import matplotlib.pyplot as plt

N = 3
random_points = np.random.rand(20, 2)
distance_from_origin = (random_points ** 2).sum(axis=1)

plt.scatter(*random_points.T)

idx_N_near_origin = np.argpartition(distance_from_origin, N)[:N]
n_minimal_values = random_points[idx_N_near_origin]

plt.gca().scatter(*n_minimal_values.T)



