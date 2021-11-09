import numpy as np

threePointQuadratic_list = []
threePointQuadratic_label = ['x', 'y', 'iter']


def cubicInterpolation(f, points, epsilon=0.01, iter=500):
    matrix = []
    for (x, y) in points:
        matrix.append([x ** 3, x ** 2, x, y])
    solve = np.linalg.solve(np.array(matrix))
    return 5