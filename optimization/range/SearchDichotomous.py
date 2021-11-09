# -----------------------search_dichotomous--------------------------------------
search_method_dichotomous_iterations_list = []
search_method_dichotomous_iterations_label = ['x', 'y', 'start_x', 'end_x', "center_x", 'iter']


def search_dichotomous(f, start_x, end_x, epsilon=0.01, iter=500):
    search_method_dichotomous_iterations_list.clear()

    def search_method_dichotomous_inner(f, start_x, end_x, epsilon, iter):
        center_x = start_x + (end_x - start_x) / 2
        search_method_dichotomous_iterations_list.append(
            [center_x, f(center_x), start_x, end_x, center_x, iter]
        )
        if abs(end_x - start_x) < epsilon or iter < 0:
            return [start_x, end_x]
        else:
            center_x = start_x + (end_x - start_x) / 2
            left_x = center_x - epsilon / 2.1
            right_x = center_x + epsilon / 2.1
            if f(left_x) < f(right_x):
                return search_method_dichotomous_inner(f, start_x, right_x, epsilon, iter - 1)
            else:
                return search_method_dichotomous_inner(f, left_x, end_x, epsilon, iter - 1)

    return search_method_dichotomous_inner(f, start_x, end_x, epsilon, iter)
