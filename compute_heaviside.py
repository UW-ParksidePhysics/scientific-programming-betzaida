def compute_heaviside(position):
    """
    Compute the Heaviside step function H(x).
    Returns 0 if x < 0 and 1 if x >= 0.
    """
    if position < 0:
        return 0
    else:
        return 1

def test_heaviside():
    """
    Test the Heaviside function with various values.
    """
    test_values = [-10, -10 - 15, 0, 10 - 15, 10]
    expected_results = [0, 0, 1, 0, 1]

    print("Testing Heaviside Function:")
    for i in range(len(test_values)):
        result = compute_heaviside(test_values[i])
        print("H(" + str(test_values[i]) + ") = " + str(result) + ", Expected: " + str(expected_results[i]))
        assert result == expected_results[i], "Test failed for H(" + str(test_values[i]) + ")"

if __name__ == "__main__":
    test_heaviside()