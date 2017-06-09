#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009 
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030 
# Felipe Eduardo Silva de Almeida   1715310031 
# Felipe Guerreiro De Mello         1315120052 
# Silas castro de Mendonça          1715310066
#
#03.Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#----------------------------------------------------------------

name = input("Digite seu nome (mín.: 3 caracteres): ")
while len(name) < 3:
    print("Campo inválido: ")
    name = input("Digite seu nome (mín.: 3 caracteres): ")

age = int(input("Digite sua idade: "))
while age < 0 or age > 150:
    print("Campo inválido: ")
    age = int(input("Digite sua idade: "))

sallary = float(input("Digite seu salário: "))
while sallary <= 0:
    print("Campo inválido :")
    sallary = float(input("Digite seu salário: "))

sex = input("Digite seu sexo usando f para feminino e m para masculino: ")
while sex != 'f' and sex != 'm':
    print("Campo inválido: ")
    sex = input("Digite seu sexo usando f para feminino e m para masculino: ")

civil_state = input("Digite seu estado civil (s, c, v, d): ")
while civil_state != 's' and civil_state != 'c' and civil_state != 'v' and civil_state != 'd':
    civil_state = input("Digite seu estado civil (s, c, v, d): ")

print("Informações atualizadas") 
