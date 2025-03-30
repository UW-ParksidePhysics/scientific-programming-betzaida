import numpy as np

def calculate_difference_quotient(function, position, interval=0.01):
    """
    Approximate the derivate of a function using the difference quotient formula.
    f'(x) ≈ (f(x + h) - f(x - h)) / (2h)
    """
    return (function(position + interval) - function(position - interval)) / (2 * interval)

def test_difference_quotient():
    """
    Verify that the difference quotient gives an exact result for a quadratic function.
    """
    f = lambda x: x**2
    exact_derivative = lambda x: 2 * x
    x_test = 3
    computed_derivative = calculate_difference_quotient(f, x_test)
    error = abs(computed_derivative - exact_derivative(x_test))
    print("Test for quadratic function: Error =", error)

def run_test():
    """
    Run test cases for different functions.
    """
    functions = [
        (lambda x: np.exp(x), 0, 1),
        (lambda x: np.exp(-2 * x**2), 0, 0),
        (lambda x: np.cos(x), 2 * np.pi, 0),
        (lambda x: np.log(x), 1, 1)
    ]

    for func, pos, exact_derivative in functions:
        approx_derivative = calculate_difference_quotient(func, pos)
        error = abs(approx_derivative - exact_derivative)
        print("f(x) at x =", pos, " -> Approx Derivative:", round(approx_derivative, 5),
              "| Exact Derivative:", exact_derivative, "| Error:", round(error, 5))

if __name__ == '__main__':
    test_difference_quotient()
    print("\nRunning differentiation test:")
    run_test()