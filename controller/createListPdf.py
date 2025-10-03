
from model.pdfMerger import pdfMerger
from view.pathFiles import pathFiles


class createListPdf:
    def __init__(self):
        self._createList()
        
    def _createList():
        pdfList = pathFiles.selectDocFiles()
        pdflist = list(pdflist)
        pdflist.insert(0, "cover.pdf")
        pdfMerger()