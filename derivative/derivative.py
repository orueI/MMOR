import copy

from MMOR.utils.function import nd_func_to_1d_func


def numerical_derivative_1d(func, epsilon):
    def deriv_func(x):
        return (func(x + epsilon) - func(x)) / epsilon

    return deriv_func


def numerical_derivative_nd(func, epsilon):
    def deriv_func(X):
        deriv = copy.deepcopy(X)
        print(deriv)
        for (index, x) in enumerate(X):
            deriv[index] = numerical_derivative_1d(nd_func_to_1d_func(func, X, index), epsilon)(x)
            print(X)
        return X

    return deriv_func
