from math import floor


def main():
    inp = """1000
977
966
959
957
934
915
893
890
873
871
855
827
825
803
774
764
741
713
692
671
653
652
641
614
610
600
588
566
541
536
512
484
468
441
425
423
410
388
363
342
328
327
301
293
289
260
233
224
200""".split("\n")


    inp = list(map(int, inp))

    ans = 1
    for i in range(1, len(inp)):
        ratio = inp[i-1]/inp[i]
        print(ans)
        ans *= ratio

    print(ans)
    print(2025*ans)

    





if __name__ == "__main__":
    main()
