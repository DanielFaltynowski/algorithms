def derivative(f, x, h=0.0001):
        return (f(x + h) - f(x)) / h