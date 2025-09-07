from PyPDF2 import PdfMerger


class pdfMerger:
    def __init__(self, pdfs: list[str]):
        self.pdfs = pdfs
        self.merger = PdfMerger()
        self._mergerFiles()
        
    def _mergerFiles(self):
        for pdf in self.pdfs:
            self.merger.append(pdf)
        self.merger.write("final.pdf")
        self.merger.close()    
    