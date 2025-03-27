def print_mem_tree(mem, depth=0):
    for key, value in mem.items():
        print("    " * depth, key, ":", value)
        if isinstance(value, dict):
            print_mem_tree(value, depth + 1)



#imprimir matriz
def mostrar_matriz(matriz):
    print("La matriz es la siguiente:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()  # Cambia de línea después de imprimir una fila completa            