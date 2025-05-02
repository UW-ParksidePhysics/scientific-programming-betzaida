import math

def gaussian(position):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position ** 2)

if __name__ == '__main__':
    n_points = 41
    start = -4
    end = 4
    step = (end - start) / (n_points - 1)

    positions = []
    gaussian_values = []

    for i in range(n_points):
        x = start + i * step
        positions.append(x)
        gaussian_values.append(gaussian(x))

print("First 5 positions and corresponding Gaussian values:")
for i in range(5):
    print(f"x = {positions[i]:.2f}, g(x) = {gaussian_values[i]:.5f}")
