# golden_section = ((5 ** (0.5) + 1) / 2)
#
# search_golden_section_iterations_list = []
# search_golden_section_iterations_label = ['x', 'y', 'start_x', 'end_x', 'iter']
#
# log_search_golden_section_iterations_list = []
# log_search_golden_section_iterations_label = ['start_x', 'end_x', 'left', "center", 'right', 'iter']
#
#
# def search_golden_section(f, start_x, end_x, epsilon=0.01, iter=500):
#     search_golden_section_iterations_list.clear()
#     log_search_golden_section_iterations_list.clear()
#
#     def search_golden_section_inner(f, start_x, end_x, left, right, epsilon, iter):
#         search_golden_section_iterations_list.append(
#             [(end_x + start_x) / 2, f((end_x + start_x) / 2), start_x, end_x, iter]
#         )
#         log_search_golden_section_iterations_list.append(
#             [(end_x + start_x) / 2, f((end_x + start_x) / 2), start_x, end_x, left, right, iter]
#         )
#         if abs(end_x - start_x) < epsilon or iter < 0:
#             return [(end_x + start_x) / 2, f((end_x + start_x) / 2)]
#         if left is None:
#             left_x = start_x + end_x - right[0]
#             left = [left_x, f(left_x)]
#         if right is None:
#             right_x = start_x + end_x - right[0]
#             right = [right_x, f(right_x)]
#
#         # return
#         if left[1] < right[1]:
#             return search_golden_section_inner(f, start_x, right[0], None, left, epsilon, iter - 1)
#         else:
#             return search_golden_section_inner(f, left[0], end_x, right, None, epsilon, iter - 1)
#
#     left_x = start_x - (end_x - start_x) / golden_section
#     right_x = start_x + (end_x - start_x) / golden_section
#
#     left = [left_x, f(left_x)]
#     right = [right_x, f(right_x)]
#
#     if left[1] < right[1]:
#         return search_golden_section_inner(f, start_x, right_x, None, left, epsilon, iter - 1)
#     else:
#         return search_golden_section_inner(f, left_x, end_x, right, None, epsilon, iter - 1)
golden_section = ((5 ** (0.5) + 1) / 2)

search_golden_section_iterations_list = []
search_golden_section_iterations_label = ['x', 'y', 'start_x', 'end_x', 'iter']

log_search_golden_section_iterations_list = []
log_search_golden_section_iterations_label = ['start_x', 'end_x', 'left', "center", 'right', 'iter']


def search_golden_section(f, start_x, end_x, epsilon=0.001, iter=500):
    search_golden_section_iterations_list.clear()

    def search_golden_section_inner(f, start_x, end_x, left, right, epsilon, iter):
        search_golden_section_iterations_list.append(
            [(end_x + start_x) / 2, f((end_x + start_x) / 2), start_x, end_x, iter]
        )
        if abs(end_x - start_x) < epsilon or iter < 0:
            return [start_x,end_x]#[(end_x + start_x) / 2, f((end_x + start_x) / 2)]
        if left is None:
            left_x = end_x - (end_x - start_x) / golden_section
            left = [left_x, f(left_x)]
        if right is None:
            right_x = start_x + (end_x - start_x) / golden_section
            right = [right_x, f(right_x)]
        log_search_golden_section_iterations_list.append(
            [start_x, end_x, left, right, epsilon, iter]
        )
        if left[1] < right[1]:
            return search_golden_section_inner(f, start_x, right[0], None, left, epsilon, iter - 1)
        else:
            return search_golden_section_inner(f, left[0], end_x, right, None, epsilon, iter - 1)

    left_x = end_x - (end_x - start_x) / golden_section
    right_x = start_x + (end_x - start_x) / golden_section

    left = [left_x, f(left_x)]
    right = [right_x, f(right_x)]
    search_golden_section_iterations_list.append(
        [(end_x + start_x) / 2, f((end_x + start_x) / 2), start_x, end_x, iter]
    )
    if abs(left[1]) < abs(right[1]):
        return search_golden_section_inner(f, start_x, right_x, None, left, epsilon, iter - 1)
    else:
        return search_golden_section_inner(f, left_x, end_x, right, None, epsilon, iter - 1)

# %%
