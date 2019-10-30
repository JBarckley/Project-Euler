# Find an approximation for the sum of the infinite series of 1/k^3
def k3():
    total = 0
    for i in range(1, 100000):
        total += (1 / pow(i, 3))
    return total

# Finds a divisor which approximately divides the sum of the infinite series of 1/k^3 evenly
def find_divisor(series_sum):
    for i in range(3, 1000):
        if series_sum % (i / 1000) < 0.0001:
            print(i / 1000)
            print(total / (i / 1000))


# Examines strictly the odd component of 1/k^3
def odd():
    total = 0;
    for i in range(0, 100000):
        total += (1 / pow((2*i + 1), 3))
    return total


# Examines strictly the even component of 1/k^3
def even():
    total = 0
    for i in range(1, 100000):
        total += (1 / pow((2*i), 3))
    return total


total = k3()
print(total)
find_divisor(total)
print(odd())
print(even())
print(odd() + even())

# Did you know mathematicians don't know the value of the infinite sum of 1/k^3?
# This program approximates such sum, where the error is negligible.
# From this program I found that .601 is approximately 1/2 of the infinite sum of 1/k^3!
