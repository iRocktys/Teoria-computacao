import AFN
import AFD

from Conversor import *

afn = AFN('afn.txt')
#afd = AFD('afd.txt',True)
afd = converte(afn)
afn.printAFN()
afd.printAFD()

while(1):
    # inserindo uma cadeia para testar no afn e no afd
    sequencia = input('Insira uma sequencia para o reconhecimento: ')

    # garantir que todos os caracteres pertencem ao alfabeto
    while((afd.verificaCadeiaAFD(sequencia) != True and afn.verificaCadeiaAFN(sequencia) != True)):
        print(' ')
        print('Cadeia inválida!')
        sequencia = input('Insira uma sequencia para o reconhecimento: ')
    print(' ')

    print('Cadeia a ser testada: ', sequencia)

    # mostrar o percorrimento da cadeia no afn
    print("Reconhecimento da cadeia no AFN\n")
    a = afn.verificaAFN(sequencia, afn.q0)
    # mostrar o percorrimento da cadeia no afd
    print("Reconhecimento da cadeia no AFD\n")
    b = afd.verificaAFD(sequencia, afd.q0)


    # veredito do reconhecimento da cadeia
    if a and b:
        print('\nA cadeia é reconhecida pelos automatos!\n')
    else:
        print('\nA cadeia nao é reconhecida pelos automatos!')
    print('--------------------------------------------------\n')