from tkinter import Tk, filedialog

class pathFiles:

    def selectDocFiles():
        root = Tk()
        root.withdraw()
        selectedFiles = filedialog.askopenfilenames(initialdir = "/", title= "Select your document files Files", filetypes = (("pdf files", "*.pdf"), ("docx files", "*.docx"), ("doc files", "*.doc"), ("docm files", "*.docm")))
        
        root.destroy()
            
        return selectedFiles
    
   
        