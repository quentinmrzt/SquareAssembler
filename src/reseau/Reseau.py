import os, string, sys, time, getopt
sys.path.append ("C:\ivy-python-2.1")
from ivy.std_api import *

class Reseau:
    def __init__(self):
        self.nom = "Joueur"
        self.message = ""
        self.estConnecte = False

        
    def on_msg(self, agent, *arg):        
        if(self.estConnecte):
            self.message = str(arg)
            self.maj()
        
        if ("is ready" in str(arg)):
            self.estConnecte = True
            
    def on_connection_change(self, agent, event):
        if event == IvyApplicationDisconnected :
            self.estConnecte = False
    
    def on_die(self, agent, id):
        IvyStop()

    def envoyer(self, message):
        IvySendMsg(message)
    
    def connexion(self):        
        print("CONNEXION")
        # initialising the bus 
        readymsg = '[%s is ready]' % self.nom
        
        IvyInit(self.nom, readymsg, 0, self.on_connection_change, self.on_die)

        # starting the bus
        IvyStart("127.0.0.1:2010")
        
        # bind the supplied regexps
        IvyBindMsg(self.on_msg, "(.*)")