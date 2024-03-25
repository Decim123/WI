import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from code_generator import generate_accept_code
# тип писма
message_type = "email_chek" # or "change_password" email_chek

sendler = "wimp.mailer@gmail.com" # sendler mail
user = "alaz2005tv@gmail.com" #получатель в будующем будет передаваться пока просто подставлять

# Ваш код подтверждения
key_code = str(generate_accept_code()) # генерация случайного 6 значного числа

if message_type == "email_chek":

    # Создание контейнера для сообщения - правильный MIME-тип multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Код подтверждения"
    msg['From'] = sendler
    msg['To'] = user

    # Создание тела сообщения 
    text = f"Привет!\nВот ваш код подтверждения email: {key_code}"
    html = f"""
    <html>
    <head></head>
    <body style="background-color: #E6FFE6; border-radius: 15px; padding: 20px;height: 600px;width: 500px; text-align: center; margin:auto">
        <div style="background: linear-gradient(to bottom, #87A3D2, #90D6A0); padding: 10px; border-radius: 10px;height: 95%;">
        <p style="font-family: Arial, sans-serif; font-size: 40px; color: #FFFFFF;">WI<br>Привет!</p>
        <p style="font-family: Arial, sans-serif; font-size: 20px; color: #FFFFFF;">Ваш код подтверждения: </p>
        <p style="font-family: Arial, sans-serif; font-size: 40px; color: #FFFFFF;"><strong>{key_code}</strong></p> 
        <p style="font-family: Arial, sans-serif; font-size: 20px; color: #FFFFFF;">Никому не сообщайте код подтверждения.<br>Если вы не запрашивали код, то игнорируете это сообщение<br>С уважением, ваши кенты из WI</p>
        </div>
    </body>
    </html>
    """
elif message_type == "change_password":

    
    # Создание контейнера для сообщения - правильный MIME-тип multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] =  "Код восстановления пароля"

    msg['From'] = sendler
    msg['To'] = user


        # Создание тела сообщения 
    text = f"Привет!\nВот ваш код для восстановления пароля: {key_code}"
    html = f"""
    <html>
    <head></head>
    <body style="background-color: #E6FFE6; border-radius: 15px; padding: 20px;height: 600px;width: 500px; text-align: center; margin:auto">
        <div style="background: linear-gradient(to bottom, #87A3D2, #90D6A0); padding: 10px; border-radius: 10px;height: 95%;">
        <p style="font-family: Arial, sans-serif; font-size: 40px; color: #FFFFFF;">WI<br>Привет!</p>
        <p style="font-family: Arial, sans-serif; font-size: 20px; color: #FFFFFF;">Ваш код для восстановления пароля: </p>
        <p style="font-family: Arial, sans-serif; font-size: 40px; color: #FFFFFF;"><strong>{key_code}</strong></p> 
        <p style="font-family: Arial, sans-serif; font-size: 20px; color: #FFFFFF;">Никому не сообщайте код подтверждения.<br>Если вы не запрашивали код, то игнорируете это сообщение<br>С уважением, ваши кенты из WI</p>
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
