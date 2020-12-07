import csv
import random
import codecs

class mot:
    def __init__(self):
        self.__mot = self.getRandom()
        self.__essais = []
        self.__echecs = 0

    def getRandom(self):
        liste_mot = self.openFile()
        rand = random.randint(0,len(liste_mot)-1)
        return liste_mot[rand]

    def getMot(self):
        return  self.__mot
    
    def getEssais(self):
        return self.__essais
    
    def addEchec(self):
        self.__echecs += 1
    
    def getEchecs(self):
        return self.__echecs
    
    def addEssais(self, lettre):
        if lettre not in self.__essais:
            self.__essais.append(lettre)
    
    def getMotCache(self):
        cache = ''
        for lettre in self.__mot:
            if lettre  == '-' or lettre == ' ' or lettre == "'":
                print(lettre, end='')
                cache += lettre
            else:
                print("_", end='')
                cache += "_"
        return cache
    
    def changeMotCache(self,choix):
        cache = ''
        for lettre in self.__mot:
            if (lettre in self.__essais) or (lettre == '-') or (lettre == ' ') or (lettre == "'"):
                cache += lettre
            else:
                print("_", end='')
                cache += "_"
        return cache
    
    def openFile(self):
        f = codecs.open('liste_francais.txt', 'r', encoding='latin-1')
        content = f.readlines()
        liste_ren = []
        for element in content:
            word = element[:-2].lower()
            liste_ren.append(word)
        return liste_ren