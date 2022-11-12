# coding: utf-8

from tkinter import *
from random import *

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
canvas = Canvas(fenetre, width=500, height=500, background='white')
for i in range(10):
    ligne1 = canvas.create_line(50*i, 0, 50*i, 500)
    ligne2 = canvas.create_line(0, 50*i, 500, 50*i)
canvas.pack()

fenetre.mainloop()
