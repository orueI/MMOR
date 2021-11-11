def get_method_of_steepest_descent():
    def numerical_derivative_1d(func, epsilon):
        def deriv_func(x):
            return (func(x + epsilon) - func(x)) / epsilon

        return deriv_func

    def numerical_derivative_nd(func, epsilon):
        def deriv_func(X):
            return X

        return deriv_func

    def method_of_steepest_descent():

    return " "
