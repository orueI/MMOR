import copy


def nd_func_to_1d_func(func, X, axios):
    def new_func(x):
        new_X = copy.deepcopy(X)
        new_X[axios] = x
        return func(new_X)

    return new_func
