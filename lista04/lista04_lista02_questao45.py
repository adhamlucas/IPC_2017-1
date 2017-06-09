#------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr.
#
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Joelson Pereira Lima                  1715310060
# Judá Salazar Braga                    1515200050
# Kethelen Tamara Braga Barbosa         1525212002
# Lucas Gabriel Silveira                1715310053
# Silas Castro de Mendonça              1715310066
# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, 
#de modo que o lado A representa o maior dos
#3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, 
#com base nos seguintes casos, sempre escrevendo
#uma mensagem adequada:
	#se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
	#se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
	#se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
	#se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
	#se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
	#se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
#--------------------------------------------------------------------------
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

maior = A
if B > maior:
    maior = B
    B = A
    A = maior
if C > maior:
    maior = C
    C = A
    A = maior

if A >= B+C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')

if A == B == C:
        print('TRIANGULO EQUILATERO')
else:
    if A == B != C or A != B == C or A == C != B:
        print('TRIANGULO ISOSCELES')
