# Basic variables
num_1 = 13
num_2 = 24

# Arithmetic operations
print("Sum:", num_1 + num_2)
print("Difference:", num_1 - num_2)
print("Division:", num_2 / num_1)
print("Integer Division:", num_2 // num_1)
print("Modulo:", num_2 % num_1)
print("Power:", num_1 ** 2)

# Comparisons
x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# Simple function
def difference_ratio(a, b):
    bigger = max(a, b)
    smaller = min(a, b)
    return (bigger - smaller) / smaller

result = difference_ratio(24, 14)
print("Difference ratio:", result)
