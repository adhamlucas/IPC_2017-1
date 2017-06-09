# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Diogo Roberto Duarte da Costa 1715310056
# Iury da Silva Coelho          1715310069
#
# 2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
# Faça um programa que leia e valide as seguintes informações:
#-----------------------------------------------------------------------------------------------------------------------

username = input("Informe um nome de usuário: ")
password = input("Digite sua senha: ")

while username == password:
    print("Não utilize seu nome de usuário como senha!")
    password = input("Digite sua senha: ")

print("Informações válidas")
