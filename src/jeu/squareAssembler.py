#-*-coding: Latin-1-*-
from tkinter import *
from tkinter.messagebox import *
from src.jeu import Plateau

def cliqueGauche(event):
    global plateau, score
    
    if(plateau!=None):
        x = (int)(event.x/tailleCarre)
        y = (int)(event.y/tailleCarre)
    
        score += plateau.supprime(x,y)
        plateau.gravite()
        plateau.decalage()
        maj()
            
def cliqueDroit(event):
    global plateau
    
    if(plateau!=None):
        x = (int)(event.x/tailleCarre)
        y = (int)(event.y/tailleCarre)
    
        plateau.l_map[y][x]=0
        plateau.gravite()
        plateau.decalage()
        maj()
     
def maj():
    global canvasPlateau, canvasScore, tailleCarre
    
    canvasPlateau.delete("all")
    tailleCarre = 600/plateau.tailleX

    x = 0
    while x<plateau.tailleX:
        y = 0
        while y<plateau.tailleY: 
            image = canvasPlateau.create_rectangle(x*tailleCarre,y*tailleCarre,x*tailleCarre+tailleCarre,y*tailleCarre+tailleCarre,fill=plateau.getCouleur(x,y))
            y = y+1
        x = x+1
    canvasPlateau.grid(row=0,column=0,padx=0)
    
    canvasScore.delete("all")
    canvasScore.create_text(50,50,text="Score = "+str(score))
    canvasScore.grid(row=0,column=1)

def aPropos():
    showinfo("Numéro d'anonymat", "Quentin Morizot")    

def nouveau():
    global win

    win = Toplevel(root)
    win.geometry('300x100+300+300')
    win.title("Changement de plateau")
    message = "Choisissez la taille du plateau:"
    Label(win, text=message).grid(row=0,column=0,columnspan=2)
    Button(win,text='10x10', command=nouveau10x10).grid(row=1,column=0,padx=0)
    Button(win,text='20x20', command=nouveau20x20).grid(row=1,column=1,padx=0)
    
def nouveau10x10():
    global plateau, score, win
    plateau = Plateau.Plateau(10,10)
    score = 0
    maj()
    win.destroy()
    
def nouveau20x20():
    global plateau, score, win
    plateau = Plateau.Plateau()
    score = 0
    maj()
    win.destroy()

root = Tk()
root.resizable(width=False,height=False)
root.title("Square Assembler")
root.geometry('810x605+200+200')
score = 0
# Menu
menubar = Menu(root)
# Menu Jeu et ses sous menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=nouveau)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Jeu", menu=filemenu)
# Menu "A propos" et son sous menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Numéro d'anonymat", command=aPropos)
menubar.add_cascade(label="A propos", menu=editmenu)
# affichage du menu
root.config(menu=menubar)

plateau = None

# Affichage de la map
canvasPlateau = Canvas(root, width=600, height=600, borderwidth=0, background='grey')
canvasPlateau.bind('<Button-1>', cliqueGauche)
canvasPlateau.bind('<Button-3>', cliqueDroit)
canvasPlateau.grid(row=0,column=0,padx=0)

canvasScore = Canvas(root, width=200, height=600, borderwidth=0, background='grey')
canvasScore.grid(row=0,column=1,padx=0)

root.mainloop()