f = open ("intrare.in", "r")
sir = f.readline()
sir = sir[:-1]

nr_noduri = int(f.readline())

dict = {}
l = f.readline().split()
ct = -1
for ch in l:
    ct = ct + 1
    dict[ch] = ct

nr_finale = int(f.readline())
lst = []
lst = f.readline().split()
lst_finale = []
for x in lst:
    lst_finale.append(dict[x])

stare1 = []
stare2 = []
caracter = []
top = []
adauga = []
nr_tranzitii = 0

for x in f:
    l = x.split()
    stare1.append(dict[l[0]])
    stare2.append(dict[l[1]])
    caracter.append(l[2])
    top.append(l[3])
    adauga.append(l[5:])
    nr_tranzitii += 1


def verificareCuvant(nodCurent, cuvant, stiva2):
    stiva_noua = []
    if cuvant == "" and len(stiva2) == 0:
        return True
    elif cuvant == "" and nodCurent in lst_finale:
        return True
    else:
        for i in range(nr_tranzitii):
            if caracter[i] == 'lambda':
                if nodCurent == stare1[i] and top[i] == 'lambda':
                    aux = stiva2
                    if len(adauga[i]) > 1 or (len(adauga[i]) == 1 and adauga[i][0] != 'lambda'):
                        stiva_noua[:] = adauga[i]
                        stiva_noua.reverse()
                    else:
                        stiva_noua = []
                    stiva_noua = aux + stiva_noua
                    if verificareCuvant(stare2[i], cuvant, stiva_noua) == True:
                        return True

                if nodCurent == stare1[i] and stiva2[-1] == top[i]:
                    aux = stiva2[:-1]
                    if adauga[i] != ['lambda']:
                        stiva_noua[:] = adauga[i]
                        stiva_noua.reverse()
                    else:
                        stiva_noua = []
                    stiva_noua = aux + stiva_noua
                    if verificareCuvant(stare2[i], cuvant, stiva_noua) == True:
                        return True
            elif cuvant != "":
                if nodCurent == stare1[i] and cuvant[0] == caracter[i] and top[i] == 'lambda':
                    aux = stiva2
                    if adauga[i] != ['lambda']:
                        stiva_noua[:] = adauga[i]
                        stiva_noua.reverse()
                    else:
                        stiva_noua = []
                    stiva_noua = aux + stiva_noua
                    newstr = cuvant[1:]
                    if verificareCuvant(stare2, newstr, stiva_noua) == True:
                        return True

                if nodCurent == stare1[i] and cuvant[0] == caracter[i] and stiva2[-1] == top[i]:
                    aux = stiva2[:-1]
                    if adauga[i] != ['lambda']:
                        stiva_noua[:] = adauga[i]
                        stiva_noua.reverse()
                    else:
                        stiva_noua = []
                    stiva_noua = aux + stiva_noua
                    newstr = cuvant[1:]
                    if verificareCuvant(stare2[i], newstr, stiva_noua) == True:
                        return True
    return False


stiva = []

stiva.append("Z0")
start = 0

if verificareCuvant(start, sir, stiva) == True:
    print("Este acceptat")
else:
    print("Nu este acceptat")

'''
9
q0 q1 q2 q3 q4 q5 q6 q7 q8
1
q8
q0 q1 a Z0 / A Z0
q1 q0 a A / A
q0 q1 a A / A A
q0 q2 b A / lambda
q2 q2 b A / lambda
q2 q3 x Z0 / X Z0
q3 q3 x X / X X
q3 q4 2 X / X
q4 q5 3 X / X
q5 q6 y X / X X
q6 q6 y X / X X
q6 q7 z X / lambda
q7 q7 z X / lambda
q7 q8 lambda Z0 / lambda
'''