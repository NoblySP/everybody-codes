
inp = """Aeorzryn,Agnarlith,Qalpyr,Lithpyr,Zyrrilor,Fenvash,Kharath,Orahgarath,Brelix,Wyrrex

L6,R9,L7,R7,L1,R6,L2,R5,L1,R9,L3"""

inp = inp.split("\n")

names = inp[0].split(",")
lst = inp[-1].split(",")

max_edge = len(names) - 1

pos = 0
for instr in lst:
    # print(pos)
    # print(names[pos])
    val = int(instr[1:])

    if instr[0] == "L":
        if pos - val < 0:
            pos = 0
        else:
            pos -= val

    elif instr[0] == "R":
        if pos + val > max_edge:
            pos = max_edge
        else:
            pos += val

print(names[pos])
