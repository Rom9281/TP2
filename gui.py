# Romain GAUD
# 8/12/2020
# Objectif :
#


import tkinter as tk
import mot

class gui():
    def __init__(self):
        self.__main = ''    #Definition  de la fentre principale
        self.__jeu = ''     #Definition de la fenetre du jeu

        # Definition d'une liste de lettres authorisee:
        self.__auth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','é','è','î','ê','û','ë','ô','']
        
        self.__mot = mot.mot()  #Definition de l'objet mot qui a pour but de traiter en arriere plan 
        self.__cache = self.__mot.getMotCache()     #Definition du mot cache ex: ____-____ : se decouvre progressivemeent pour devenir un mot apparent

        self.__label_essais = "\n"  #label indiquant les differents essaies de lettres
        self.__label_nb_echecs = "\n"   #label indiquant le nombre d'echecs
        self.__label_error = ""
        self.__b_retour = ''

        #Creation du label d'affichage et de la valeur d'entree
        self.__label_c = ''     #Label du mot cache
        self.__choix = ''   #choix de la lettre de la pesonne
        self.__boutton = ''  #definition du boutton permettant de valider son choix

        self.__option = ''  #Definition de la fenetre de l'option

        self.__nb_echecs = 3    #Nombres d'echecs authorises
    
    def affMain(self):
        if self.__jeu != '':
            self.__jeu.destroy()
            self.__jeu = ""
        
        if self.__option != '':
            self.__option.destroy()
            self.__option = ""
        
        self.__main = tk.Tk()   #creation de la fenetre principale
        self.__main.geometry("400x300")     #Definition de la geometrie de la fenetre principal
        a = tk.Label(self.__main, text ="Pendu")     #Ajout du label du jeu
        a.pack()

        jouer = tk.Button(self.__main,text = 'Jouer',command = self.affJeu) #Ajout du boutton pour acceder a l'interface du jeu
        jouer.pack()

        Options = tk.Button(self.__main,text = 'Option',command = self.affOption) #Ajout du boutton pour acceder a l'interface du jeu
        Options.pack()
        self.__main.mainloop()  #initialisation de la boucle d'affichage
    
    def affOption(self):
        self.__main.destroy()
        self.__main = ''
        self.__option = tk.Tk()
        

        a = tk.Label(self.__option, text ="Ecrire le nombre de chances maximums : ")     #Ajout du label du jeu
        a.pack()

        self.__choix = tk.Entry(self.__option, text ="Entrer la valeur")
        self.__choix.pack()

        self.__b_retour = tk.Button(self.__option, text ="Retour au menu",command = self.affMain)
        self.__b_retour.pack()

        self.__option.mainloop()
    
    def affJeu(self):
        self.__main.destroy()   #Detruit la fenetre principale
        self.__main = ''
        self.__jeu = tk.Tk()    #Creation d'une nouvelle fenetre
        self.__jeu.geometry("150x300")  #Definition de la geometrie de la fenetre

        self.__label_c = tk.Label(self.__jeu, text = self.__cache)  #Initialisation du label du mot cache avec un contenu non null
        self.__label_c.bind('<Return>', self.getLettre)     #Creation d'une liaison entre le label et la fonction getLettre
        self.__label_c.pack()

        """
        img = ImageTk.PhotoImage(Image.open('hm_2.gif'))
        panel = tk.Label(self.__jeu, image = img)
        
        panel.pack(side = "bottom", fill = "both", expand = "yes")

        tk.Label(self.__jeu, text = "Tentatives : ").pack()"""

        self.__label_essais = tk.Label(self.__jeu, text = "")
        self.__label_essais.bind('<Return>', self.changeEssais)
        self.__label_essais.pack()

        tk.Label(self.__jeu, text = "Nombres d'echecs : ").pack()

        self.__label_nb_echecs = tk.Label(self.__jeu, text = "0")
        self.__label_nb_echecs.bind('<Return>', self.changeEssais)
        self.__label_nb_echecs.pack()

        self.__choix = tk.Entry(self.__jeu, text ="Entrer la lettre")
        self.__choix.pack()

        self.__boutton = tk.Button(self.__jeu, text ="Valider", command = self.verifyEntry)
        self.__boutton.bind('<Return>', self.changeBoutton)
        self.__boutton.pack()

        self.__label_error = tk.Label(self.__jeu, text = "")
        self.__label_error.bind('<Return>', self.changeEssais)
        self.__label_error.pack()

        self.__b_retour = tk.Button(self.__jeu, text ="Retour au menu",command = self.affMain)
        self.__b_retour.pack()

        self.__jeu.mainloop()
    
    def verifyEntry(self):
        lettre = self.__choix.get()
        if self.__mot.getEchecs() <= self.__nb_echecs:   #Si le nombre d'echecs est inferieur au nombre authorises
            if lettre in self.__auth:   #Si la lettre est dans la liste d'entrees authoriser, continuer
                self.eraseError()
                self.getLettre()
            else:
                self.changeError()
        else:
            self.changeBoutton()    #Si le nombre d'echecs est sup au nombre authorise, changer le boutton en text
    
    def getLettre(self):
        lettre = self.__choix.get()
        self.__mot.addEssais(lettre)
        if (lettre in self.__mot.getMot()) :
            self.changeCache(lettre)
        else:
            self.__mot.addEchec()
        self.changeEssais()
    
    #_________________ INTERACTION FENETRE _______________
    
    def changeCache(self, variable):
        self.__cache = self.__mot.changeMotCache(variable)
        self.__label_c['text'] = self.__cache
    
    def changeEssais(self):
        liste_e = self.__mot.getEssais()
        nombre_e = self.__mot.getEchecs()
        self.__label_essais['text'] += liste_e[-1]
        self.__label_essais['text'] += "-"
        self.__label_nb_echecs['text'] = str(nombre_e)
    
    def changeBoutton(self):
        self.__boutton.destroy()
        self.__boutton = tk.Label(self.__jeu, text = "Vous avez perdu...");
        self.__boutton.pack()

    def changeError(self):
        self.__label_error['text'] = "Erreur: la variable lettre est invalide"
    
    def eraseError(self):
        self.__label_error['text'] = ""


        


        
        
        