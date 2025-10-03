from datetime import date
from model.Data.settings import settings
from model.Data.universityData import universityData
from model.pdfCoverGenerator import pdfCoverGenerator
from model.pdfMerger import pdfMerger
from view.pathFiles import pathFiles


def main():
    
    ActivityName = "Actividad inutil"
    EEName = "Materia Inutil"
    NameUser = "Balatrexis Nava Moya"
    FacilitatorName = "Magdiel Market"
    
    a = pdfCoverGenerator(settings, universityData, ActivityName, EEName, NameUser, FacilitatorName, date.today())
    a.generate()
    
    pdflist = pathFiles.selectDocFiles()
    print(type(pdflist))
    pdflist = list(pdflist)
    pdflist.insert(0, "cover.pdf")
    print(pdflist)
    pdfMerger(pdflist)
  
if __name__ == '__main__':
    main()