from src.jeu import Plateau

class Modele:
    def __init__(self,nbJoueur=0):
        self.scoreJ1 = 0
        self.listeCouleurJ1 = []
        self.scoreJ2 = 0
        self.listeCouleurJ2 = []
        
        self.listeCouleurRestante = []
        
        self.nombrePartie = 0
                
        self.nbJoueur = nbJoueur
        
        self.enJeu = False
                
        self.plateau = None
        self.tailleX = 0
        self.tailleY = 0
        
        self.tourDeJeu = None
        
        self.joueurNumero = 0

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
    
    def changementJoueur(self):
        if(self.tourDeJeu == 1):
            self.tourDeJeu = 2
        else:
            self.tourDeJeu = 1
                
    def passerTour(self):
        if(self.nbJoueur==2 and self.enJeu):
            if(self.tourDeJeu==1):
                if(self.plateau.estJouableTest(self.listeCouleurJ2+self.listeCouleurRestante)):
                    self.changementJoueur()
                    return True
                else:
                    return False
            else:
                if(self.plateau.estJouableTest(self.listeCouleurJ1+self.listeCouleurRestante)):
                    self.changementJoueur()
                    return True
                else:
                    return False
        else:
            return True
                    
    def nouveauPlateau(self,x,y,nb):
        self.enJeu = True
        self.nombrePartie += 1
        self.nbJoueur = nb

        self.tailleX = x
        self.tailleY = y
        
        self.plateau = Plateau.Plateau(x,y)
        self.plateau.aleatoire()
        
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
    
    def supprimerPlateau(self):
        self.enJeu = False
        self.plateau = None
        
        self.scoreJ1 = 0
        self.listeCouleurJ1 = []
        self.scoreJ2 = 0
        self.listeCouleurJ2 = []
        
        self.listeCouleurRestante = []
                
        self.nbJoueur = 0
        self.joueurNumero = 0
        
        self.enJeu = False
                
        self.tailleX = 0
        self.tailleY = 0
        
        self.tourDeJeu = None
    
    
    def nouveauPlateauListe(self, taille, listeMap):
        self.enJeu = True
        self.nombrePartie += 1
        self.nbJoueur = 2

        self.tailleX = taille
        self.tailleY = taille
        
        self.plateau = Plateau.Plateau(self.tailleX, self.tailleY)
        self.plateau.listePlateau(listeMap)
        
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