# ---------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Lukas Michel Souza Mota               1715310018
# Marcus Viniciius Paes da Silva Santos 1515070060
# Matheus de Oliveira Marques           1515310514
# Natália Cavalcante Xavier             1715310021
# Nayara da Silva Cerdeira da Costa     1715310038
#
#52) Implementar um algoritmo em PORTUGOL para calcular o sen(X). O valor de X
#deverá ser digitado em graus. O valor do seno de X será calculado pela soma dos 15
#primeiros termos da série a seguir:
# senx= x-x^3/3!+x^5/5!...
#----------------------------------------------------------------------------------
                                       #Doação_do_grupo_07
x = float(input("Informe o grau: "))   #Doação_do_grupo_07
x = (x*3.1415926535)/180               #Doação_do_grupo_07
c = 1                                  #Doação_do_grupo_07 by: uaadc
senx = 0
m = 1

while c <= 14:
    i = 1
    fatorial = 1

    while i <= m:
        fatorial = fatorial * i
        i += 1
    senx = senx + (x ** m / fatorial) 
    c += 1
    m += 2
    senx = -senx
senx = 1-senx

print(senx)
