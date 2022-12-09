class AFD:
    def __init__(self, nomeArquivo, permisaoLeitura):
        # Se a leitura do arquivo = TRUE
        if(permisaoLeitura == True):
            # Faz a abertura do arquivo, com nome designado na main
            arq = open(nomeArquivo, 'r')
            # Faz a leitura dos estados iniciais e finais, transicoes
            self.Q = arq.readline().strip().split(' ')
            self.S = arq.readline().strip().split(' ')
            self.q0 = str(arq.readline()).strip()
            self.F = arq.readline().strip().split(' ')
            self.transicoes = arq.readlines()
            # Fecha o arquivo
            arq.close()

            matriz = []

            for i in range(len(self.transicoes)):
                matriz.append(self.transicoes[i].strip().split())
            self.deltad = {}
            for k in range(len(matriz)):
                self.deltad[(matriz[k][0], matriz[k][1])] = matriz[k][2]
        else:
            # Se nao e para fazer a leitra, deixa todas as listas vazias
            self.Q = []
            self.S = []
            self.q0 = []
            self.F = []
            self.deltad = {}

    def pertence(self, carac):
        if carac in self.S:
            return True
        return False

    def verificaCadeiaAFD(self, seq):
        for i in seq:
            if(self.pertence(i) == False):
                return False
        return True


    def verificaAFD(self, seq, estado):
        if seq == '':
            return estado in self.F

        else:
            proxcaract = seq[0]
            dupla = (estado, proxcaract)
            print(dupla, ' -> ', self.deltad[(dupla)])
            if dupla in self.deltad:
                return self.verificaAFD(seq[1:], self.deltad[dupla])
            else:
                return False


    def printAFD(self):
        print('\n\n----------AUTOMATO FINITO DETERMINISTICO----------\n')
        print('Estados: ', self.Q)
        print('Estado inicial: ', self.q0)
        print('Estados finais: ', self.F)
        print('Transições:')
        print('(Estado atual, Simbolo) -> Estado resultante\n')
        for i in self.deltad:
            print(i,' -> ',self.deltad[i])
        print('\n--------------------------------------------------\n')