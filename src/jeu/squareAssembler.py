#-*-coding: Latin-1-*-
from tkinter import *
from tkinter.messagebox import showinfo
import random

from src.jeu import Plateau

def test(event):
    global tailleCarre, plateau
    x = (int)(event.x/tailleCarre)
    y = (int)(event.y/tailleCarre)
    print("[",x,"/",y,"]")
    print("Couleur: ",plateau.getCouleur(x,y))
    print("C'est case est supprimable :", plateau.estSupprimable(x,y))
    plateau.supprime(x,y)
    plateau.gravite()
    plateau.decalage()
    maj()

     
def maj():
    global canvas
    x = 0
    while x<plateau.tailleX:
        y = 0
        while y<plateau.tailleY: 
            image = canvas.create_rectangle(x*tailleCarre,y*tailleCarre,x*tailleCarre+tailleCarre,y*tailleCarre+tailleCarre,fill=plateau.getCouleur(x,y))
            y = y+1
        x = x+1
    canvas.pack()
    
root = Tk()
root.title("Square Assembler")
root.geometry('500x500+200+200')

def aPropos():
    showinfo("Numéro d'anonymat", "Quentin Morizot")

    
def nouveau():
    plateau.aleatoire()
    maj()

menubar = Menu(root)

# Menu Jeu et ses sous menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=nouveau)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Jeu", menu=filemenu)

# Menu "A propos" et ses sous menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Numéro d'anonymat", command=aPropos)
menubar.add_cascade(label="A propos", menu=editmenu)

# affichage du menu
root.config(menu=menubar)

plateau = Plateau.Plateau()

# Affichage de la map
tailleCarre = 20
canvas = Canvas(root, width=tailleCarre*plateau.tailleX, height=tailleCarre*plateau.tailleY, background='grey')

x = 0
while x<plateau.tailleX:
    y = 0
    while y<plateau.tailleY: 
        image = canvas.create_rectangle(x*tailleCarre,y*tailleCarre,x*tailleCarre+tailleCarre,y*tailleCarre+tailleCarre,fill=plateau.getCouleur(x,y))
        y = y+1
    x = x+1

canvas.bind('<Button-1>', test)

#canvas.coords(image, 0, 0, 5, 5)
canvas.pack()

root.mainloop()