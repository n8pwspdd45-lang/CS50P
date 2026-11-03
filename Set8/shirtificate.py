from fpdf import FPDF
from fpdf.enums import XPos, YPos

name = input("Name: ").strip()

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.set_font("helvetica", size=40)
pdf.cell(0, 40, "CS50 Shirtificate", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

img_width = 190
x = (pdf.w - img_width)/2
pdf.image("shirtificate.png", x=x, y=60, w=img_width)

pdf.set_font("helvetica", size=24)
pdf.set_text_color(255, 255, 255)

pdf.set_y(135)
pdf.set_x(0)
pdf.cell(0, 10, text=f"{name} took CS50", align='C')

pdf.output("shirtificate.pdf")
