halving_method_iterations_list = []
halving_method_iterations_label = ['x', 'y', 'start_x', 'end_x', 'iter']

log_halving_method_iterations_list = []
log_halving_method_iterations_label = ['start_x', 'end_x', 'left', "center", 'right', 'iter']


def center_range(X):
    return X[0] + (X[1] - X[0]) / 2


def halving_method(f, start_x, end_x, epsilon=0.01, iter=500):
    halving_method_iterations_list.clear()

    def halving_method_inner(f, start_x, end_x, center, epsilon, iter):
        halving_method_iterations_list.append(
            [center[0], center[1], start_x, end_x, iter]
        )
        if abs(end_x - start_x) < epsilon or iter < 0:
            return center
        left_center_x = center_range([start_x, center[0]])
        right_center_x = center_range([center[0], end_x])

        left_center = [left_center_x, f(left_center_x)]
        right_center = [right_center_x, f(right_center_x)]

        if left_center[1] < center[1]:
            return halving_method_inner(f, start_x, center[0], left_center, epsilon, iter - 1)
        if center[1] > right_center[1]:
            return halving_method_inner(f, center[0], end_x, right_center, epsilon, iter - 1)
        if left_center[1] >= center[1] <= right_center[1]:
            return halving_method_inner(f, left_center[0], right_center[0], center, epsilon, iter - 1)
        raise ValueError('illegal argument exception')

    center_x = center_range([start_x, end_x])
    left_center_x = center_range([start_x, center_x])
    right_center_x = center_range([center_x, end_x])

    center = [center_x, f(center_x)]
    left_center = [left_center_x, f(left_center_x)]
    right_center = [right_center_x, f(right_center_x)]
    halving_method_iterations_list.append(
        [center[0], center[1], start_x, end_x, iter]
    )
    log_halving_method_iterations_list.append(
        [start_x, end_x, left_center, center, right_center, iter]
    )
    if left_center[1] < center[1]:
        return halving_method_inner(f, start_x, center[0], left_center, epsilon, iter - 1)
    if center[1] > right_center[1]:
        return halving_method_inner(f, center[0], end_x, right_center, epsilon, iter - 1)
    if left_center[1] >= center[1] <= right_center[1]:
        return halving_method_inner(f, left_center[0], right_center[0], center, epsilon, iter - 1)
    raise ValueError('illegal argument exception')
