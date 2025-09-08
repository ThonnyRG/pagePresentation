from tkinter import Tk

class frm:
    def __init__(self):
        self.root = Tk()
        self._setSize()
        self._setBackground()
        self._defaultResizable()
        
        
    def _setSize(self):
        self.root.geometry("500x200")
        return self
    
    def setTitle(self, title: str):
        self.root.title(title)
        
    def _defaultResizable(self):
        self.root.resizable(width = False, height = False)
        return self
    
    def _setBackground(self):
        self.root.configure(bg = "#222222")
        return self
        
    def show(self):
        self.root.mainloop()
       
    def close(self):
        self.root.destroy() 
        
    def getRoot(self):
        return self.root