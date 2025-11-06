

def add(num1, num2):
    x1, y1 = num1
    x2, y2 = num2

    res = [x1 + x2, y1 + y2]
    return res


def mul(num1, num2):
    x1, y1 = num1
    x2, y2 = num2

    res = [x1 * x2 - y1 * y2, x1 * y2 + y1 * x2]
    return res

def div(num1, num2):
    x1, y1 = num1
    x2, y2 = num2

    res = [x1 // x2, y1 // y2]
    return res


def main():
    res = [0, 0]
    # A = [25, 9]
    A=[152,52]

    # 3 cycles
    for i in range(3):
        res = mul(res, res)
        res = div(res, [10, 10])
        res = add(res, A)

    print(res)


if __name__ == "__main__":
    main()

