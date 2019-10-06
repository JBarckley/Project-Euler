import math
steps = 0
prime_factor_list = []


def per(num):
    global steps
    sum = 1
    print(num)
    if num > 9:
        for i in str(num):
            sum *= int(i)
        steps += 1
        per(sum)
    else:
        print("STEPS:", steps)

def pFactorization(m):
    individual_factor_list = []
    global prime_factor_list
    for n in range(1, math.ceil(math.sqrt(m)) + 1):
        if (n <= m) & (m % n == 0) & ((m / n) not in individual_factor_list):
            individual_factor_list.append(n)
            if (m / n) % 1 == 0:
                individual_factor_list.append(int(m / n))
    if len(individual_factor_list) > 2:
        individual_factor_list.pop(0)
        individual_factor_list.pop(0)
        print(individual_factor_list, "INDIVID")
        print(prime_factor_list, "PRIME DEBUG 1")
        for i in individual_factor_list:
            print(i, "I")
            print(pFactorization(i), "pFACTOR I")
            print(prime_factor_list, "PRIME DEBUG 2")
            if pFactorization(i) != prime_factor_list:
                for k in pFactorization(i):
                    if k != 1:
                        prime_factor_list.append(k)
    else:
        return individual_factor_list
    return prime_factor_list


per(33322)
#print(pFactorization(8))
#print(pFactorization(3))
