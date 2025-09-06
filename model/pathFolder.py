from tkinter import Tk, filedialog

class pathFiles:

    def selectDocFiles():
        selectedFile = filedialog.askopenfilenames(initialdir = "/", title= "Select your pdf FIles", filetypes = (("pdf files", "*.pdf"), ("docx files", "*.docx"), ("doc files", "*.doc"), ("docm files", "*.docm")))
        return selectedFile
    
    
        