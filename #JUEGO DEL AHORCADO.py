""" JUEGO DEL AHORCADO """
#Definir la tematica y las palabras a adivinar
Palabras_animales=["perro","gato","leon","tigre","elefante","jirafa","cebra","mono","oso","pato","gallina","vaca","caballo","burro","cerdo","oveja","conejo","rana","tortuga","cocodrilo","serpiente","aguila","halcon","loro","pajaro","pavo","cisne","pato","ganso","paloma","colibri","avestruz","pinguino","ballena","delfin","tiburon","pez","pulpo","calamar","cangrejo","langosta","camaron","caracol"]
#texto que aparece al inicio del juego
print("BIENVENIDOS AL JUEGO DEL AHORCADO")
print("Tematica: Animales")
print("Solo tienes 6 intentos para encontrar la palabra secreta")
print("Buena suerte!")
#Ingresar el dibujo de las etapas del ahorcado
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
#texto que aparece al final del juego
#Si gana el juego
print("Felicidades :) Has encontrado la palabra secreta")
#Si pierde el juego
print("Lo siento :( Has perdido")