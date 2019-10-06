import math
# The big realization here was that the max possible factor of n can only be at most the sqrt of n!


def find_triangle_number():
    tri_nums = []
    for i in range(12000, 100000):
        tri_nums.append(triangle(i))
    return tri_nums


def triangle(num):
    summation = 0
    for k in range(0, num):
        summation += k
    return summation


def find_factors(r1, r2):
    individual_factor_list = []
    for k in range(r1, r2):
        m = triangle(k)
        for n in range(1, math.ceil(math.sqrt(m))):
            if (n < m) & (m % n == 0) & ((m / n) not in individual_factor_list):
                individual_factor_list.append(n)
                if (m / n) % 1 == 0:
                    individual_factor_list.append(int(m / n))
        if len(individual_factor_list) > 500:
            return individual_factor_list
        individual_factor_list = []


def main():

     print(find_factors(0, 100000))


main()

