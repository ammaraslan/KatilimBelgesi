import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def mailGonder(alici,dosyaadi):
    fromaddr = "bilgisayar.teknolojileri.btu@gmail.com"
    toaddr = alici
    sifre = "Aaslan3..."
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "IIC2022"

    body = "IIC 2022"

    msg.attach(MIMEText(body, 'plain'))

    filename = dosyaadi
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, sifre)
    text = msg.as_string()
    try:
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("Başarılı bir şekilde gönderildi")
    except:
        print("Gönderme Başarısız",alici)
