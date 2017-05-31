# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
#
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão
#
# é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados,
#
# eles devem ser modificados para valores dentro da faixa de forma elegante.


from lista08.ipc import matriz, vetor
matriz1 = matriz.cria_matriz(40, 40)

matriz.imprime_retagulo_matriz(matriz1)
