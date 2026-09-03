""" Juego de adivinar el número secreto entre 1 y 100. Final"""
""" Prueba - Sebastian Correa - Autor"""

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

def mostrar_resultado_final(gano, intentos, numero_secreto):
    if gano:
        print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
    else:
        print(f"Se acabaron los intentos. El número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")

#Funcion para reiniciar el juego 

def quiere_jugar_de_nuevo():
    respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    return respuesta == 's'

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
            mostrar_resultado_final(True, intentos, numero_secreto)
            break
        else:
            print(dar_pista(intento, numero_secreto))
    else:
        mostrar_resultado_final(False, intentos, numero_secreto)

if __name__ == "__main__":
    jugar()