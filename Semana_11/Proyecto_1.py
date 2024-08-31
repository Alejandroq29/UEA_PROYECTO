# Definimos la matriz 3x3
arreg_bidim_matriz = [
    [30, 40, 60], #indice 0
    [20, 10, 70], #indice 1
    [90, 50, 80]  #indice 2
]

def buscar_valor (arreg_bidim_matriz, valor) :
    # Recorremos el arreg_bidim_matriz
    for i in range(len(arreg_bidim_matriz)):
        for j in range(len(arreg_bidim_matriz[i])):
            if arreg_bidim_matriz [i][j] == valor:
                return [i,j]  # Retornamos la posición (fila, columna)
    return None  # Retornamos None si no se encuentra el valor

# Valor a buscar
valor_a_buscar = 50

# Llamamos a la función de búsqueda
resultado = buscar_valor(arreg_bidim_matriz, valor_a_buscar)

# Mostramos el resultado
if resultado is not None:
    print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en el arreg_bidim_matriz.")