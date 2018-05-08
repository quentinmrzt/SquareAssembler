from tkinter import Tk, Menu, Canvas, Label, Toplevel, Button
from tkinter.messagebox import showinfo
from src.jeu import Plateau
from src.jeu import Modele

class Fenetre:
    def __init__(self,modele):
        self.modele = modele
        
        self.root = Tk()
        self.root.resizable(width=False,height=False)
        self.root.title("Square Assembler")
        self.root.geometry('810x605+200+200')
        
        self.win = None
        
        # Menu
        menubar = Menu(self.root)
        
        # Menu Jeu et ses sous menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nouveau", command=self.nouveau)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=self.root.quit)
        
        menubar.add_cascade(label="Jeu", menu=filemenu)
        # Menu "A propos" et son sous menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Numéro d'anonymat", command=self.aPropos)
        menubar.add_cascade(label="A propos", menu=editmenu)
        
        # Affichage de la map
        self.canvasPlateau = Canvas(self.root, width=600, height=600, borderwidth=0, background='grey')
        self.canvasPlateau.bind('<Button-1>', self.cliqueGauche)
        self.canvasPlateau.bind('<Button-3>', self.cliqueDroit)
        self.canvasPlateau.grid(row=0,column=0,padx=0)
        
        # Affichage du score
        self.canvasScore = Canvas(self.root, width=200, height=600, borderwidth=0, background='grey')
        self.canvasScore.grid(row=0,column=1,padx=0)
        
        # affichage du menu
        self.root.config(menu=menubar)
        
        self.root.mainloop()
        
    def maj(self):        
        self.canvasPlateau.delete("all")
        
        if(self.modele.existePlateau()):
            tailleCarre = 600/self.modele.tailleX
        
            x = 0
            while x<self.modele.tailleX:
                y = 0
                while y<self.modele.tailleY: 
                    self.canvasPlateau.create_rectangle(x*tailleCarre,y*tailleCarre,x*tailleCarre+tailleCarre,y*tailleCarre+tailleCarre,fill=self.modele.plateau.getCouleur(x,y))
                    y = y+1
                x = x+1
            self.canvasPlateau.grid(row=0,column=0,padx=0)
            
            self.canvasScore.delete("all")
            self.canvasScore.create_text(50,50,text="Score = "+str(self.modele.score))
            self.canvasScore.grid(row=0,column=1)
            
            
    def aPropos(self):
        showinfo("Numéro d'anonymat", "Quentin Morizot")    
    
    def nouveau(self):
        self.win = Toplevel(self.root)
        self.win.geometry('300x100+300+300')
        self.win.title("Changement de plateau")
        
        Label(self.win, text="Choisissez la taille du plateau:", width=41, height=2).grid(row=0,column=0,columnspan=2)
        Button(self.win,text='10x10', width=10, height=3,command=self.nouveau10x10).grid(row=1,column=0,padx=0)
        Button(self.win,text='20x20', width=10, height=3, command=self.nouveau20x20).grid(row=1,column=1,padx=0)
        
    def nouveau10x10(self):
        self.modele.nouveauPlateau(10,10)
        self.maj()
        self.win.destroy()
        
    def nouveau20x20(self):
        self.modele.nouveauPlateau(20,20)
        self.maj()
        self.win.destroy()
        
    def cliqueGauche(self,event): 
        if(self.modele.existePlateau()):

            tailleCarre = 600/self.modele.tailleX
            
            x = (int)(event.x/tailleCarre)
            y = (int)(event.y/tailleCarre)
        
            self.modele.supprimerCase(x,y)
            
            self.maj()
                
    """ Fonction pour tester: à supprimer """
    def cliqueDroit(self,event):
        if(self.modele.existePlateau()):
            tailleCarre = 600/self.modele.tailleX
            
            x = (int)(event.x/tailleCarre)
            y = (int)(event.y/tailleCarre)
        
            self.modele.plateau.l_map[y][x]=0
            self.modele.plateau.gravite()
            self.modele.plateau.decalage()
            self.maj()