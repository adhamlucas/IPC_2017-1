#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Ulisses Antonio Antonino da Costa 1515090555
# Walter Nobre da Silva conceição   1715310057
# Jandinne Duarte de Oliveira       1015070265
# Vitor Summer Oliveira Pantaleão   1715310042
# Reinaldo vargas                   1715310054
#
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

vetor_salario =[]
abono = 100
contador = 0
montante = 1
soma_abono = 0
maior = []
while contador < montante:
    salario = int(input("Digite o salário : "))
    vetor_salario.append(salario)

    if salario == 0:
        vetor_salario.remove(0)
        print('todos os salários',vetor_salario)
        len(vetor_salario)
        print("=================================================")
        contador+=1

        for salario in vetor_salario:
            if salario < 1000:
                soma = abono+salario
                maior.append(soma)
                len(maior)
                print(salario,"salário + abono = ",soma)

print("Foram processados ", len(vetor_salario)," colaboradores")
print("O total gasto com abono  foi de :", sum(maior))
print("Maior valor de abono pago foi: ", 'R$',max(maior))
print("valor minimo pago a: ",len(maior), "funcionários")

