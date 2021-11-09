from scipy.spatial import distance
import copy

coordinate_descent_iter_list = []
coordinate_descent_iter_label = ['X', 'z']


def get_coordinate_descent(optimization_algoritm):
    def to_2d_fun(f, X, i):
        def new_fun(x):
            X[i] = x
            return f(X)

        return new_fun

    def coordinate_descent(f, start_point, eps: float, max_iteration_g: int = 200):
        coordinate_descent_iter_list.clear()

        def optimize_point(point):
            new_point = copy.deepcopy(point)
            for (index, x) in enumerate(new_point):
                min = optimization_algoritm(to_2d_fun(f, new_point, index), new_point[index])
                new_point[index] = min
            return new_point

        def optimize(previous_point, max_iteration):
            new_point = optimize_point(copy.deepcopy(previous_point))
            coordinate_descent_iter_list.append(copy.deepcopy([new_point, f(new_point)]))

            tmp = distance.euclidean(previous_point, new_point)
            if distance.euclidean(previous_point, new_point) < eps or max_iteration < 0:
                return new_point
            else:
                return optimize(new_point, max_iteration - 1)

        coordinate_descent_iter_list.append(copy.deepcopy([start_point, f(start_point)]))
        return optimize(start_point, max_iteration_g)

    return coordinate_descent
