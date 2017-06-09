#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Nayara da Silva Cerdeira da Costa     1715310038
# Joelson Pereira Lima 			        1715310060
# Ian Gabriel Costa Machado             1215120276
#
#7.(MAT 88) Dada uma seqüência de n números reais, determinar os números que compõem a seqüência e o número de vezes
#que cada um deles ocorre na mesma.
#
#Exemplo: n = 8
#Seqüência: -1.7,  3.0,  0.0,  1.5,  0.0, -1.7,  2.3, -1,7
#
#Saída:                
#-1.7 ocorre 3 vezes
# 3.0 ocorre 1 vez
# 0.0 ocorre 2 vezes
# 1.5 ocorre 1 vez
# 2.3 ocorre 1 vez
#----------------------------------------------------------------------------------------------------------------------

sequence = input().split()
size = len(sequence)
times = []
used_numbers = []
repetitions = 0
c = 0

while c < size:
    if sequence[c] not in used_numbers:
        for i in sequence[:]:
            if float(sequence[c]) == float (i):
                repetitions += 1
        used_numbers += [sequence[c]]
        times += [repetitions]

    c += 1
    repetitions = 0

c = 0

while c < len(times):
    if times[c] > 1:
        print(used_numbers[c],"ocorre",times[c],"Vezes")
    
    else:
        print(used_numbers[c],"ocorre",times[c],"Vez")
    c += 1

