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
# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for
#maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos",
#senão escrever "Valores nao aceitos".

nums = (input().split())
a,b,c,d = nums
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a:
	if c+d > a+b:
		if c > 0 and d > 0:
			if a % 2 == 0:
				print("Variaveis aceitas")
else:
	print("Variaveis invalidas")
