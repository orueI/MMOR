# --------------------------method_sven--------------------------------------
method_sven_iterations_list = []


def method_sven(x0: float, h: float, f, n: int = 200):
    method_sven_iterations_list.clear()
    method_sven_iterations_list.append(
        [x0, f(x0), h]
    )

    def inner_method_sven(x0: float, h: float, f, n: int = 200):
        x1 = x0 + h
        f0 = f(x0)
        f1 = f(x1)
        method_sven_iterations_list.append([x1, f1, h])
        if f1 < f0:
            return inner_method_sven(x1, h * 2, f, n)
        else:
            return [x0, x1]

    x1 = x0 + h
    f0 = f(x0)
    f1 = f(x1)
    method_sven_iterations_list.append([x1, f1, h])
    if f1 < f0:
        return inner_method_sven(x0, h * 2, f, n - 1)
    else:
        return inner_method_sven(x0, h * -1, f, n - 1)
