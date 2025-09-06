from datetime import date

class dateFormatter:
    MONTHS = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    @classmethod
    def formatDateInSpanish(cls, targetDate: date):
        month = cls.MONTHS[targetDate.month - 1]
        return f"{month} {targetDate.year}"
    