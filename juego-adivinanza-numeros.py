import random


def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    acierto = False

    # Primeras líneas del juego dando la bienvenida
    print("¡Bienvendo al juego de adivinanza de número")
    print("Debes adivinar un número del 1 al 100")
    print("¡Intenta adivinar!")

    while not acierto:
        # Solicitar un número del 1 al 100
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo pasamos de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreo es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganado! El número {adivinanza} es el número secreto y lo has logrado en {intentos} intentos."
                )
        else:
            print("Por favor intruduzca un número valido")

juego_adivinanza()