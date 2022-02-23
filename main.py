import datetime
import os, sys  # Standard Python Libraries
from docxtpl import DocxTemplate, InlineImage  # pip install docxtpl
from docx2pdf import convert
import datetime as tarih
import mailGonder
from openpyxl import Workbook,load_workbook

import mailGonder

wb = load_workbook("katilimcilar.xlsx")
ws = wb.active

# Aktif çalışma sayfasının adını yazdırma
# print(wb.sheetnames)
for x in range(2, 4):
  adiSoyadi = ws.cell(x,2).value
  baslik = ws.cell(x, 6).value
  gonderilecekMail = ws.cell(x, 3).value
  os.chdir(sys.path[0])
  doc = DocxTemplate("Template.docx")
  an = tarih.datetime.now()
  context = {
      "adsoyad": adiSoyadi,
      "baslik": baslik,
      "universite": "Batman Üniversitesi",
      "tarih": tarih.datetime.strftime(an, '%d %B %Y')
  }

  doc.render(context)
  dokumanAdi = adiSoyadi + ".docx";
  doc.save(dokumanAdi)
  dosyaadi=str(x)+"IIC2022"+"Kabul_Mektubu"+".pdf"
  convert(dokumanAdi,dosyaadi)
  print(gonderilecekMail)
  mailGonder.mailGonder(gonderilecekMail, dosyaadi)