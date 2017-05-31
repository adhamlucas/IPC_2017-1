def verificar_quadrado_magico(quadrado):

    count = 0
    count1 = 0
    for x in range(2):

        linhas = quadrado[0 + count] + quadrado[1 + count] + quadrado[2 + count]
        coluns = quadrado[0 + count1] + quadrado[3 + count1] + quadrado[6 + count1]

        if linhas != 15 or coluns != 15:
            x = 4

        count += 3
        count1 += 1

    count = 0

    for y in range(2):

        diag = quadrado[0 + count] + quadrado[4] + quadrado[8 - count]

        if diag != 15:
            y = 4

        count += 2

    if x == 4 or y == 4:
        return 'Não é um quadrado mágico'

    else:
        return quadrado


quadrado = []

tam = 0

while len(quadrado) != 9:
    value = int(input('Digite um valor: '))

    if value not in quadrado:
        quadrado.append(value)

print(verificar_quadrado_magico(quadrado))

