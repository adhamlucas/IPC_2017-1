# encoding: utf-8
# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA - 1515090555
# TIAGO FERREIRA ARANHA - 1715310047
# VÍTOR SIMÕES AZEVEDO - 1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA - 1715310063
# REINALDO VARGAS - 1715310054
#
# 47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
# alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme
# a descrição acima informada (retirar o melhor e o pior salto e depois calcular
# a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04
# -----------------------------------------------------------------------------

nome_ginasta = input("Informe o nome do ginasta: ")

c = 1

soma = 0

while c <= 7:

    valor = float(input("Nota {}: ".format(c)))
    soma = soma + valor

    if c == 1:
        melhor_nota = valor
        pior_nota = valor
    else:
        if valor > melhor_nota:
            melhor_nota = valor
        elif valor < pior_nota:
            pior_nota = valor
    c += 1

    media = (soma - melhor_nota - pior_nota) / 5

print("Resultado final:")
print("Atleta: %s" % nome_ginasta)
print("Melhor nota: %1.1f" % melhor_nota)
print("Pior nota: %1.1f" % pior_nota)
print("Media: %1.2f" % media)
