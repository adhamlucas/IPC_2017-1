# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Hugo Thadeu Silva Cardoso          1715310013
# Luiz Paulo Machado                 1515200542
# Ian Gabriel Costa Machado          1215120276
# André Luis Laborda Neves           1515070006
# Gabriel de Queiroz Souza           1715310044
# João Vitor De Cordeiro B Gonçalves 1515140036
# Rodrigo Duarte de Souza            1115140049

# ----------------------------------------------------------
ang1 = int(input('Informe medida do primeiro ângulo: '))
ang2 = int(input('Informe medida do segundo ângulo: '))
tam = ang1 + ang2
if tam < 180:
    ang3 = (ang1 + ang2) - 180
    ang3 = ang3 * (-1)
    print('Medida do terceiro ângulo =', ang3)
else:
    print('Soma de ângulos acima de 180 graus. Não é triângulo equilátero')

