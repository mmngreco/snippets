import numpy as np


def get_index(a, item):
    return np.argmax(a==item)


def get_indexes(a, items):
    return np.vectorize(get_index)(a, items)
