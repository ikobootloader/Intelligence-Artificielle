# coding: utf-8

from tkinter import *
from random import *
from tkinter import Canvas

fenetre = Tk()

# label = Label(fenetre, text="")
# label.pack()

fenetre.title("Grille de territoire")
fenetre.geometry("800x600+10+10")

"""
#Intégrer une image
photo = PhotoImage(file="ma_photo.png")
canvas = Canvas(fenetre,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
"""
# Créer une grille
# canvas
canvas: Canvas = Canvas(fenetre, width=500, height=500, background='white')
canvas.pack()

for i in range(10):
    canvas.create_line(50 * i, 0, 50 * i, 500)
    canvas.create_line(0, 50 * i, 500, 50 * i)

# CREATION DE L AGENT

# Les 2 premières coordonnées sont : x1,y1
# et correspondent au coin supérieur gauche du rectangle et les 2
# dernières : x2,y2 correspondent au coin inférieur droit.
# canvas.create_oval(105, 5, 145, 45, width=5, outline="pink")
# Progression sur les x de 50 en 50, idem pour les y
# canvas.create_oval(155,5,195,45,width=5,outline="pink")
# canvas.create_oval(155,55,195,95,width=5,outline="pink")

# Position de l'agent
agent_x1 = 105
agent_y1 = 5
agent_x2 = 145
agent_y2 = 45

# Max haut gauche x0 y0
# canvas.create_oval(5, 5, 45, 45, width=5, outline="red")
# Max haut droite x10 y0
# canvas.create_oval(455, 5, 495, 45, width=5, outline="red")
# Max bas gauche x0 y10
# canvas.create_oval(5, 455, 45, 495, width=5, outline="red")
# Max bas droite x10 y10
# canvas.create_oval(455, 455, 495, 495, width=5, outline="red")

def modification():

    compteur = 0
    while compteur < 100:
        # Créer un chiffre aléatoire pour l'action d'exploration
        actionAleatoire = randint(0, 3)
        if actionAleatoire == 0 and agent_x1 + 50 <= 455 and agent_x2 + 50:
            canvas.create_oval(5, 5, 45, 45, width=5, outline="red")
            # canvas.create_oval(agent_x1 + 50, agent_y1, agent_x2 + 50, agent_y2, width=5, outline="pink")
        elif actionAleatoire == 1 and agent_x1 - 50 >= 5 and agent_x1 - 50 >= 5:
            canvas.create_oval(455, 5, 495, 45, width=5, outline="red")
            # canvas.create_oval(agent_x1 - 50, agent_y1, agent_x2 - 50, agent_y2, width=5, outline="pink")
        elif actionAleatoire == 2 and agent_y1 + 50 <= 455 and agent_y2 + 50 <= 455:
            canvas.create_oval(5, 455, 45, 495, width=5, outline="red")
            # canvas.create_oval(agent_x1, agent_y1 + 50, agent_x2, agent_y2 + 50, width=5, outline="pink")
        elif actionAleatoire == 3 and agent_y1 - 50 >= 5 and agent_x2 + 50 <= 455:
            canvas.create_oval(455, 455, 495, 495, width=5, outline="red")
            # canvas.create_oval(agent_x1, agent_y1 - 50, agent_x2, agent_y2 - 50, width=5, outline="pink")

fenetre.after(5000, modification)
fenetre.mainloop()



