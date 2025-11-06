
inp = """Valkryth,Tireldrin,Axallorath,Calynn,Urzorin,Krynnnylor,Zyrixxeth,Tarlfelix,Sylvyr,Glynnkyris,Zarathfyr,Vyrdravor,Ilmarvalir,Havwyris,Brythsor,Cynvargnaris,Urral,Talketh,Eadelor,Tarlmyr,Thyroscarth,Agnarasis,Voraxidris,Balbel,Lazcarth,Jaercoryx,Galfarin,Xyrsor,Glaurcarth,Wynwyris

L35,R45,L33,R38,L6,R45,L42,R9,L32,R26,L19,R43,L30,R13,L48,R25,L25,R41,L31,R29,L5,R39,L5,R6,L5,R15,L5,R28,L5,R7,L5,R20,L5,R46,L5,R25,L5,R24,L5,R6,L29,R17,L44,R33,L44,R15,L23,R19,L45,R30,L14,R7,L8,R46,L12,R8,L26,R8,L42"""

# inp = """Vyrdax,Drakzyph,Fyrryn,Elarzris
# 
# R3,L2,R3,L3"""

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
            # pos = max_edge - (((val - pos) % max_edge) - 1)
            neg_idx = -((val - pos) % (max_edge+1))
            pos = max_edge + neg_idx + 1
        else:
            pos -= val

    elif instr[0] == "R":
        if pos + val > max_edge:
            pos = (pos + val) % max_edge - 1
        else:
            pos += val

    # swap(names[pos], names[0])
    tmp = names[0]
    names[0] = names[pos]
    names[pos] = names[0]

print(names[pos])
