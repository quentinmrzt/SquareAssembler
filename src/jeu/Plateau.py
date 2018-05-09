import random

class Plateau:
    """Classe définissant le plateau de jeu caractérisée par :
    - sa taille en largeur et hauteur
    - son tableau 2D contenant une référence vers une couleur
    - une liste des couleurs"""

    def __init__(self, x=20,y=20): # Notre méthode constructeur
        self.tailleX = x
        self.tailleY = y
        self.nbCouleur = int(x/2.5)
        self.listeCouleur = ["white","red","blue","yellow","green","cyan","magenta","violet","orange"]
        
        self.aleatoire()

                        
    def aleatoire(self):
        nbParCouleur = [int((self.tailleX*self.tailleY)/self.nbCouleur)] * self.nbCouleur
        
        self.l_map = [[0]*self.tailleX for i in range(self.tailleY)]
        x = 0
        while x<self.tailleX:
            y = 0
            while y<self.tailleY:
                trouve = False
                while(not trouve):
                    rdm =  random.randint(1,self.nbCouleur)
                    if(nbParCouleur[rdm-1]!=0):
                        nbParCouleur[rdm-1] = nbParCouleur[rdm-1]-1
                        self.l_map[y][x] = rdm
                        trouve = True
                y = y+1
            x = x+1

    def getCouleur(self, x, y):
        return self.listeCouleur[self.l_map[y][x]]
    
    def marquage(self,x,y):
        self.l_map[y][x] = -self.l_map[y][x]
    def demarquage(self):
        x=0
        while(x<self.tailleX):
            y=0
            while(y<self.tailleY):
                if(self.l_map[y][x] < 0):
                    self.l_map[y][x] = self.l_map[y][x]*-1
                y = y+1
            x = x+1
    
    def nbSupprimable(self,x,y):
        if(self.l_map[y][x] == 0):
            return 0
        else:
            nbVoisin = self.parcoursProfondeurNbVoisin(x,y)
            self.demarquage()
            if (nbVoisin>=3):
                return nbVoisin
            else:
                return 0
    
    def parcoursProfondeurNbVoisin(self,x,y):
        couleur = self.l_map[y][x]
        nbVoisin = 1
        self.marquage(x, y)
        
        if(y>0 and self.l_map[y-1][x]==couleur): # en haut
            nbVoisin += self.parcoursProfondeurNbVoisin(x, y-1)
                
        if(x<self.tailleX-1 and self.l_map[y][x+1]==couleur): # à droite
            nbVoisin += self.parcoursProfondeurNbVoisin(x+1, y)
                
        if(y<self.tailleY-1 and self.l_map[y+1][x]==couleur): # en bas
            nbVoisin += self.parcoursProfondeurNbVoisin(x, y+1)
                
        if(x>0 and self.l_map[y][x-1]==couleur): # à gauche
            nbVoisin += self.parcoursProfondeurNbVoisin(x-1, y)

        return nbVoisin
    
    
    def supprime(self,x,y):
        nb = self.nbSupprimable(x,y)
        if(nb!=0):
            self.parcoursProfondeurSupprime(x,y)
            
        return nb
    
    def parcoursProfondeurSupprime(self,x,y):
        couleur = self.l_map[y][x]
        self.l_map[y][x] = 0
        
        if(y>0 and self.l_map[y-1][x]==couleur): # en haut
            self.parcoursProfondeurSupprime(x, y-1)
                
        if(x<self.tailleX-1 and self.l_map[y][x+1]==couleur): # à droite
            self.parcoursProfondeurSupprime(x+1, y)
                
        if(y<self.tailleY-1 and self.l_map[y+1][x]==couleur): # en bas
            self.parcoursProfondeurSupprime(x, y+1)
                
        if(x>0 and self.l_map[y][x-1]==couleur): # à gauche
            self.parcoursProfondeurSupprime(x-1, y)
            
    def gravite(self):
        y = self.tailleY-1

        while(y>=0):
            x = 0
            while(x<self.tailleX):
                if(self.l_map[y][x] == 0):
                    posY = y
                    while(posY>=0 and self.l_map[posY][x] == 0):
                        posY = posY-1
                    
                    if(posY>=0):
                        self.l_map[y][x] = self.l_map[posY][x]
                        self.l_map[posY][x] = 0
                x = x+1
            y = y - 1
            
    def decalage(self):
        y = self.tailleY-1
        x = 0
        decalage = 0
        
        while(x<self.tailleX):
            i = y
            if(self.l_map[y][x]!=0 and decalage!=0):
                while(i>=0):
                    self.l_map[i][x-decalage] = self.l_map[i][x]
                    self.l_map[i][x] = 0
                    i = i-1
            else:
                ligneVide=True
                while(i>=0 and ligneVide):
                    if(self.l_map[i][x] != 0):
                        ligneVide = False
                    i = i-1
    
                if(ligneVide):
                    decalage = decalage + 1
            x = x+1
            
    def estJouable(self):
        x = 0
        jouable = False

        while (not jouable and x<self.tailleX):
            y = 0
            while (not jouable and y<self.tailleY):
                if(self.nbSupprimable(x,y)!=0):
                    jouable = True
                y = y+1
            x = x+1
            
        return jouable