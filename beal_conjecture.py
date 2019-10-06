

def beal(A, B, x, y, limit=100):
    Ax = A**x
    By = B**y

    for i in range(3, limit + 1):
        Cz = (Ax + By)**(1.0/i)
        print(Cz, i)
        if Cz % 1 == 0:
            print(f"{Ax} + {By} = {Cz}")


beal(312, 44, 42, 83)
