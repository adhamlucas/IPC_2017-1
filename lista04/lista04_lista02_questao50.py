# ---------------------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de souza Barbosa   1315120206
#
# Leia um número inteiro que representa um código de DDD para discagem interurbana.
# Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:
#
#     DDD    DESTINATION
#     61     Brasília
#     71     São Paulo
#     11     Salvador
#     21     Rio de Janeiro
#     32     Juiz de Fora
#     19     Campinas
#     27     Vitoria
#     31     Belo Horizonte
# 
# Se a entrada for qualquer outro DDD que não esteja presente na tabela acima,
# o programa deverá informar: DDD nao cadastrado
# ---------------------------------------------------------------------------------------------------------------------------------

number = int(input("Insira o DDD: "))
if number == 61:
    print("Brasilia")
elif number == 71:
    print("Salvador")
elif number == 11:
    print("São Paulo")
elif number == 21:
    print("Rio de Janeiro")
elif number == 32:
    print("Juiz de Fora")
elif number == 19:
    print("Campinas")
elif number == 27:
    print("Vitoria")
elif number == 31:
    print("Belo Horizonte")
else:
    print("DDD not found")
