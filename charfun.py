# Devuelve True o False (Utilizo dos maneras de eliminar los espacios e invertir la cadena)
def esPalindromo(cadena):
    # Elimina los espacios
    #cadena_sin_espacios = cadena.replace(" ", "")

    # Elimina los espacios
    cadena_sin_espacios = "".join(cadena.split())

    # Conviete la cadena a minúsculas
    cadena_minusculas = cadena_sin_espacios.lower()

    # Invierte la cadena
    #cadena_invertida = cadena_minusculas[::-1]

    # Declara variable invertida como vacía
    cadena_invertida = ""
    
    # Invierte la cadena
    for i in range(len(cadena_minusculas) - 1, -1, -1):
        cadena_invertida = cadena_invertida + cadena_minusculas[i] 

    return(cadena_minusculas == cadena_invertida) 


if __name__ == "__main__":

    import os

    # Borra la consola
    #os.system('cls')

    # Pide una cadena de texto
    cadena = input("Escribe una palabra: ")

    # Imprime por pantalla si la cadena es palíndromo o no
    if esPalindromo(cadena):
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")
