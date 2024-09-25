print(" ")
print("Alvarez Delgado yael Ismael: #5 Programa que almacene un número y pida al usuario adivinarlo.")
print(" ")
import random
# El programa elige un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego de adivinanzas!")
print("He pensado en un número entre 1 y 10. Intenta adivinarlo.")

# Variable para seguir el bucle hasta que el usuario acierte
adivinado = False

while not adivinado:
    # Pedimos al usuario que ingrese su adivinanza
    intento = int(input("Introduce tu adivinanza: "))

    # Comprobamos si el número es mayor, menor o igual al número secreto
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
        print(" ")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
        print(" ")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto}.")
        adivinado = True
