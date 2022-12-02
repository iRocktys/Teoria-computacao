from AFD import AFD
from AFN import AFN

def converte(afn):
    novoQ = geraQ(afn.Q, afn)
    novoS = afn.S
    novoq0 = [afn.q0]
    novoF = geraF(novoQ, afn)
    novoDelta = geraDelta(novoQ, afn)

    for i in range(len(novoQ)):
        novoQ[i] = str(novoQ[i]).replace('\'', '').replace(', ', ',')
    novoq0 = str(novoq0).replace('\'', '').replace(', ', ',')
    novoF = str(novoF).replace('\'', '').replace(', ', ',')

    matriz = []
    for i in range(len(novoDelta)):
        matriz.append(novoDelta[i].strip().split(' '))

    # acomodar novoDelta em formato de dicionario
    dic = {}
    for i in range(len(matriz)):
        dic[(matriz[i][0], matriz[i][1])] = matriz[i][2]

    afd = AFD('afd.txt',False)
    afd.Q = novoQ
    afd.S = novoS
    afd.q0 = novoq0
    afd.F = novoF
    afd.deltad = dic

    return afd


def conjunto(Q):
    conj = [[]]
    for i in Q:
        conj.extend([subConj + [i] for subConj in conj])
    return conj

def geraQ(Q, afn):
    aux = []
    aux2 = []
    conj = conjunto(Q)
    s = set()

    for i in range(1, len(conj)):
        for j in range(len(afn.S)):
            for k in range(len(conj[i])):
                aux += (afn.deltan[(conj[i][k], afn.S[j][0])])
        if len(aux) == 1:
            aux.pop()
        if [] not in aux:
            aux2.append((aux))
            aux = []

    aux2 = list(filter(None, aux2))
    junta = lambda lista, n: [lista[i:i + n] for i in range(0, len(lista), n)]
    for i in range(len(aux2)):
        aux2[i] = junta(aux2[i], len(afn.S))

    novoQ = []

    for i in range(len(aux2)):
        for j in range(len(aux2[i])):
            if aux2[i][j] not in novoQ:
                novoQ.append(aux2[i][j])

    return novoQ


def geraF(Q, afn):
    F = []
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            if Q[i][j] in afn.F:
                F += Q[i]
    return F


def geraDelta(Q, afn):
    d = set()
    aux = []
    aux2 = []
    for i in range(len(Q)):
        for j in range(len(afn.S)):
            for k in range(len(Q[i])):
                aux2 = afn.deltan[(Q[i][k], afn.S[j][0])]
                aux.append(aux2)

            d.add(str(Q[i]) + str(afn.S[j][0]) + str(aux))
            aux = []

    d = list(d)
    s = ''
    temp = []
    for i in range(len(d)):
        d[i] = list(filter(lambda x: x != '\'' and x != ',' and x != '[' and x != ']', d[i]))
        d[i] = list(filter(None, d[i]))
        for j in range(len(d[i])):
            if d[i][j] != ' ':
                s += d[i][j]

        temp.append(s)
        s = ''
    return formataDelta(temp)

def formataDelta(delta):
    entrada = []
    simbolo = []
    saida = []
    leuDigito = False
    j = 0
    d = []

    for i in range(len(delta)):
        while True:
            if j >= len(delta[i]):
                break

            car = delta[i][j]
            proxCar = delta[i][j + 1]

            if car.isdigit() and proxCar.isalpha():
                simbolo = car
                leuDigito = True
                j += 1

            if car.isalpha() and proxCar.isdigit():
                if leuDigito:
                    saida.append(car + proxCar)
                else:
                    entrada.append(car + proxCar)
                j += 2
        
        leuDigito = False
        j = 0
        d.append(str(entrada).replace('\'', '') + ' ' + str(simbolo) + ' ' + str(saida).replace('\'', ''))
        saida = []
        entrada = []

    for i in range(len(d)):
        d[i] = d[i].replace(', ', ',')
    return d