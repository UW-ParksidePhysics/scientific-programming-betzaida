n = 10

sum_loop = 0
for i in range(1, n + 1):
    sum_loop += i

sum_formula = n * (n + 1) // 2

print(f"n = {n}")
print(f"sum(1, n) = {sum_loop}")
print(f"n(n+1)/2 = {sum_formula}")