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

    res = [int(x1 / x2), int(y1 / y2)]
    return res


def main():

    A=[35300,-64910]
    A=[-4531,-68892]
    opp_corner = add(A, [1000, 1000])

    count = 0
    points_lst = []
    for x in range(A[0], opp_corner[0] + 1, (opp_corner[0]-A[0])//1000):
        for y in range(A[1], opp_corner[1] + 1, (opp_corner[1]-A[1])//1000):
            points_lst.append([x, y])
    print(len(points_lst))

    
    for point in points_lst:
        x, y = point
        res = [0, 0]
        # 100 cycles
        for i in range(100):
            res = mul(res, res)
            res = div(res, [100_000,100_000])
            res = add(res, [x, y])

            if -1_000_000 <= res[0] <= 1_000_000 and -1_000_000 <= res[1] <= 1_000_000:
                continue
            else:
                break
        else:
            # print([x, y], res)
            count += 1  # Engrave point
    



    print(count)


if __name__ == "__main__":
    main()

