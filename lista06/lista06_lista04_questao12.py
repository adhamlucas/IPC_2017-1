# ---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Natália Cavalcantre Xavier              1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Lista 4. Q 12 - Valida e corrige número de telefone.
#       Faça um programa que leia um número de telefone,
#       e corrija o número no caso deste conter somente 7 dígitos,
#       acrescentando o '3' na frente. O usuário pode informar o
#       número com ou sem o traço separador.

# -------------------------------------------------------------------------------------------------------------

telefone = str(input())
telefone = telefone.replace("-", "")

print(telefone)

if len(telefone) == 7 and telefone[0] != "3":

    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    print("Telefone corrigido sem formatação: 3%s" % telefone)

    telefone_formatado = "3" + telefone[0:3] + "-" + telefone[3:7]
    print("Telefone corrigido com formatação: %s" % telefone_formatado)