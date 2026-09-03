""" Juego de adivinar el número secreto entre 1 y 100. """
""" Prueba """

import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    print("¡Bienvenido al juego de adivina el numero: !")
    print("Elige un numero entre 1 y 100.")

    while True:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos. ")
            break
        elif intento < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("El número secreto es menor. Intenta de nuevo.")
    else:
        print(f"Lo siento, has agotado tus {max_intentos} intentos. El número secreto era {numero_secreto}.")
        jugar()

if __name__ == "__main__":
    jugar()