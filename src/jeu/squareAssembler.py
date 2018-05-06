#-*-coding: Latin-1-*-
from tkinter import *
from tkinter.messagebox import showinfo
import random



def test(event):
    global tailleCarre, listeCouleur, l_map
    x = (int)(event.x/tailleCarre)
    y = (int)(event.y/tailleCarre)
    print("[",x,"/",y,"]")
    print("Couleur: ",listeCouleur[l_map[y][x]])
    
    


root = Tk()
root.title("Square Assembler")
root.geometry('500x500+200+200')

def aPropos():
    showinfo("Numéro d'anonymat", "Quentin Morizot")

    
def nouveau():
    print("Rien de nouveau")

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


# Generation de la map
tailleX = 20; tailleY = 20
nbCouleur = 8
nbParCouleur = [int((tailleX*tailleY)/nbCouleur)]*nbCouleur
listeCouleur = ["red","blue","yellow","green","cyan","magenta","violet","teal"]

l_map = [[0]*tailleX for i in range(tailleY)]
x = 0
while x<tailleX:
    y = 0
    while y<tailleY:
        trouve = False
        while(not trouve):
            rdm =  random.randint(0,nbCouleur-1)
            if(nbParCouleur[rdm]!=0):
                nbParCouleur[rdm] = nbParCouleur[rdm]-1
                l_map[y][x] = rdm
                trouve = True
        y = y+1
    x = x+1


# Affichage de la map
tailleCarre = 20
canvas = Canvas(root, width=tailleCarre*tailleX, height=tailleCarre*tailleY, background='grey')

x = 0
while x<tailleX:
    y = 0
    while y<tailleY: 
        image = canvas.create_rectangle(x*tailleCarre,y*tailleCarre,x*tailleCarre+tailleCarre,y*tailleCarre+tailleCarre,fill=listeCouleur[l_map[y][x]])
        y = y+1
    x = x+1



canvas.bind('<Button-1>', test)



#canvas.coords(image, 0, 0, 5, 5)
canvas.pack()



root.mainloop()