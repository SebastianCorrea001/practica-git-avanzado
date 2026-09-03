""" Juego de adivinar el número secreto entre 1 y 100. """
""" Prueba """

import random

def mostrar_bienvenida():
    print("=" * 40)
    print("¡Bienvenido al juego de adivinar el número secreto!")
    print("=" * 40)

def pedir_intento():
    return int(input("Introduce tu intento (entre 1 y 100): "))

def dar_pista(intento, numero_secreto):
    if intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 12
    mostrar_bienvenida()
    print("Elige un numero entre 1 y 100.")

    while intentos < max_intentos:
        intento = pedir_intento()
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
            break
        else:
            print(dar_pista(intento, numero_secreto))
    else:
        print(f"Se acabaron los intentos. El número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")

if __name__ == "__main__":
    jugar()