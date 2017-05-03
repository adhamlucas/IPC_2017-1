"""Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro
de combustível. Calcule e mostre:

    O modelo do carro mais econômico;
    Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetro
    s
    e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O dis
    posição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada exe
    cução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout."""

cars = input().split()
liters_km = input().split()
size = len(liters_km)
cars_organized = [0,0,0,0,0]
liters_km_organized = [0,0,0,0,0]
c = 0
car = 0
menor = 0

while c < size:
    for i in range(size):
        if float(i) < float(liters_km[c]):
            menor += 1
            print("menor",menor)
    if menor == 1:
        cars_organized[4] = [cars[c]]
        liters_km_organized[4] = [liters_km[c]]

    elif menor == 2:
        cars_organized[3] = [cars[c]]
        liters_km_organized[3] = [liters_km[c]]


    elif menor == 3:
        cars_organized[2] = [cars[c]]
        liters_km_organized[2] = [liters_km[c]]

    elif menor == 4:
        cars_organized[1] = [cars[c]]
        liters_km_organized[1] = [liters_km[c]]


    elif menor == 5:
        cars_organized[0] = [cars[c]]
        liters_km_organized[0] = [liters_km[c]]

    c += 1
    menor = 0

for i in range(size):
    liters_km[i] = float(liters_km[i]) * 2.25
c = 0
print("Relatório Final")
while c < size:
    print(c + 1,"-",cars_organized[c],"-",liters_km_organized[c],"Litros -", liters_km[c])
    c += 1
print("O Menor consumo é do :", cars_organized[0])
