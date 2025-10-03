from tkinter import Tk, filedialog

class pathFiles:

    def selectDocFiles():
        root = Tk()
        root.withdraw()
        selectedFiles = filedialog.askopenfilenames(initialdir = "/", title= "Select your document files Files", filetypes = (("pdf files", "*.pdf")))
        
        root.destroy()
            
        return selectedFiles
    
   
        