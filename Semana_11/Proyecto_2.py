# Definimos la matriz 3x3
arreg_bidim_matriz = [
    [30, 40, 60], #indice 0
    [20, 10, 70], #indice 1
    [50, 90, 80]  #indice 2
]

def bubble_sort(fila):
    # Implementación del algoritmo Bubble Sort
    n = len(fila)
    for a in range(n):
        for b in range(0, n-a-1):
            if fila[b] > fila[b+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                fila[b], fila[b+1] = fila[b+1], fila[b]

def ordenar_fila(arreg_bidim_matriz, fila_index):
    # Ordenar la fila específica de el arreg_bidim_matriz
    if 0 <= fila_index < len(arreg_bidim_matriz):
        bubble_sort(arreg_bidim_matriz[fila_index])
    else:
        print("Índice de fila fuera de rango.")

# Mostrar el arreg_bidim_matriz original
print("Matriz original:")
for fila in arreg_bidim_matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Llamamos a la función para ordenar la fila
ordenar_fila(arreg_bidim_matriz, fila_a_ordenar)

# Mostrar el arreg_bidim_matriz con la fila ordenada
print("\narreg_bidim_matriz con la fila ordenada:")
for fila in arreg_bidim_matriz:
    print(fila)