#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058

# Escreva um algoritmo em PORTUGOL que calcule os N-menores números primos.
#Este número N deve ser lido do teclado.




n2= int(input("digite limite"))
n = 0
a = 0
while a < n2:
  a=a+1
  isPrime = 1
  if n < 2:
    isPrime = 0
    n=n+1
  else:
      i = 2
      while i*i <= n:
          if n%i == 0:
              isPrime = 0
          i += 1
      if isPrime != 0:
        print(n)
  
  n=n+1
