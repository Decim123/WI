import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from code_generator import generate_accept_code
# тип писма
message_type = "email_chek" # or "change_password"

sendler = "wimp.mailer@gmail.com" # sendler mail
user = "aleksandrtuman@gmail.com" #получатель в будующем будет передаваться пока просто подставлять

# Создание контейнера для сообщения - правильный MIME-тип multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Код подтверждения"
msg['From'] = sendler
msg['To'] = user

# Ваш код подтверждения
key_code = str(generate_accept_code()) # генерация случайного 6 значного числа

if message_type == "email_chek":

    # Создание тела сообщения 
    text = f"Привет!\nВот ваш код подтверждения email: {key_code}"
    html = f"""
    <html>
    <head></head>
    <body style="background-color: #E6FFE6; border-radius: 15px; padding: 20px;">
        <div style="background-color: #4CAF50; padding: 10px; border-radius: 10px;">
        <p style="font-family: Arial, sans-serif; font-size: 16px; color: #FFFFFF;">Привет!<br>
        Вот ваш код подтверждения email: <strong>{key_code}</strong></p>
        </div>
    </body>
    </html>
    """
elif message_type == "change_password":
        # Создание тела сообщения 
    text = f"Привет!\nВот ваш код для восстановления пароля: {key_code}"
    html = f"""
    <html>
    <head></head>
    <body style="background-color: #E6FFE6; border-radius: 15px; padding: 20px;">
        <div style="background-color: #4CAF50; padding: 10px; border-radius: 10px;">
        <p style="font-family: Arial, sans-serif; font-size: 16px; color: #FFFFFF;">Привет!<br>
        Вот ваш код для восстановления пароля: <strong>{key_code}</strong></p>
        </div>
    </body>
    </html>
    """
else:
    print("ERROR: message_type")

# Указание MIME-типов для обоих частей - text/plain и text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Добавление частей в контейнер сообщения.
msg.attach(part1)
msg.attach(part2)

# Отправка сообщения через сервер SMTP Gmail.
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('wimp.mailer@gmail.com', 'scik tckj livn wzzu')
mail.sendmail(sendler, user, msg.as_string())
mail.quit()
