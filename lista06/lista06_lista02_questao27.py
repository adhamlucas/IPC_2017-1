#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcante Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Uma grande firma deseja saber quais os três empregados mais recentes. Fazer um
# algoritmo em PORTUGOL para ler um número indeterminado de informações
# (máximo de 300) contendo o número do empregado e o número de meses de trabalho
# deste empregado e imprimir os três mais recentes.
# Observações: A última informação contém os dois números iguais a zero. Não existem
# dois empregados admitidos no mesmo mês.
#---------------------------------------------------------------------------

i = 0
fim = 0
empregados = []
meses = []
recente = []
empregrec = []

while fim == 0:
    
    numempre = int(input())
    mes = int(input())
    
    if numempre != 0 and mes != 0:
        
        empregados.append(numempre)
        meses.append(mes)
        
        if i < 3:
            
            recente.append(mes)
            empregrec.append(numempre)
            
        else:
            
            if mes < recente[0]:
                
                recente[0] = mes
                empregrec[0] = numempre
                
            else:
                
                if mes < recente[1]:
                
                    recente[1] = mes
                    empregrec[1] = numempre
                    
                else:
                    
                    if mes < recente[2]:
                
                        recente[2] = mes
                        empregrec[2] = numempre
    
    else:
        
        fim = 1
        
    i += 1
    
    if i == 300:
        
        fim = 1
        
print("empregados mais recentes:")
print("empregado de número", empregrec[0], ", por ", recente[0], "meses")
print("empregado de número", empregrec[1], ", por ", recente[1], "meses")
print("empregado de número", empregrec[2], ", por ", recente[2], "meses")
