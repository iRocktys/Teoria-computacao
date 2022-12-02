import AFN
import AFD

from Conversor import *

afn = AFN('afn.txt')
afn.printAFN()
#afd = AFD('afd.txt',True)
afd = converte(afn)
afn.printAFN()
afd.printAFD()

while(1):
    # inserindo uma cadeia para testar no afn e no afd
    sequencia = input('\033[1;34mInsira uma sequencia para o reconhecimento:\033[0;0m')

    # garantir que todos os caracteres pertencem ao alfabeto
    while((afd.verificaCadeiaAFD(sequencia) != True and afn.verificaCadeiaAFN(sequencia) != True)):
        print(' ')
        print('\033[1;34mCadeia inválida!\033[0;0m')
        sequencia = input('\033[1;34mInsira uma sequencia para o reconhecimento:\033[0;0m')
    print(' ')

    print('\n\033[1;34mCadeia a ser testada: \033[0;0m',sequencia,'\n')

    # mostrar o percorrimento da cadeia no afn
    print("\n\033[1;34mReconhecimento da cadeia no AFN\033[0;0m\n")
    a = afn.verificaAFN(sequencia, afn.q0)
    # mostrar o percorrimento da cadeia no afd
    print("\n\033[1;34mReconhecimento da cadeia no AFD\033[0;0m\n")
    b = afd.verificaAFD(sequencia, afd.q0)


    # veredito do reconhecimento da cadeia
    if a and b:
        print('\n\033[1;92mA cadeia é reconhecida pelos automatos!\033[0;0m\n')
    else:
        print('\n\033[1;91mA cadeia nao é reconhecida pelos automatos!\033[0;0m\n')
    print('--------------------------------------------------\n')