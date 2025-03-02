#Juego del ahorcado Proyecto
import random
#Palabras que debe adivinar el usuario
palabras = ["ornitorrinco", "canguro", "elefante", "rinoceronte", 
            "jirafa", "hipopotamo", "cocodrilo", "gorila",  
            "pinguino", "ballena", "delfin", "tiburon", 
            "calamar", "medusa", "caballo", "gallina", 
            "murcielago", "serpiente", "lagartija", "cocodrilo", 
            "tortuga", "iguana", "camaleon", "lagarto"]
#El codigo elige aleatoriamente una palabra de la lista anterior
palabra_oculta = random.choice(palabras)
letras_adivinadas = set()
intentos = 6
#Etapas del ahorcado para mostrar en la pantalla de inicio
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
      / \   |
           |
    --------
    """
]

#Pantalla de inicio del codigo del juego
print(" JUEGO DEL AHORCADO ")
print("BIENVENIDOS AL JUEGO DEL AHORCADO")
print("Tematica: Animales")
print("Buena suerte!")
print("Solo tienes 6 intentos para encontrar la palabra secreta")

#Mostrar el estado del tablero y el dibujo del ahorcado
while intentos > 0:
    
    tablero = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra_oculta])
    print(tablero)
    print(ahorcado[6 - intentos])

    #Ingreso de datos del jugador para adivinar la palabra oculta
    letra = input("Introduce una letra: ").lower()

    #Aqui se verifica que el usuario no ingrese una letra repetida 
    if letra in letras_adivinadas:
        print("Ya has intentado con esa letra. Prueba con otra.")
        continue

    #Bucle de verificacion de los datos ingresados por el usuario

    #Si la letra está en la palabra oculta, se suma a las letras adivinadas
    if letra in palabra_oculta:
        letras_adivinadas.add(letra)
        print("¡Correcto! La letra está en la palabra.")

    #Si la letra no está en la palabra oculta se resta un intento y vuelve a pedir otra letra   
    else:
        intentos -= 1
        print("Incorrecto. Te quedan ",intentos, "intentos.")

    #sverifica si el usuario adivina todas las letras de la palabra oculta
    if all(letra in letras_adivinadas for letra in palabra_oculta):
        print("Felicidades :) Has adivinado, la palabra era: ", palabra_oculta)
        break

#verifica si el usuario pierde todos sus intentos
if intentos == 0:
    print("Lo siento :( Has perdido, La palabra era: " , palabra_oculta)
    #Presenta el dibujo final del ahorcado
    print(ahorcado[6])  

print("¡Gracias por jugar!")
