import ipc.matriz

matrix = ipc.matriz.cria_matriz_quadrada(6)
ipc.matriz.imprime_matriz(matrix)
minor = ipc.matriz.menor_item_secundaria(matrix)
print("O menor item da diagona secundária é: %d" %minor)