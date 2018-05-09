from src.jeu import Plateau

class Modele:
    def __init__(self,nbJoueur=0):
        self.scoreJ1 = 0
        self.listeCouleurJ1 = []
        self.scoreJ2 = 0
        self.listeCouleurJ2 = []
        
        self.listeCouleurRestante = []
        
        self.nbJoueur = nbJoueur
        
        self.enJeu = False
        
        self.plateau = None
        self.tailleX = 0
        self.tailleY = 0
        
        self.tourDeJeu = None

    def existePlateau(self):
        return (self.plateau!=None)
    
    
    
    def estMaCouleur(self,couleur,joueur=1):
        if(joueur==1):
            return couleur in self.listeCouleurJ1 or (couleur in self.listeCouleurRestante and len(self.listeCouleurJ1)<self.plateau.nbCouleur/2)
        else:
            return couleur in self.listeCouleurJ2 or (couleur in self.listeCouleurRestante and len(self.listeCouleurJ2)<self.plateau.nbCouleur/2)
        
    def ajouterCouleurJ1(self, couleur):
        if(len(self.listeCouleurJ1) < self.plateau.nbCouleur/2):
            if(couleur in self.listeCouleurRestante):
                self.listeCouleurJ1.append(couleur)
                self.listeCouleurRestante.remove(couleur)
        
    def ajouterCouleurJ2(self, couleur):
        if(len(self.listeCouleurJ2) < self.plateau.nbCouleur/2):
            if(couleur in self.listeCouleurRestante):
                self.listeCouleurJ2.append(couleur)
                self.listeCouleurRestante.remove(couleur)

    
    def supprimerCase(self,x,y,joueur=1):
        couleur = self.plateau.getCouleur(x,y)
        if(couleur=="white"):
            return False
        else:
            caseSupprime = False
            
            if(joueur==1):
                if(self.nbJoueur==1):
                    scoreTmp = self.plateau.supprime(x,y)
                    if(scoreTmp!=0):
                        self.scoreJ1 += scoreTmp
                        caseSupprime = True
                else:
                    # 2 joueurs, donc on prend en compte la couleur
                    if(self.estMaCouleur(couleur,1)):
                        scoreTmp = self.plateau.supprime(x,y)
        
                        if(scoreTmp!=0):
                            self.scoreJ1 += scoreTmp
                            self.ajouterCouleurJ1(couleur)
                            caseSupprime = True
            else:
                if(joueur==2 and self.nbJoueur==2):
                    if(self.estMaCouleur(couleur,2)):                   
                        scoreTmp = self.plateau.supprime(x,y)
        
                        if(scoreTmp!=0):
                            self.scoreJ2 += scoreTmp
                            self.ajouterCouleurJ2(couleur)
                            caseSupprime = True
            
            self.plateau.gravite()
            self.plateau.decalage()
                
            if (not self.plateau.estJouable()):
                self.enJeu = False
            
            return caseSupprime
            
    def nouveauPlateau(self,x,y,nb):
        self.nbJoueur = nb
        self.enJeu = True
        
        self.tailleX = x
        self.tailleY = y
        self.plateau = Plateau.Plateau(x,y)
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        self.tourDeJeu = 1
        
        self.listeCouleurJ1.clear()
        self.listeCouleurJ2.clear()
        self.listeCouleurRestante.clear()
        
        i = 1
        while(i<=self.plateau.nbCouleur):
            self.listeCouleurRestante.append(self.plateau.listeCouleur[i])
            i = i+1
        
    def nbCase(self):
        return self.tailleX*self.tailleY