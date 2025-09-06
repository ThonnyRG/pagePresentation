from datetime import date
from fpdf import FPDF
from model.Data.dateFormatter import dateFormatter
from model.Data.universityData import universityData
from model.Data.settings import settings

class pdfCoverGenerator:
    def __init__(self, settings: settings, universityData: universityData, activityName: str, experienceInfo: str, studentName: str, facilitatorName: str, dateToday: date):
        self.settings = settings
        self.universityData = universityData
        self.activityName =activityName
        self.experienceInfo = experienceInfo
        self.studentName = studentName
        self.facilitatorName = facilitatorName
        self.dateToday = dateToday
    
    def generate(self):
        pdf = FPDF(format = self.settings.PDF_FORMAT)
        pdf.add_page()
        self._addHeader(pdf)
        self._activityTittle(pdf)        
        self._experienceInfo(pdf)        
        self._studentInfo(pdf)
        self._facilitatorInfo(pdf)
        self._dateInfo(pdf)
        self._univMottoInfo(pdf)
        self._setImages(pdf)
        self._outuputUser(pdf)
       
    def _addHeader(self, pdf: FPDF):
        pdf.set_font(self.settings.DEFAULT_FONT, size = 18)
        pdf.cell(0, 50,ln = 2, align = "R")
        pdf.cell(0, 10,txt = self.universityData.FACULTY, ln = 2, align = "R")
        pdf.cell(0, 10,txt = self.universityData.REGION, ln = 1, align = "R")
        
        pdf.set_font(self.settings.DEFAULT_FONT, size= 14)
        pdf.cell(0, 5, txt = self.universityData.CAREER, ln = 2, align = "R")

    # Activity tittle
    def _activityTittle(self, pdf: FPDF):
        pdf.set_font(self.settings.DEFAULT_FONT, style= "B", size=24)
        pdf.cell(0, 5, ln = 1, align = "R" )
        pdf.cell(0, 10, txt = self.activityName, ln= 2, align = "R")
    #courseInfo
    def _experienceInfo(self, pdf: FPDF):
        pdf.set_font(self.settings.DEFAULT_FONT, size = 14)
        pdf.cell(0, 5, ln = 1, align = "R")
        pdf.cell(0, 5, txt = "EE:",ln = 1, align = "R")
        pdf.cell(0, 5, txt = self.experienceInfo, ln = 2, align = "R")
    #studentInfo
    def _studentInfo(self, pdf: FPDF):
        pdf.set_font(self.settings.DEFAULT_FONT, style = "B" ,size = 16)
        pdf.cell(0, 5, ln = 1,align = "R")
        pdf.cell(0, 5,txt = "Alumno:", ln = 1,align = "R")
        pdf.cell(0, 5,txt = self.studentName, ln =  2,align = "R")
        
    #16
    def _facilitatorInfo(self, pdf: FPDF):
        pdf.set_font(self.settings.DEFAULT_FONT, size= 16)
        pdf.cell(0, 5,ln = 1 , align= "R")
        pdf.cell(0, 5, txt = "Faclitador:" ,ln = 1 , align= "R")
        pdf.cell(0, 5, txt = self.facilitatorName ,ln = 2 , align= "R")
        
    #Date 16
    def _dateInfo(self, pdf: FPDF):
        date = dateFormatter.formatDateInSpanish(self.dateToday)
        pdf.set_font(self.settings.DEFAULT_FONT, size = 16)
        pdf.cell(0, 5, ln = 1, align = "R")
        pdf.cell(0, 5, txt = date,ln = 1, align = "R")
    
    #Univ motto 16
    def _univMottoInfo(self, pdf: FPDF): 
        pdf.set_font(self.settings.DEFAULT_FONT, size = 16)
        pdf.cell(0, 5, ln = 1, align = "R")
        pdf.cell(0, 5, txt = self.universityData.MOTTO , ln = 1, align = "R")
    #Images
    def _setImages(self, pdf: FPDF):
        logoPos = self.settings.LOGO_POSITION
        flagPos = self.settings.FLAG_POSITION
        
        if self.settings.UV_FLAG_PATH.exists():
            pdf.image(str(self.settings.UV_FLAG_PATH), **flagPos)
        if self.settings.UV_LOGO_PATH.exists():
            pdf.image(str(self.settings.UV_LOGO_PATH), **logoPos)
            
    def _outuputUser(self, pdf: FPDF):
        pdf.output("cover.pdf")
    