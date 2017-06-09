#----------------------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Adham Lucas da Silva Oliveira                 1715310001
# Jandinne Duarte de Oliveira                   1015070265
# Roberta de Oliveira da Cruz                   0825070169
# Nayara da Silva Cerdeira da Costa             1715310038
# Wesley da Silva Rocha                         1715310026 
#
# Escreva    um  aplicativo  para    simular     o   lançamento  de  dois    dados.  O   aplicativo 
# deve    utilizar    um  objeto  da  classe  Random  uma vez para    lançar  o   primeiro    dado    e   
# novamente    para    lançar  o   segundo     dado.   A   soma    dos     dois    valores     deve    então   ser    
# calculada.      Cada    dado    pode    mostrar um  valor   de  inteiro de  1   a   6,  portanto    a   soma    
# dos valores vai variar  de  2   a   12, com 7   sendo   a   soma    mais    freqüente   e   2   e   12  sendo   
# as   somas   menos   freqüentes.     A   figura  abaixo  mostra  as  36  possíveis   combinações    
# de   dois    dados.  Seu aplicativo  deve    lançar  o   dado    36  mil     vezes.  Utilize     um  array  
# unidimensional   para    contar o número  de  vezes   que     cada    possível    soma    aparece.   
# Exiba   os  resultados  em  formato tabular. 
#----------------------------------------------------------------------------------------------------------------------------------

from random import randint

matriz = [6*[0] for i in range(6)]
frequencia_soma = 11*[0]
qtd_lancamentos = 36000
for i in range(qtd_lancamentos):
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    matriz[dado1-1][dado2-1] += 1
    frequencia_soma[dado1+dado2-2] += 1
    
print(*frequencia_soma)
for linha in matriz:
    print(*linha)
