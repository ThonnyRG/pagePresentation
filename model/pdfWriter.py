import fpdf
import gdown
from docx2pdf import convert
from PyPDF2 import PdfMerger
from datetime import date

todays_date = date.today()
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

currentMonth = months[todays_date.month - 1]
currentYear = todays_date.year

formatDate = f"{currentMonth} {currentYear}"

pdf = fpdf.FPDF(format= "Letter")
pdf.add_page()
pdf.set_font("Arial", size=18)
pdf.cell(0, 50,ln = 2, align = "R")
pdf.cell(0, 10, txt = "Facultad de contaduría y administración", ln = 2, align= "R")
pdf.cell(0, 10, txt = "Región Coatzacoalcos", ln = 1, align= "R")

#Poner en Arial Black
pdf.set_font("Arial", size = 14)
pdf.cell(0, 5, txt = "Lic. en Ingeniería de Software", ln = 2, align = "R")

pdf.set_font("Arial", style = "B", size = 24)
pdf.cell(0, 5, ln = 1, align = "R")
pdf.cell(0, 10, txt = "Nombre de la actividad lorem ipsum", ln = 2, align = "R")

pdf.set_font("Arial", size = 14)
pdf.cell(0, 5, ln = 1, align = "R")
pdf.cell(0, 5, txt = "EE:", ln = 1, align = "R")
pdf.cell(0, 5, txt = "Materia sample eeee lorem ipsum", ln = 2, align = "R")

#Poner en Arial Black
pdf.set_font("Arial", style = "B", size = 16)
pdf.cell(0, 5, ln = 1, align = "R")
pdf.cell(0, 5, txt = "Alumno:", ln = 1, align = "R")
pdf.cell(0, 5, txt = "Balatrexis Nava Moya", ln = 2, align = "R")

pdf.set_font("Arial", size = 16)
pdf.cell(0, 5, ln = 1, align = "R")
pdf.cell(0, 5, txt = "Facilitador:", ln = 1, align = "R")
pdf.cell(0, 5, txt = "Magdiel Omar Mercado Carrillo", ln = 2, align = "R")

# Obtener la fecha
pdf.set_font("Arial", size = 16)
pdf.cell(0, 5, ln = 1, align = "R")
pdf.cell(0, 5, txt = str(formatDate), ln = 1, align = "R")

pdf.set_font("Arial", size = 16)
pdf.cell(0, 5, ln = 1, align = "R")
pdf.cell(0, 5, txt = "Lis de Veracruz: Arte, Ciencia y luz", ln = 1, align = "R")

pdf.image("Model/src/uvLogo.jpg", x = 160, y = 10, w = 45, h = 39)
pdf.image("Model/src/uvFlag.png", x = 0, y = 178, w = 130, h = 100)


pdf.output("test.pdf")

pdfUser = "lorem-ipsum.pdf"

x = ["test.pdf", pdfUser]

merger = PdfMerger()

for pdf in x:
    merger.append(pdf)

merger.write("final.pdf")
merger.close()