import os, sys  # Standard Python Libraries
from docxtpl import DocxTemplate, InlineImage  # pip install docxtpl
from docx2pdf import convert
import datetime as tarih
from openpyxl import Workbook,load_workbook

wb = load_workbook("katilimcilar.xlsx")
ws = wb.active

# Aktif çalışma sayfasının adını yazdırma
print(wb.sheetnames)
for x in range(2, 3):
  adiSoyadi = ws.cell(x,2).value
  os.chdir(sys.path[0])
  doc = DocxTemplate("Template.docx")
  an = tarih.datetime.now()
  context = {
      "adsoyad": adiSoyadi,
      "baslik": "Bilmem ne Bildiri Adi",
      "universite": "Batman Üniversitesi",
      "tarih": tarih.datetime.strftime(an, '%d %B %Y')
  }

  doc.render(context)
  dokumanAdi = adiSoyadi + ".docx";
  doc.save(dokumanAdi)
  convert(dokumanAdi, adiSoyadi+".pdf")
