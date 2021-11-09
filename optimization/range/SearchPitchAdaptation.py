search_pitch_adaptation_iterations_list = []
search_pitch_adaptation_iterations_label = ['x', 'y', 'step', 'step_coef', 'iter']


# log_search_golden_section_iterations_list = []
# log_search_golden_section_iterations_label = ['start_x', 'end_x', 'left', "center", 'right', 'iter']


def search_pitch_adaptation(f, start_x, step, epsilon=0.1, iter=500):
    search_pitch_adaptation_iterations_list.clear()

    def next_step_coef(coef, Y):
        if Y[1] < Y[0] and coef >= 0.5:
            return 2
        if Y[1] < Y[0] and coef < 0.5:
            return 0.5
        if Y[1] >= Y[0] and coef == 2:
            return 0.25
        if Y[1] >= Y[0] and coef != 2:
            return -0.5

    def search_pitch_adaptation_inner(f, start, step, step_coef, epsilon, iter):
        search_pitch_adaptation_iterations_list.append(
            [start[0], start[1], step, step_coef, iter]
        )
        if abs(step) < epsilon or iter < 0:
            return start

        next_x = start[0] + step
        next = [next_x, f(next_x)]

        next_sc = next_step_coef(step_coef, [start[1], next[1]])

        if next[1] < start[1]:
            return search_pitch_adaptation_inner(f, next, step * next_sc, next_sc, epsilon, iter - 1)
        else:
            return search_pitch_adaptation_inner(f, start, step * next_sc, next_sc, epsilon, iter - 1)

    return search_pitch_adaptation_inner(f, [start_x, f(start_x)], step, 0, epsilon, iter - 1)
# %%
