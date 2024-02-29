import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sendmail():
    fromaddres = "screen4life@mail.ru"
    toaddr = "screen4life@mail.ru"
    mypass = "9utdPSe8hetUHpbg5Sv2"
    reportname = "log.txt"

    msg = MIMEMultipart()
    msg['From'] = fromaddres
    msg['To'] = toaddr
    msg['Subject'] = "Автотест письмо"

    with open(reportname, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
        msg.attach(part)
    #
    body = "Тест"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

    # server.starttls()
    server.login(fromaddres, mypass)
    text = msg.as_string()
    server.sendmail(fromaddres, toaddr, text)
    server.quit()