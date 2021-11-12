import copy


def get_method_of_steepest_descent():
    def numerical_derivative_1d(func, epsilon):
        def deriv_func(x):
            return (func(x + epsilon) - func(x)) / epsilon

        return deriv_func

    def nd_func_to_1d_func(func, X, axios):
        def new_func(x):
            new_X = copy.deepcopy(X)
            new_X[axios] = x
            return func(new_X)

        return new_func

    def numerical_derivative_nd(func, epsilon):
        def deriv_func(X):
            deriv = copy.deepcopy(X)
            for (index, x) in enumerate(X):
                deriv[index] = numerical_derivative_1d(nd_func_to_1d_func(func, X, index), epsilon)(x)
            return X

        return deriv_func

    return numerical_derivative_nd
