import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['From'] = 'Kevin Serina'
email['To'] = 'kevin.serina2@yahoo.com'
email['Subject'] = "Python!!"

email.set_content('This is a test email sent with Python programming!! - King')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('myemail', 'mypassword')
    smtp.send_message(email)
    print('All done!')
