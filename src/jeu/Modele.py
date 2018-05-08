from src.jeu import Plateau

class Modele:
    def __init__(self):
        self.score = 0
        self.plateau = None
        self.tailleX = 0
        self.tailleY = 0

    def existePlateau(self):
        return (self.plateau!=None)
    
    def supprimerCase(self,x,y):
        self.score += self.plateau.supprime(x,y)
        self.plateau.gravite()
        self.plateau.decalage()
            
        if (not self.plateau.estJouable()):
            self.plateau = None
            
    def nouveauPlateau(self,x,y):
        self.tailleX = x
        self.tailleY = y
        self.plateau = Plateau.Plateau(x,y)
        self.score = 0