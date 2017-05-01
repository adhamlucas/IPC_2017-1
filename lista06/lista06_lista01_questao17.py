#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Dayana Picanço Marquez            1715310058
# Vitor Simões Azevedo              1715310025
# Wilbert Luís Evangelista Marins   1715310055
# Enrique Leo Barbosa Izel          1515310048
# Edson de Lima Barros              1715310043
# Víctor Hugo de Oliveira Carreira  1715310063
#
#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
#determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
#distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
#O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme
#o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
#
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#
#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m
#
c = 0
saltos = []
nome = input("Atleta: ")
soma = 0
while c < 5:
    if len(nome) == 0 or len(nome) <= 2:
        break
    number = input("salto(em metros): ")
    soma = soma + float(number)
    saltos.append(number)
    c = c + 1
media = soma/ 5

print("\nResultado Final: ")
print("Atleta: ",nome)
print("saltos: ", saltos)
print("Média dos saltos: ",media, "m")
