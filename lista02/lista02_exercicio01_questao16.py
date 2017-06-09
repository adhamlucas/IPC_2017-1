# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Hugo Thadeu Silva Cardoso	         1715310013
# Luiz Paulo Machado	             1515200542
# Ian Gabriel Costa Machado          1215120276
# André Luis Laborda Neves	         1515070006
# Gabriel de Queiroz Souza           1715310044
# João Vitor De Cordeiro B Gonçalves 1515140036
#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#  Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#  que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# ----------------------------------------------------------
metros = int(input("Digite a quantidade de metros quadrados a serem pintados: "))
litros = metros/3

priceL = 80.0
capacityL = 18

latas = round(litros / capacityL,2)
total = round(latas * priceL,2)

print ('Você usará',latas,'latas de tinta')
print ('O preco total é de: R$',total)
