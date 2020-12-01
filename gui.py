import tkinter
from Pendu import Mot

class gui():
    def __init__(self):
        self.__root = ''
    
    def affMain(self):
        root = Tk() 
        a = Label(root, text ="Hello World") 
        a.pack() 
          
        root.mainloop() 
        
        
        