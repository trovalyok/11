def is_integer(n):
    try:
        int()
        return True
    except Exception:
        return False


def numbers_of_cats_in_hats():
    n = input("Enter amount of cats: ")
    while not is_integer(n):
        n = input("Enter amount of cats: ")
    n = int(n)

    r = input("Enter amount of rounds: ")
    while not is_integer(r):
        r = input("Enter amount of rounds: ")
    r = int(r)

    a = []
    for i in range(n):
        a.append(0)

    for j in range(1, r+1):
        for i in range(n):
            if i % j == 0:
                if a[i]:
                    a[i] = 0
                else:
                    a[i] = 1

    res = []

    for i in range(n):
        if a[i]:
            res.append(i+1)

    return res


print(numbers_of_cats_in_hats())
