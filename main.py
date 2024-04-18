from reportlab.pdfgen import canvas
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfReader, PdfWriter

input_file = PdfReader(open("1.pdf", "rb"))
box = input_file.pages[0].mediabox
print(box)


pdf = FPDF()
pdf.add_page()
pdf.add_font('times', '', fname='times.ttf', uni=True)
pdf.set_font('times', size=11)
x_cord = 130
pdf.x = x_cord
pdf.y = 240

pdf.cell(w=70, h=5, txt='СОГЛАСОВАНО', border=1, align='C', fill=False, ln=1)
pdf.x = x_cord
pdf.cell(w=70, h=5, txt='АО КИС «ИСТОК»', border=1, align='C', fill=False, ln=1)
pdf.x = x_cord
pdf.cell(w=35, h=5, txt='Главный инженер', border=1, align='C', fill=False)
pdf.cell(w=35, h=5, txt='ГИП', border=1, align='C', fill=False, ln=1)
pdf.x = x_cord
pdf.cell(w=35, h=5, txt='Р.Ш. Бичурин', border='LTR', align='C', fill=False)
pdf.cell(w=35, h=5, txt='Ю.В. Смирнов', border='LTR', align='C', fill=False, ln=1)
pdf.x = x_cord
pdf.cell(w=35, h=5, txt='', border='LRB', align='C', fill=False)
pdf.cell(w=35, h=5, txt='', border='LRB', align='C', fill=False, ln=1)
pdf.x = x_cord
pdf.cell(w=35, h=5, txt='Дата', border=1, align='L', fill=False)
pdf.cell(w=35, h=5, txt='Дата', border=1, align='L', fill=False, ln=1)
pdf.x = x_cord
pdf.cell(w=35, h=5, txt='Инв. №', border=1, align='L', fill=False)
pdf.cell(w=17, h=5, txt='Дата', border=1, align='L', fill=False)
pdf.cell(w=18, h=5, txt='Экз.', border=1, align='L', fill=False)
pdf.output(f'watermark.pdf')

watermark = PdfReader(open("watermark.pdf", "rb"))

output_file = PdfWriter()
input_page = input_file.pages[0]
input_page.merge_page(watermark.pages[0])
output_file.add_page(input_page)

for i in range (1, len(input_file.pages)):
    output_file.add_page(input_file.pages[i])


with open("document-output.pdf", "wb") as outputStream:
    output_file.write(outputStream)