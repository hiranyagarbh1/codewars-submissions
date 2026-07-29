def regression_line(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
​
    denominator = n * sum_x2 - sum_x ** 2
​
    a = (sum_x2 * sum_y - sum_x * sum_xy) / denominator
    b = (n * sum_xy - sum_x * sum_y) / denominator
​
    return (round(a, 4), round(b, 4))
​