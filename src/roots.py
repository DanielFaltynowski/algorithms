from calculus import derivative

def approximation_method(f, a, b, epsilon=0.01):
    if epsilon < 0:
        epsilon = -epsilon
    ans = a
    while ans <= b:
        if -epsilon <= f(ans) <= epsilon:
            return ans
        ans = ans + epsilon


def bisection_method(f, a, b, epsilon=0.0001):
    if epsilon < 0:
        epsilon = -epsilon
    if a > b:
        temp = a
        a = b
        b = temp
    ans = (a + b) / 2
    while f(ans) > epsilon or f(ans) < -epsilon:
        if f(ans) > 0:
            if f(a) > 0:
                a = ans
            else:
                b = ans
        if f(ans) < 0:
            if f(a) > 0:
                b = ans
            else:
                a = ans
        ans = (a + b) / 2
    return ans

def newton_raphson_method(f, x_0, epsilon=0.0001):
    if epsilon < 0:
        epsilon = -epsilon
    ans = x_0
    while f(ans) > epsilon or f(ans) < -epsilon:
        ans = ans - (f(ans) / derivative(f, ans))
    return ans


if __name__ == '__main__':
    def f(x):
        return (x ** 2) - 49

    print(f'Approximation Method: {approximation_method(f, 0, 10)}')
    print(f'Bisection Method: {bisection_method(f, 0, 10)}')
    print(f'Newton-Raphson Method: {newton_raphson_method(f, 1)}')