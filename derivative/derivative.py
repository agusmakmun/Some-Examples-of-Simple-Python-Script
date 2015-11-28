"""Derivative or Turunan, eg output:
>>> Masukkan Bilangan, (eg: 4x^3-3x^2+2x-45). __>> 4x^3-3x^2+2x-45
Solved COY:  12x^2+6x-2
>>> Masukkan Bilangan, (eg: 4x^3-3x^2+2x-45). __>> 6x^2+2+2x
Solved COY:  12x+2
>>> Masukkan Bilangan, (eg: 4x^3-3x^2+2x-45). __>> 7x-10x^2-3
Solved COY:  7-20x
"""

"""Comprehension"""
x = 2
a = 4*x**3
b = 3*x**2
c = 2*x
d = 45
_all = a-b+c-d

"""Implementation"""
def Turunan(inputan):
    import operator, re
    """Sengaja dibuat dict, agar apabila nantinya diperlukan dapat mudah memanggilnya dengan variable yg sama"""
    op = {'+':operator.add,
          '-':operator.sub,
          '*':operator.mul,
          '^':operator.pow,
          '/':operator.div
          }

    #inputan    = "4x^3-3x^2+2x-45"
    #inputan     = "6x^2+2+2x"

    split_all   = re.split(r'(\+|-|)\s*', inputan)

    tmp = []
    for opsm in split_all:
        if opsm in op.keys():
            tmp.append(opsm)

    tmp = tmp
    out = []
    count = 0
    for item in split_all:
        if "x" not in item:
            out = out
        else:
            count += 1
            get_x = item.split("x")[0]
            get_pangkat = item.split("^")
            
            pangkat  = ""
            try:
                pangkat = get_pangkat[1]
            except IndexError:
                pangkat  = "1"
            pkt = "x^" + str(int(pangkat)-1)
            if pkt == "x^1":
                pkt = "x"
            elif pkt == "x^0":
                pkt = ""
            else:
                pkt = pkt

            goal = str(int(get_x)*int(pangkat)) + pkt
            if "x" in goal:
                try:
                    goal = goal+tmp[count]
                except IndexError:
                    goal = tmp[count-1]+goal
                        
            elif "x" not in goal:
                goal = goal
            out.append(goal)

    print "Solved COY: ", "".join(out)


while True:
    inputan = raw_input("Masukkan Bilangan, (eg: 4x^3-3x^2+2x-45). __>> ")
    Turunan(inputan)
