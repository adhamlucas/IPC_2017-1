
tabuada = int(input('Tabuada de: '))
inicio = int(input('Comeca: '))
fim = int(input('Fim: '))
c = 1
while c <= fim:
    produto = tabuada * inicio
    print('%.d X %.d = %.d' % (tabuada, inicio, produto))
    inicio += 1
    c += 1