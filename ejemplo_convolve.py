from scipy.ndimage import convolve
import numpy as np

a = np.random.randn(10,10)
b = np.identity(4)

convolve(a, b, mode='constant')[1:-1, 1:-1]
idx = np.arange(4)+1
a[idx, idx].sum()
