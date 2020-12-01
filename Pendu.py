import csv
import random
import codecs


class Mot:
    def __init__(self):
        self.ortho = ""
        self.taille = len(self.ortho)
        self.winning = True
        self.essais = []
        self.fautes = 0
    
    def getRandom(self):
        liste_mot = self.openFile()
        rand = random.randint(0,len(liste_mot)-1)
        return liste_mot[rand]
    
    def openFile(self):
        f = codecs.open('liste_francais.txt', 'r', encoding='latin-1')
        content = f.readlines()
        liste_ren = []
        for element in content:
            word = element[:-2].lower()
            liste_ren.append(word)
        return liste_ren
    
    def play(self):
        print("Bonjour et bienvenu dans ce programme modélsant un pendu")
        print("Essayez de deviner le mot suivant, faisant partie d'un des mots du dictionnaires")
        
        self.ortho = self.getRandom()
        
        while self.winning:
            self.winning = self.mot_cache()
            if not self.winning:
                break            
            self.proposition()
            self.winning = self.pendu()        
        
    def mot_cache(self):
        cache = ''
        for lettre in self.ortho:
            if lettre in self.essais or lettre == '-' or lettre == ' ' or lettre == "'":
                print(lettre, end='')
                cache += lettre
            else:
                print("_", end='')
                cache += "_"
        print()
        print()
        print(self.essais)
        if cache == self.ortho:
            return False
        else:
            return True

    def proposition(self):
        print("Quelle lettre pense-tu qu'il y ai dans le mot  ?")
        lettre = input()
        print()
        if lettre not in self.ortho:
            self.fautes += 1
        if lettre not in self.essais:
            self.essais.append(lettre)

    def pendu(self):
        if self.fautes == 0:
            print("")
        elif self.fautes == 1:
            print("")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 2:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 3:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |")
            print("    |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 4:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |        |")
            print("    |        |")
            print("    |")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 5:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |        |")
            print("    |        |")
            print("    |       / \\")
            print("    |")
            print("___/|\\___")
        elif self.fautes == 6:
            print("     _________")
            print("    |/       |")
            print("    |        |")
            print("    |        O")
            print("    |       \\|/")
            print("    |        |")
            print("    |       / \\")
            print("    |")
            print("___/|\\___")
            print()
            print(self.ortho)
            print()
            print("Eh, t'as perdu.")
            return False
        print()
        return True

