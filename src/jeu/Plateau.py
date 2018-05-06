import random

class Plateau:
    """Classe définissant le plateau de jeu caractérisée par :
    - sa taille en largeur et hauteur
    - son tableau 2D contenant une référence vers une couleur
    - une liste des couleurs"""

    
    def __init__(self): # Notre méthode constructeur
        self.tailleX = 20
        self.tailleY = 20
        self.nbCouleur = 8 
        self.nbParCouleur = [int((self.tailleX*self.tailleY)/self.nbCouleur)] * self.nbCouleur
        self.listeCouleur = ["red","blue","yellow","green","cyan","magenta","violet","teal"]
        
        self.aleatoire()
                        
    def aleatoire(self):
        self.l_map = [[0]*self.tailleX for i in range(self.tailleY)]
        x = 0
        while x<self.tailleX:
            y = 0
            while y<self.tailleY:
                trouve = False
                while(not trouve):
                    rdm =  random.randint(0,self.nbCouleur-1)
                    print(rdm)
                    if(self.nbParCouleur[rdm]!=0):
                        self.nbParCouleur[rdm] = self.nbParCouleur[rdm]-1
                        self.l_map[y][x] = rdm
                        trouve = True
                y = y+1
            x = x+1
                        
    def getCouleur(self, x, y):
        return self.listeCouleur[self.l_map[y][x]]