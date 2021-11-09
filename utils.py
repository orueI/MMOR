import numpy as np


def require(value: bool):
    if not value:
        raise Exception("IllegalArgumentException")


def center(X):
    return X[0] + (X[0] - X[1]) / 2


def to_nd_array(arr):
    return np.array([it for it in np.array(arr)])
