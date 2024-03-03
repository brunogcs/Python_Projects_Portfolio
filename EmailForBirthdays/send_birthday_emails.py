import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# SMTP server settings (MailHog)
smtp_server = 'localhost'  # MailHog server address
smtp_port = 1025  # Default MailHog port

# Function to read the CSV file and return a list of today's birthday celebrants
def get_birthday_people():
    today = datetime.today().strftime('%m-%d')
    birthday_people = []
    with open('aniversariantes.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['data_de_nascimento'][-5:] == today:
                birthday_people.append(row)
    return birthday_people

# Loop to send birthday greetings emails to all celebrants of the day.
for person in get_birthday_people():
    sender_email = 'noreply@example.com'
    receiver_email = person['email']
    subject = 'Happy Birthday!'
    message = f'Hello {person["nome"]},\n\nWishing you a fantastic birthday! May your day be filled with joy and happiness.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f'Birthday greetings email sent to {person["nome"]} ({receiver_email})')
        server.quit()
    except Exception as e:
        print(f'Error sending email to {person["nome"]} ({receiver_email}): {str(e)}')
