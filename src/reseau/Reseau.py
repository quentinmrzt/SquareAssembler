import os, string, sys, time, getopt
sys.path.append ("C:\ivy-python-2.1")
from ivy.std_api import *
import time

class Reseau:
    def __init__(self, nom):
        self.nom = nom
        self.nomAdversaire = None
        self.temps = time.time()
        
        self.adresse = "127.0.0.1"
        self.port = "2010"
        
        self.message = ""
        
        self.estConnecte = False
        self.estServeur = False
        self.estPret = False
        
        self.aDuree = False
        self.aTaille = False
        self.aPlateau = False
        
        self.dureeTour = 0
        self.taille = 0
        self.map = []
        
        self.click = False
        self.x = None
        self.y = None
        
        self.passerTour = False
        
    def on_msg(self, agent, *arg):
        #print('Received from %r: %s', agent, arg and str(arg) or '<no args>')
        
        if(self.estConnecte):
            self.message = str(arg)
        
        if ("is ready" in str(arg)):
            self.estConnecte = True
            self.envoyer("time: "+str(self.temps)+" ")
            
        # Qui est le serveur
        if ("nom:" in str(arg)):
            if(self.nomAdversaire==None):
                self.envoyer("nom: "+self.nom+" ")
                
            test1 = str(arg)
            test2 = test1.split(' ')
            test3 = test2[1]

            self.nomAdversaire = test3
                    
        if("time:" in str(arg)):
            test1 = str(arg)
            test2 = test1.split(' ')
            test3 = test2[1]
            test4 = float(test3)
            
            if(test4<self.temps):
                self.estServeur = False
            else:
                self.estServeur = True
            
            self.estPret = True
        
        # Pour récupérer la durée d'un tour
        if("tour:" in str(arg)):
            test1 = str(arg)
            test2 = test1.split(' ')
            test3 = test2[1]
            test4 = int(test3)
            
            self.dureeTour = test4
            self.aDuree = True
        
        # Pour récupérer la taille
        if("taille:" in str(arg)):
            test1 = str(arg)
            test2 = test1.split(' ')
            test3 = test2[1]
            test4 = int(test3)
            
            self.taille = test4
            self.aTaille = True
            
        if("map:" in str(arg)):
            test1 = str(arg)
            test2 = test1.replace("map:", "").replace("[", "").replace("]", "").replace("'", "").replace("(", "")
            test2 = test2.split(',')
            
            i = 0
            while (i<self.taille*self.taille):
                self.map.append(int(test2[i]))
                i += 1
            self.aPlateau = True
            
        if("Infos ok" in str(arg)):
            self.aDuree = True
            self.aTaille = True
            self.aPlateau = True
            
        if("click:" in str(arg)):
            test1 = str(arg)
            test2 = test1.split(' ')
            self.x = int(test2[1])
            self.y = int(test2[2])
                        
            self.click = True
            
        if("passer tour" in str(arg)):
            print("on passe le tour")
            self.passerTour = True
           
    def aInformation(self):
        return self.dureeTour and self.aTaille and self.aPlateau and self.nomAdversaire!=None
            
    def on_connection_change(self, agent, event):
        if event == IvyApplicationDisconnected :
            self.estConnecte = False
        else:
            print("quelqu'un c'est co")
    
    def on_die(self):
        IvyStop()

    def envoyer(self, message):
        IvySendMsg(message)
    
    def connexion(self):        
        print("CONNEXION")
        # initialising the bus 
        readymsg = '[%s is ready]' % self.nom
        
        IvyInit(self.nom, readymsg, 0, self.on_connection_change, self.on_die)

        # starting the bus
        IvyStart(self.adresse+":"+self.port)
        
        # bind the supplied regexps
        IvyBindMsg(self.on_msg, "(.*)")