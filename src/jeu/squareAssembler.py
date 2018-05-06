#-*-coding: Latin-1-*-
from tkinter import *
from tkinter.messagebox import showinfo
import random

from src.jeu import Plateau

def cliqueGauche(event):
    global plateau
    x = (int)(event.x/tailleCarre)
    y = (int)(event.y/tailleCarre)
    
    plateau.supprime(x,y)
    plateau.gravite()
    plateau.decalage()
    maj()
    
def cliqueDroit(event):
    global plateau
    x = (int)(event.x/tailleCarre)
    y = (int)(event.y/tailleCarre)
    
    plateau.l_map[y][x]=0
    plateau.gravite()
    plateau.decalage()
    maj()

     
def maj():
    global canvas, tailleCarre
    
    canvas.delete("all")
    tailleCarre = 600/plateau.tailleX

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
root.geometry('600x600+200+200')

def aPropos():
    showinfo("Numéro d'anonymat", "Quentin Morizot")

    
def nouveau10x10():
    global plateau
    plateau = Plateau.Plateau(10,10)
    maj()
    
def nouveau20x20():
    global plateau
    plateau = Plateau.Plateau()
    maj()

plateau = Plateau.Plateau()



menubar = Menu(root)

# Menu Jeu et ses sous menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau 10x10", command=nouveau10x10)
filemenu.add_command(label="Nouveau 20x20", command=nouveau20x20)

filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Jeu", menu=filemenu)

# Menu "A propos" et ses sous menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Numéro d'anonymat", command=aPropos)
menubar.add_cascade(label="A propos", menu=editmenu)

# affichage du menu
root.config(menu=menubar)


# Affichage de la map
tailleCarre = 600/20
canvas = Canvas(root, width=600, height=600, background='grey')

x = 0
while x<plateau.tailleX:
    y = 0
    while y<plateau.tailleY: 
        image = canvas.create_rectangle(x*tailleCarre,y*tailleCarre,x*tailleCarre+tailleCarre,y*tailleCarre+tailleCarre,fill=plateau.getCouleur(x,y))
        y = y+1
    x = x+1

canvas.bind('<Button-1>', cliqueGauche)
canvas.bind('<Button-3>', cliqueDroit)


#canvas.coords(image, 0, 0, 5, 5)
canvas.pack()

root.mainloop()