#-*-coding: Latin-1-*-
from tkinter import *
from tkinter.messagebox import showinfo


root = Tk()
root.title("Square Assembler")
root.geometry('500x500+200+200')

def aPropos():
    showinfo("Numéro d'anonymat", "Quentin Morizot")

    
def nouveau():
    print("Rien de nouveau")

menubar = Menu(root)

# Menu Jeu et ses sous menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=nouveau)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.quit)
menubar.add_cascade(label="Jeu", menu=filemenu)

# Menu "A propos" et ses sous menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Numéro d'anonymat", command=aPropos)
menubar.add_cascade(label="A propos", menu=editmenu)

# affichage du menu
root.config(menu=menubar)

root.mainloop()