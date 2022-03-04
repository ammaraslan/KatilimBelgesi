import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Google Güvenli erişim kapatılması gerekmektedir. Aşağıdaki linlten kapatabilirsiniz.
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PvBJSlJA155OqwhiSPaFe9OzLSvMoZn2clBmlUTOf42XxQIr4mcMx3iOM2eBINvLw8vk1fzhVvCIGgvrNStlCZoGkPxg

def mailGonder(alici, dosyaadi):
    gonderecelMail = "bilgisayar.teknolojileri.btu@gmail.com"
    sifre = ""
    ileti = MIMEMultipart()

    ileti['From'] = gonderecelMail
    ileti['To'] = alici
    ileti['Subject'] = "Your paper has been accepted"
    icerik = '''Dear Participant,
    
The article you submitted for IIC2022 Congress was accepted as a result of the review process.

You can see acceptance letter in this email’s attachment.


Sincerly. '''

    ileti.attach(MIMEText(icerik, 'plain'))
    attachment = open("pdf/" + dosyaadi, "rb")

    part = MIMEBase('application', 'octet-stream')

    part.set_payload((attachment).read())

    encoders.encode_base64(part)

    part.add_header('Content-Disposition', "attachment; filename= %s" % dosyaadi)

    ileti.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gonderecelMail, sifre)
    text = ileti.as_string()
    try:
        server.sendmail(gonderecelMail, alici, text)
        server.quit()
        print("Başarılı bir şekilde gönderildi")
    except:
        print("Gönderme Başarısız", alici)
