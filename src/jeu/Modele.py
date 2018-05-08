from src.jeu import Plateau

class Modele:
    def __init__(self,nbJoueur=2):
        
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        
        self.nbJoueur = nbJoueur
        
        self.plateau = None
        self.tailleX = 0
        self.tailleY = 0

    def existePlateau(self):
        return (self.plateau!=None)
    
    def supprimerCase(self,x,y,joueur=1):
        if(joueur==1):
            self.scoreJ1 += self.plateau.supprime(x,y)
        else:
            if(joueur==2 and self.nbJoueur>=2):
                self.scoreJ2 += self.plateau.supprime(x,y)
        
        self.plateau.gravite()
        self.plateau.decalage()
            
        if (not self.plateau.estJouable()):
            self.plateau = None
            
    def nouveauPlateau(self,x,y,nb):
        self.nbJoueur = nb
        
        self.tailleX = x
        self.tailleY = y
        self.plateau = Plateau.Plateau(x,y)
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        
    def nbCase(self):
        return self.tailleX*self.tailleY