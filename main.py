from reportlab.pdfgen import canvas
import time
import os
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfReader, PdfWriter


current_folder = input("Введите путь к папке: ")
print(f'Указана папка: {current_folder}')
folder_walk = os.walk(current_folder, onerror=None, followlinks=False)
folder_walk_list = []


for i in folder_walk:
    folder_walk_list.append(i)

try:
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('times', '', fname=r'c:\Windows\Fonts\times.ttf', uni=True)
    pdf.set_font('times', size=11)
    pdf.set_line_width(0.5)
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
    watermark_path = os.path.join(current_folder, 'watermark.pdf')
    pdf.output(watermark_path)


    watermark = PdfReader(open(watermark_path, "rb"))
except Exception as e:
    print(e)

for folder in folder_walk_list:
    print(f'Папка: {folder[0]}')

    for current_file in folder[2]:
        try:
            file_path_full = os.path.join(folder[0], current_file)
            input_file = PdfReader(open(f'{file_path_full}', "rb"))
            output_file = PdfWriter()
            for i in range(2):
                input_page = input_file.pages[i]
                input_page.merge_page(watermark.pages[0])
                output_file.add_page(input_page)


            for i in range(2, len(input_file.pages)):
                output_file.add_page(input_file.pages[i])
            os.chdir(current_folder)
            if not os.path.isdir('approve'):
                os.mkdir('approve')
            file_export_path_full = os.path.join(current_folder, 'approve', current_file)
            with open(file_export_path_full, "wb") as outputStream:
                output_file.write(outputStream)
        except Exception as e:
            print(f'Ошибка выполнения файла {current_file}. {e}')

time.sleep(10)