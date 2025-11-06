
inp = """Vorndra,Malthyris,Gavmarn,Valhynd,Silgonn,Jarxal,Pyrilor,Zraalvor,Morjoris,Iskarvash,Zarzris,Darrex,Nyhal,Caelaxis,Quirbel,Nynyn,Jalsyx,Tirzorin,Shaeleon,Wyrdaros

L12,R8,L8,R13,L15,R11,L12,R13,L12,R13,L5,R7,L5,R6,L5,R5,L5,R13,L5,R13,L16,R19,L12,R12,L5,R18,L18,R6,L17"""


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
            # pos = (pos - val) % max_edge - 1
            pos = max_edge - (((val - pos) % max_edge) - 1)
        else:
            pos -= val

    elif instr[0] == "R":
        if pos + val > max_edge:
            pos = (pos + val) % max_edge - 1
        else:
            pos += val

print(names[pos])
