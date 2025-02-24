import random
import tkinter as tk
from tkinter import messagebox

#Lista de palabras tematica animales
palabras = ["ornitorrinco", "canguro", "elefante", "rinoceronte", "jirafa", "hipopotamo", "cocodrilo", "tigre", "pinguino", "ballena", "delfin", "tiburon", "calamar", "medusa", "caballo", "oveja", "gallina", "conejo", "raton", "oso hormiguero", "oso perezoso", "murcielago", "serpiente", "lagartija", "cocodrilo", "tortuga", "iguana", "camaleon", "lagarto"]

#Selecciona una palabra al azar y el numero de letras adivinadas
palabra_secreta = random.choice(palabras).lower()
letras_adivinadas = set()
intentos = 6

#Graficos de los estados del ahorcado
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

#Creación de la ventana principal del juego
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("400x600")

#Texto de la ventana Grafica
etiqueta = tk.Label(ventana, text="Bienvenido al juego del ahorcado", padx=20, pady=20)
etiqueta.pack()

#Muestra la palabra con letras adivinadas
label_palabra = tk.Label(ventana, text="", font=("Arial", 24)) 
label_palabra.pack(pady=20)

label_ahorcado = tk.Label(ventana, text="", font=("Arial", 14), justify=tk.LEFT)  #Muestra el estado del ahorcado
label_ahorcado.pack(pady=10)

label_intentos = tk.Label(ventana, text="", font=("Arial", 14))  #Muestra los intentos restantes
label_intentos.pack(pady=10)

entry_letra = tk.Entry(ventana, font=("Arial", 14))  #Campo para ingresar una letra
entry_letra.pack(pady=10)
entry_letra.focus_set()

boton_terminar = tk.Button(ventana, text="Terminar", font=("Arial", 14), command=ventana.destroy)  #Botón para terminar el juego
boton_terminar.pack(pady=10)

#Función para actualizar la interfaz gráfica
def actualizar_interfaz():
    tablero = " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
    label_palabra.config(text=tablero)
    label_ahorcado.config(text=ahorcado[6 - intentos])
    label_intentos.config(text=f"Intentos: {intentos}")

#Función para manejar la adivinanza de una letra
def adivinar_letra(event=None):
    global intentos
    letra = entry_letra.get().lower()
    entry_letra.delete(0, tk.END)
    #Verifica si la letra ya fue usada
    if letra in letras_adivinadas:  
        messagebox.showinfo("Ahorcado", "Letra ya usada.")
        return
    # Verifica si la letra está en la palabra secreta
    if letra in palabra_secreta:  
        letras_adivinadas.add(letra)# Verifica si el jugador ganó
        if all(l in letras_adivinadas for l in palabra_secreta):  
            messagebox.showinfo("Ahorcado","¡Ganaste! Palabra: {palabra_secreta}")
            reiniciar_juego()
    else:
        intentos -= 1  #Reduce los intentos si la letra es incorrecta
        if intentos == 0:  #Verifica si el jugador perdió
            messagebox.showinfo("Ahorcado","Perdiste. Palabra: {palabra_secreta}")
            reiniciar_juego()
    actualizar_interfaz()

#Función para reiniciar el juego
def reiniciar_juego():
    global palabra_secreta, letras_adivinadas, intentos
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = set() 
    intentos = 6 
    actualizar_interfaz() 

entry_letra.bind('<Return>', adivinar_letra)

reiniciar_juego()
ventana.mainloop()