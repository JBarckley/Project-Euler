
def tensdigit(n):
    ten = 3
    twenty = 6
    thirty = 6
    forty = 5
    fifty = 5
    sixty = 5
    seventy = 7
    eighty = 6
    ninety = 6

    digit = {
        1: ten,
        2: twenty,
        3: thirty,
        4: forty,
        5: fifty,
        6: sixty,
        7: seventy,
        8: eighty,
        9: ninety
    }

    return digit.get(n, "")


def onesdigit(n):
    one = 3
    two = 3
    three = 5
    four = 4
    five = 4
    six = 3
    seven = 5
    eight = 5
    nine = 4

    digit = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine
    }

    return digit.get(n, "")


def teenagers(n):
    ten = 3
    eleven = 6
    twelve = 6
    thirteen = 8
    fourteen = 8
    fifteen = 7
    sixteen = 7
    seventeen = 9
    eighteen = 8
    nineteen = 8

    digit = {
        0: ten,
        1: eleven,
        2: twelve,
        3: thirteen,
        4: fourteen,
        5: fifteen,
        6: sixteen,
        7: seventeen,
        8: eighteen,
        9: nineteen
    }

    return digit.get(n, "")

def amt(num):
    ttl = 0

    if int(num[0]) != 0 and int(num[0]) != 1:
        ttl += tensdigit(int(num[0]))
    elif int(num[0]) == 1:
        ttl += teenagers(int(num[1]))

    if int(num[1]) != 0 and int(num[0]) != 1:
        ttl += onesdigit(int(num[1]))
    return ttl


def countnumbers():
    summation = 0
    hundred = 7
    _and = 3

    # 1 - 9
    for m in range(1, 10):
        summation += onesdigit(m)
        print(m, summation)

    #summation += 70  10 - 19
    for f in range(10, 20):
        summation += teenagers(int(str(f)[1]))
        print(f, summation)

    # 20 - 1000
    for k in range(20, 1001):
        if len(str(k)) < 3:
            if int(str(k)[1]) != 0:
                summation += onesdigit(int(str(k)[1]))
            summation += tensdigit(int(str(k)[0]))
        else:
            summation += onesdigit(int(str(k)[0]))
            summation += hundred
            summation += _and
            summation += amt(str(k)[1:])
        print(summation, k)


countnumbers()
