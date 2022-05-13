#import os

forca = ["____", "|       |",
         "|       ", "|      ", "|       "]


def desenho():
    for n in forca:
        print(n)


def palavra():
    p = input("Digite a palavra a ser descoberta!!!         ")
    p1 = [i for i in p]
    return p1


def dica():
    d = input("Digite a dica!!!   ")
    return d


def desenha_falado(p):
    s = "| "
    for x in p:
        s = s + x + " "
    print(s)


def verifica_letra(l, pa):
    dici = {}
    cont = 0
    l = l.lower()
    for i in pa:
        if l == i:
            dici[cont] = l
        cont += 1
    return dici


def joga():
    global forca
    erro = 0
    ganhou = True
    p = palavra()

    p_falado = []
    d = dica()

    print(d)
    t = len(p)
    print(p,t)
    for i in range(t):
        p_falado = p_falado + ["_"]

    desenho()
    desenha_falado(p_falado)
    while ganhou:
        l = input("digite uma letra:    ")
        dici1 = verifica_letra(l, p)
        if dici1 == {}:
            if erro == 0:
                forca[2] += "O"
                erro += 1
            elif erro == 1:
                forca[3] += "/"
                erro += 1
            elif erro == 2:
                forca[3] += "|"
                erro += 1
            elif erro == 3:
                forca[3] += "\\"
                erro += 1
            elif erro == 4:
                forca[4] += "/"
                erro += 1
            elif erro == 5:
                forca[4] += "\\"
                erro += 1
        else:
            for j in dici1:
                p_falado[j] = dici1[j]

        desenho()
        desenha_falado(p_falado)
        print(d)
        if p_falado == p:
            print("Vc ganhou!!!!")
            ganhou = False
        if erro == 6:
            print("Vc perdeu!!!!")
            ganhou = False


joga()
