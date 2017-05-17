matriz = []
for i in range(3):
    linha = []
    linha.append(raw_input("nome da planta: "))
    linha.append(int(input("quantidade ideal: ")))
    linha.append(int(input("quantidade em estoque: ")))
    matriz.append(linha)
a_comprar = []
for i in range(3):
    linha_b = []
    linha_b.append(matriz[i][0])
    linha_b.append("deve comprar: ")
    if matriz[i][2] - matriz[i][1] > 0:
        linha_b.append(0)
    else:
        linha_b.append(matriz[i][1] - matriz[i][2])
    a_comprar.append(linha_b)
for i in range(3):
    print(a_comprar[i])
