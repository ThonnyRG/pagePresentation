from tkmacosx import Button
from tkinter import Tk

class button:
    def __init__(self, frame : Tk):
        self.button = Button(frame)
        self._setFont()
        self._setSize()
        self._setBorderless()
        
        
    def _setFont(self):
        self.button.config(font = "Roboto 20")
        return self
   
    def setText(self, message : str):
        self.button.config(text = message)
        return self
    
    def setForeGround(self, foreGround : str, activeForeGround: str):
        self.button.config(fg = foreGround, activeforeground = activeForeGround)
        return self
    
    def setBackGround(self, background : str, activeBackground: str):
        self.button.config(bg = background, activebackground = activeBackground)
        return self
    
    def _setSize(self):
        self.button.config(padx = 10, pady = 10)
        return self
    
    def _setBorderless(self):
        self.button.config(borderless = 1)
        return self
    
    def setPlace(self, X: int, Y: int):
        self.button.place(x = X, y = Y)
        return self
    
    def setAction(self, cmd):
        self.button.configure(command = cmd)
    
    def setEnabled(self, isEnabled : bool):
        if(isEnabled != True):
            self.button.configure(state = self.button.DISABLED)    
        return self
        
    