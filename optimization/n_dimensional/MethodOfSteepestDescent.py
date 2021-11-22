import copy

import numpy as np
from scipy.spatial import distance

method_of_steepest_descent_iter_list = []
method_of_steepest_descent_iter_label = ['X', 'z']


# def get_method_of_steepest_descent(optimization_algorithm):
#     def method_of_steepest_descent(f, f_derivative, start_point, eps: float, max_iteration_g: int = 200):
#         def to_2d_fun(f, start_g_point, gradient_of_point):
#             direction = np.cos(np.arctan(gradient_of_point))
#
#             def res_f(x: float):
#                 return f(start_g_point + direction * x)
#
#             def point(x: float):
#                 return start_g_point + direction * x
#
#             return [res_f, point]
#
#         method_of_steepest_descent_iter_list.clear()
#
#         def optimize_point(point):
#             opt_f = to_2d_fun(f, point, f_derivative(point))
#             new_point = optimization_algorithm(opt_f[0], copy.deepcopy(point))
#             return opt_f[1](new_point)
#
#         def optimize(previous_point, max_iteration):
#             new_point = optimize_point(copy.deepcopy(previous_point))
#             euclidean = distance.euclidean(previous_point, new_point)
#             method_of_steepest_descent_iter_list.append(copy.deepcopy([new_point, f(new_point), euclidean]))
#
#             if euclidean < eps or max_iteration < 0:
#                 return new_point
#             else:
#                 return optimize(new_point, max_iteration - 1)
#
#         method_of_steepest_descent_iter_list.append(copy.deepcopy([start_point, f(start_point), 0]))
#         return optimize(start_point, max_iteration_g)
#
#     return method_of_steepest_descent


def get_method_of_steepest_descent(optimization_algorithm):
    def norm(X):
        arr = np.array(X)
        norm = np.linalg.norm(arr)
        normal_array = arr / norm
        return normal_array

    def method_fletcher_reeves(f, f_derivative, start_point, eps: float, max_iteration_g: int = 200):
        def to_2d_fun(f, start_g_point, gradient_of_point):
            direction = np.cos(np.arctan(gradient_of_point))

            def res_f(x: float):
                return f(start_g_point + direction * x)

            def point(x: float):
                return start_g_point + direction * x

            return [res_f, point]

        method_of_steepest_descent_iter_list.clear()

        def optimize_point(point, previous_point):
            grad = norm(np.array(f_derivative(point)) * -1)

            opt_f = to_2d_fun(f, point, grad)
            new_point = optimization_algorithm(opt_f[0], copy.deepcopy(point))
            new_point = opt_f[1](new_point)
            euclidean = distance.euclidean(point, new_point)

            return point + euclidean * grad

        def optimize(point, previous_point, max_iteration):
            new_point = optimize_point(copy.deepcopy(point), copy.deepcopy(previous_point))
            euclidean = distance.euclidean(point, new_point)
            method_of_steepest_descent_iter_list.append(copy.deepcopy([new_point, f(new_point), euclidean]))

            if euclidean < eps or max_iteration < 0:
                return new_point
            else:
                return optimize(new_point, point, max_iteration - 1)

        method_of_steepest_descent_iter_list.append(copy.deepcopy([start_point, f(start_point), 0]))

        grad = np.array(f_derivative(start_point))
        opt_f = to_2d_fun(f, start_point, grad)
        new_point = optimization_algorithm(opt_f[0], copy.deepcopy(start_point))
        new_point = opt_f[1](new_point)

        return optimize(start_point, new_point, max_iteration_g)

    return method_fletcher_reeves
