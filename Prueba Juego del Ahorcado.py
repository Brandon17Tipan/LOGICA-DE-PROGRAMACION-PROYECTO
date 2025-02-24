# Palabra fija para el juego
palabra_secreta = "murcielago"
letras_adivinadas = set()
intentos = 6

# Dibujo de las etapas del ahorcado
ahorcado = [
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    --------
    """
]

# Pantalla de Inicio del juego
print(" JUEGO DEL AHORCADO ")
print("BIENVENIDOS AL JUEGO DEL AHORCADO")
print("Tematica: Animales")
print("Buena suerte!")
print("Solo tienes 6 intentos para encontrar la palabra secreta")

# Bucle principal con el que juego funciona
while intentos > 0:
    # Mostrar el estado actual del tablero y el dibujo del ahorcado
    tablero = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
    print(tablero)
    print(ahorcado[6 - intentos])

    # Pedir al jugador que ingrese una letra
    letra = input("Introduce una letra: ")

    # Verificar si la letra ya fue ingresada no se eliminan los intentos
    if letra in letras_adivinadas:
        print("Ya has intentado con esa letra. Prueba con otra.")
        continue

    # Verificar si la letra está en la palabra secreta
    # Si la letra está en la palabra, se agrega a las letras adivinadas
    if letra in palabra_secreta:
        letras_adivinadas.add(letra)
        print("La letra está en la palabra.")
    # Si la letra no está en la palabra, se resta un intento    
    else:
        intentos -= 1
        print("Incorrecto. Te quedan ",intentos, "intentos.")

    # Verificar si el jugador ha adivinado toda la palabra
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("Felicidades :) Has adivinado, la palabra era: ", palabra_secreta)
        break

# Si el jugador se queda sin intentos
if intentos == 0:
    print("Lo siento :( Has perdido, La palabra era: " , palabra_secreta)
    print(ahorcado[6])  # Mostrar el dibujo final del ahorcado

print("Gracias por jugar")
