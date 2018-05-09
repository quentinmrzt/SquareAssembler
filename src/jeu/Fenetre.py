from tkinter import Tk, Menu, Canvas, Label, Toplevel, Button, Radiobutton, IntVar


import tkinter.font as tkFont
from tkinter.messagebox import showinfo
from src.jeu import Plateau
from src.jeu import Modele

class Fenetre:
    def __init__(self,modele):
        self.modele = modele
        self.tailleEcranX = 604
        self.tailleEcranY = 700
        self.root = Tk()
        self.root.resizable(width=False,height=False)
        self.root.title("Square Assembler")
        self.root.geometry(str(self.tailleEcranX)+'x'+str(self.tailleEcranY)+'+200+200')
        
        self.win = None
        
        # Menu
        menubar = Menu(self.root)
        # Menu Jeu et ses sous menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nouveau", command=self.fenetreChoix)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=self.root.quit)
        menubar.add_cascade(label="Jeu", menu=filemenu)
        # Menu "A propos" et son sous menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Numéro d'anonymat", command=self.aPropos)
        menubar.add_cascade(label="A propos", menu=editmenu)
        # affichage du menu
        self.root.config(menu=menubar)
        
        # Affichage de la map
        self.taillePlateauX = 600
        self.taillePlateauY = 600
        self.canvasPlateau = Canvas(self.root, width=self.taillePlateauX, height=self.taillePlateauY, borderwidth=0)
        self.canvasPlateau.bind('<Button-1>', self.cliqueGauche)
        self.canvasPlateau.bind('<Button-2>', self.cliqueMolette)
        self.canvasPlateau.bind('<Button-3>', self.cliqueDroit)
        
        # Affichage du score
        self.tailleScoreX = 600
        self.tailleScoreY = 70
        self.canvasScore = Canvas(self.root, width=self.tailleScoreX, height=self.tailleScoreY, borderwidth=0, bg=None)
        
        self.maj()
        
        self.root.mainloop()
        
    def maj(self):                
        self.canvasScore.delete("all")
        
        # Titre
        police = tkFont.Font(family='Impact', size=15)
        self.canvasScore.create_text(self.tailleScoreX/2,15,text="SQUARE",font=police)
        self.canvasScore.create_text(self.tailleScoreX/2,35,text="ASSEMBLER",font=police)
        
        # Affichages des joueurs
        if(self.modele.nbJoueur>=1):
            color="black"
        else:
            color="grey"
        
        self.canvasScore.create_text(100,15,text="1UP",font=police,fill=color)
        self.canvasScore.create_text(100,35,text=self.strScore(1),font=police,fill=color)
            
        if(self.modele.nbJoueur>=2):
            color="black"
        else:
            color="grey"
            
        self.canvasScore.create_text(self.tailleScoreX-100,15,text="2UP",font=police,fill=color)
        self.canvasScore.create_text(self.tailleScoreX-100,35,text=self.strScore(2),font=police,fill=color)
        
        # Ligne de séparation
        self.canvasScore.create_line(0, 50, self.tailleScoreX, 50, width=2)
        
        # Affichage si le jeu est en cours
        if(self.modele.existePlateau()):
            self.canvasPlateau.delete("all")
            
            tailleCarre = self.tailleScoreX/self.modele.tailleX
        
            # Affichage du plateau
            x = 0
            while x<self.modele.tailleX:
                y = 0
                while y<self.modele.tailleY: 
                    self.canvasPlateau.create_rectangle(x*tailleCarre,y*tailleCarre,x*tailleCarre+tailleCarre,y*tailleCarre+tailleCarre,fill=self.modele.plateau.getCouleur(x,y))
                    y = y+1
                x = x+1
            
            # Affichage des carrés de couleurs
            tailleCarre = 14
            y = 54
            
            x = 100-(len(self.modele.listeCouleurJ1)*tailleCarre)/2
            i = 0
            while (i<len(self.modele.listeCouleurJ1)):
                self.canvasScore.create_rectangle(x+tailleCarre*i,y,x+tailleCarre+tailleCarre*i,y+tailleCarre,fill=self.modele.listeCouleurJ1[i])
                i = i+1
            
            x = (self.tailleScoreX-100)-(len(self.modele.listeCouleurJ2*tailleCarre))/2
            i = 0
            while (i<len(self.modele.listeCouleurJ2)):
                self.canvasScore.create_rectangle(x+tailleCarre*i,y,x+tailleCarre+tailleCarre*i,y+tailleCarre,fill=self.modele.listeCouleurJ2[i])
                i = i+1
            
            x = (self.tailleScoreX/2)-(len(self.modele.listeCouleurRestante)*tailleCarre)/2
            i = 0
            while (i<len(self.modele.listeCouleurRestante)):
                self.canvasScore.create_rectangle(x+tailleCarre*i,y,x+tailleCarre+tailleCarre*i,y+tailleCarre,fill=self.modele.listeCouleurRestante[i])
                i = i+1
        
        # Affichage fin de jeu
        

        if(not self.modele.enJeu and self.modele.nbJoueur!=0):
            police = tkFont.Font(family='Impact', size=30)
            self.canvasPlateau.create_text(self.taillePlateauX/2,self.taillePlateauY/2-20,text="FIN DU JEU",font=police)
            
            if(self.modele.nbJoueur==1):
                self.canvasPlateau.create_text(self.taillePlateauX/2,self.taillePlateauY/2+20,text="SCORE FINAL: "+str(self.modele.scoreJ1),font=police)
            
            if(self.modele.nbJoueur==2):
                if(self.modele.scoreJ1>self.modele.scoreJ2):
                    self.canvasPlateau.create_text(self.taillePlateauX/2,self.taillePlateauY/2+20,text="VICTOIRE JOUEUR 1",font=police)
                else:
                    if(self.modele.scoreJ2>self.modele.scoreJ1):
                        self.canvasPlateau.create_text(self.taillePlateauX/2,self.taillePlateauY/2+20,text="VICTOIRE JOUEUR 2",font=police)
                    else:
                        self.canvasPlateau.create_text(self.taillePlateauX/2,self.taillePlateauY/2+20,text="EGALITE",font=police)
                
        
        self.canvasScore.grid(row=0,column=0)
        self.canvasPlateau.grid(row=1,column=0,padx=0)
        
    def strScore(self,joueur):
        tailleMax = 3
        if(joueur==1):
            score = str(self.modele.scoreJ1)
        else:
            score = str(self.modele.scoreJ2)
        
        taille = len(score)
        while(tailleMax-taille>0):
            score = "0"+score
            taille = len(score)
            
        if(self.modele.nbJoueur<joueur):
            score += "/000"
        else:
            score +="/"+str(self.modele.nbCase())
        
        return score
    
    def aPropos(self):
        showinfo("Numéro d'anonymat", "Quentin Morizot / Rémi Pierron")    
    
    def fenetreChoix(self):
        self.win = Toplevel(self.root)
        self.win.geometry('300x260+300+300')
        self.win.title("Changement de plateau")
        
        Label(self.win, text="Choisissez la taille du plateau:", width=41, height=2).grid(row=0,column=0,columnspan=2)
        varTaille = IntVar()
        varTaille.set(0)
        Radiobutton(self.win, width=10, height=3, variable=varTaille, text='10x10', value=10,indicatoron=0).grid(row=1,column=0,padx=0)
        Radiobutton(self.win, width=10, height=3, variable=varTaille, text='20x20', value=20,indicatoron=0).grid(row=1,column=1,padx=0)
        
        Label(self.win, text="Choisissez le nombre de joueur:", width=41, height=2).grid(row=2,column=0,columnspan=2)
        varJoueur = IntVar()
        varJoueur.set(0)
        Radiobutton(self.win, width=10, height=3, variable=varJoueur, text='1 joueur', value=1,indicatoron=0).grid(row=3,column=0)
        Radiobutton(self.win, width=10, height=3, variable=varJoueur, text='2 joueurs', value=2,indicatoron=0).grid(row=3,column=1)
        
        canvasLigne = Canvas(self.win, width=300, height=10)
        canvasLigne.create_line(10, 7, 290, 7)
        canvasLigne.grid(row=4,column=0,columnspan=2)

        Button(self.win,text='VALIDER',command=lambda:self.nouveau(varTaille.get(),varJoueur.get())).grid(row=5,column=0)
        Button(self.win,text='ANNULER',command=self.win.destroy).grid(row=5,column=1)
    
    def nouveau(self,taille,joueur):
        if (taille!=0 and joueur!=0):
            self.modele.nouveauPlateau(taille,taille,joueur)
            self.maj()
            self.win.destroy()
        
    def cliqueGauche(self,event): 
        if(self.modele.enJeu and self.modele.existePlateau()):
            tailleCarre = 600/self.modele.tailleX
            
            x = (int)(event.x/tailleCarre)
            y = (int)(event.y/tailleCarre)
        
            if(x>=0 and x<self.modele.tailleX and y>=0 and y<self.modele.tailleY):
                self.modele.supprimerCase(x,y)
            
            self.maj()
                
    """ Fonction pour tester: à supprimer """
    def cliqueMolette(self,event):
        if(self.modele.existePlateau()):
            tailleCarre = 600/self.modele.tailleX
            
            x = (int)(event.x/tailleCarre)
            y = (int)(event.y/tailleCarre)
        
            self.modele.plateau.l_map[y][x]=0
            self.modele.plateau.gravite()
            self.modele.plateau.decalage()
            self.maj()
            
    def cliqueDroit(self,event):
        if(self.modele.enJeu):
            tailleCarre = 600/self.modele.tailleX
            
            x = (int)(event.x/tailleCarre)
            y = (int)(event.y/tailleCarre)
        
            self.modele.supprimerCase(x,y,2)
            
            self.maj()