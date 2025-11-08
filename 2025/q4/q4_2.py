from math import floor


def main():
    inp = """981
972
946
937
926
924
898
892
888
869
856
848
827
817
806
778
768
762
756
750
747
727
715
700
683
678
669
647
628
602
597
589
580
563
548
519
508
484
472
443
414
411
409
389
379
368
354
338
332
313""".split("\n")


    inp = list(map(int, inp))

    ans = 1
    for i in range(1, len(inp)):
        ans *= inp[i-1]/inp[i]

    print(ans)
    x = 10000000000000
    print(x/ans)

    





if __name__ == "__main__":
    main()
