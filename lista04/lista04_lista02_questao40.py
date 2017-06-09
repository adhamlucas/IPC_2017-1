# ------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de souza Barbosa - 1315120206
#
#
# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente
# às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para 
# cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média
# for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for
# inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor
# entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
# Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
# Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2).
# e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.",
# (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter
# pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.
# --------------------------------------------------------------------------------------------------------------------

n1 = float(input("Informe a 1º nota: "))
n2 = float(input("Informe a 2º nota: "))
n3 = float(input("Informe a 3º nota: "))
n4 = float(input("Informe a 4º nota: "))
n1p = n1*2
n2p = n2*3
n3p = n3*4
n4p = n4*1

media = ((n1p+n2p+n3p+n4p)/4)
print("Média: %.1f" %media)

if media >= 7.0:
    print("Aluno aprovado")
elif media < 5.0:
    print("Aluno reprovado")
elif 5 <= media <= 6.9:
    print("Aluno em exame")
if 5 <= media <= 6.9:
    exame = float(input("Nota do exame:"))
    media2 = ((media+exame)/2)
    print("Média do exame: %.1f" %media2)
    if media2 >= 5:
        print("aprovado!")
    else:
        print("Reprovado no Exame")
