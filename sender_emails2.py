import smtplib, email
from email.mime.text import MIMEText



'''
Extension MIME Type
.doc      application/msword
.dot      application/msword

.docx     application/vnd.openxmlformats-officedocument.wordprocessingml.document
.dotx     application/vnd.openxmlformats-officedocument.wordprocessingml.template
.docm     application/vnd.ms-word.document.macroEnabled.12
.dotm     application/vnd.ms-word.template.macroEnabled.12

.xls      application/vnd.ms-excel
.xlt      application/vnd.ms-excel
.xla      application/vnd.ms-excel

.xlsx     application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
.xltx     application/vnd.openxmlformats-officedocument.spreadsheetml.template
.xlsm     application/vnd.ms-excel.sheet.macroEnabled.12
.xltm     application/vnd.ms-excel.template.macroEnabled.12
.xlam     application/vnd.ms-excel.addin.macroEnabled.12
.xlsb     application/vnd.ms-excel.sheet.binary.macroEnabled.12

.ppt      application/vnd.ms-powerpoint
.pot      application/vnd.ms-powerpoint
.pps      application/vnd.ms-powerpoint
.ppa      application/vnd.ms-powerpoint

.pptx     application/vnd.openxmlformats-officedocument.presentationml.presentation
.potx     application/vnd.openxmlformats-officedocument.presentationml.template
.ppsx     application/vnd.openxmlformats-officedocument.presentationml.slideshow
.ppam     application/vnd.ms-powerpoint.addin.macroEnabled.12
.pptm     application/vnd.ms-powerpoint.presentation.macroEnabled.12
.potm     application/vnd.ms-powerpoint.template.macroEnabled.12
.ppsm     application/vnd.ms-powerpoint.slideshow.macroEnabled.12

.mdb      application/vnd.ms-access
'''

def send_emails2():
    subject = "An email with attachment from Python"
    from_addr = "me@fomin3.ru"
    to_addr = "me@fomin3.ru"
    password = "qgtoijzyzdcvqvwa"
    content = 'Отчет'
    message = email.message.EmailMessage()
    message["From"] = from_addr
    message["To"] = to_addr
    message["Subject"] = subject
    #message["Bcc"] = to_addr  # Recommended for mass emails
    body = MIMEText(content, 'plain')
    message.attach(body)
    filename = "Справка.docx"
    with open(filename, mode="rb") as f:
        fp = f.read()
        message.add_attachment(fp, maintype="application", subtype="vnd.openxmlformats-officedocument.wordprocessingml.document", filename=filename)
    filename2 = 'report.xlsx'
    with open(filename, mode="rb") as f:
        fp = f.read()
        message.add_attachment(fp, maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=filename2)
    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.login(from_addr, password)
    server.send_message(message, from_addr=from_addr, to_addrs=[to_addr])
    server.quit()
    
send_emails2()