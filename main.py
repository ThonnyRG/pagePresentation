from datetime import date
from model.Data.settings import settings
from model.Data.universityData import universityData
from model.pdfCoverGenerator import pdfCoverGenerator


def main():
    a = pdfCoverGenerator(settings, universityData, "Ejmplo Lorem", "Materia Inutil de Vergara", "Balatrexis Nava Moya", "Magdiel Market", date.today())
    a.generate()
   
if __name__ == '__main__':
    main()