#13)Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
#calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
#-----------------------------------------------------------------------------------------------------------------------

mes = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho",
       "agosto", "setembro", "outubro", "novembro", "dezembro"]
temperatura_ano = []
c = 0

while c < 12:
    print(mes[c])
    temperatura = input("Digite a temperatura media do mês: ")
    temperatura_ano.append(temperatura)
    c += 1
i = 0
soma = 0
while i < len(temperatura_ano):
    soma += int(temperatura_ano[i])
    i += 1
media = soma / len(temperatura_ano)
x = 0
soma2 = 0
print("%.2f"%media)
while x < len(temperatura_ano):
    if float(temperatura_ano[x]) > float(media):
        print(x+1,"-",mes[x],"graus",end=" ")
        print(temperatura_ano[x])
        soma2 += 1
    x += 1
if soma2 == 0:
    print("Não existe nenhum mes com temperatura acima da média")
