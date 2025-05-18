# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    
        return sum(sum(fila) for fila in matriz)

        pass

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
        return max(max(fila) for fila in matriz)
        pass

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    pass

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
        return [list(fila) for fila in zip(*matriz)]
        pass

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
        return [x for x in lista if x % 2 == 0]
        pass

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
        return len(frase.split())
        pass

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
        return [n * i for i in range(1, 11)]
        pass

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
        return sum(1 for x in lista if x < 0)
        pass

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
    pass

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    resultado = []
    for char in texto:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado.append(nuevo_char)
        else:
            resultado.append(char)
    return ''.join(resultado)
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()