threePointQuadratic_list = []
threePointQuadratic_label = ['x', 'y', 'iter']


def threePointQuadratic(f, start, end, center, epsilon=0.01, iter=500):
    def p(start, end, center):
        return (center[0] - start[0]) * (end[1] - center[1])

    def q(start, end, center):
        return (end[0] - center[0]) * (start[1] - center[1])

    def min(point1, point2, e=0):
        if point1[e] < point2[e]:
            return point1
        else:
            return point2

    def max(point1, point2, e=0):
        if point1[e] > point2[e]:
            return point1
        else:
            return point2

    def threePointQuadratic_inner(f, start, end, center, epsilon, iter):
        threePointQuadratic_list.append([center[0], center[1], iter])
        new_center_x = (p(start, end, center) * (center[0] + start[0]) + q(start, end, center) * (
                end[0] + center[0])) \
                       / (2 * (p(start, end, center) + q(start, end, center)))
        new_center = [new_center_x, f(new_center_x)]
        if new_center[0] < start[0] < end[0] < new_center[0]:
            return center

        if abs(center[0] - new_center[0]) or iter < 0:
            if center[1] < new_center[1]:
                return center
            else:
                return new_center
        if center[1] < new_center[1]:
            return threePointQuadratic_inner(f, min(start, new_center), max(end, center), center, epsilon, iter - 1)
        else:
            return threePointQuadratic_inner(f, start, end, new_center, epsilon, iter - 1)

    res = threePointQuadratic_inner(f, start, end, center, epsilon, iter - 1)
    threePointQuadratic_list.append([res[0], res[1], 0])
    return res
