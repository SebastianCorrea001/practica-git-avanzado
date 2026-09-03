""" Juego de adivinar el número secreto entre 1 y 100. """
""" Prueba """

import random

def jugar():
    numero_secreto = random.randint(1, 100)
    print("¡Bienvenido al juego de adivina el numero: !")
    print("Elige un numero entre 1 y 100.")

    while True:
        intento = int(input("Introduce tu intento: "))

        if intento == numero_secreto:
            print("¡Felicidades! Has adivinado el número secreto.")
            break
        elif intento < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("El número secreto es menor. Intenta de nuevo.")

if __name__ == "__main__":
    jugar()