#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058

# 47-  Sendo H = 1 - 1/2 + 1/3 - 1/4 + ... 1/n  faça um
# algoritmo em PORTUGOL para gerar o número H. O número N é lido do teclado.

n = float(input("valor de n: "))
i=float(1)
h=float(0)
while i<=n:
    if i % 2!=0:
        h+=1/i
    else:
        h-=1/i
    i+=1
print (h)

