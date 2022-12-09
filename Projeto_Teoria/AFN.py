class AFN:
    def __init__(self, nomeArquivo):
        arq = open(nomeArquivo, 'r')
        self.Q = arq.readline().strip().split(' ')
        self.S = arq.readline().strip().split(' ')
        self.q0 = str(arq.readline()).strip()
        self.F = arq.readline().strip().split(' ')
        self.transicoes = arq.readlines()
        arq.close()

        matriz = []
        for i in range(len(self.transicoes)):
            matriz.append(self.transicoes[i].strip().split())
        self.deltan: dict = {}
        for k in range(len(matriz)):
            if (matriz[k][2] == '[]'):
                self.deltan[(matriz[k][0], matriz[k][1])] = []
            else:
                if (len(matriz[k]) == 3):
                    self.deltan[(matriz[k][0], matriz[k][1])] = [matriz[k][2]]
                else:
                    aux = matriz[k]
                    aux = aux[2:]
                    self.deltan[(matriz[k][0], matriz[k][1])] = aux

    def pertence(self, carac):
        if carac in self.S:
            return True
        return False

    def verificaCadeiraAFN(self, sequencia):
        for i in sequencia:
            if(self.pertence(i) == False):
                return False
        return True

    def verificaAFN(self, sequencia, estadoatual):
        if sequencia == '':
            return estadoatual in self.F
        proxseq = sequencia[0]
        checaestado = (estadoatual, proxseq)
        print(checaestado, ' -> ', end='')
        if checaestado in self.deltan:
            proxest = self.deltan[checaestado]
            for est in proxest:
                if (est not in proxest[0]):
                    print('Backtracking!')
                    print(checaestado, ' -> ', end='') 
                print(est)
                if self.verificaAFN(sequencia[1:], est):
                    return True
        return False

    def printAFN(self):
        print('\n\n--------AUTOMATO FINITO NAO DETERMINISTICO--------\n')
        print('Estados: ',self.Q)
        print('Estado inicial: ',self.q0)
        print('Estados finais: ',self.F)
        print('Transições:')
        print('(Estado atual, Simbolo) -> Estados resultantes\n')
        for i in self.deltan:
            print(i,' -> ',self.deltan[i])