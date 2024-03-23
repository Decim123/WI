import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from code_generator import generate_accept_code

sendler = "wimp.mailer@gmail.com"
user = "aleksandrtuman@gmail.com"

# Создание контейнера для сообщения - правильный MIME-тип multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Код подтверждения"
msg['From'] = sendler
msg['To'] = user

# Ваш код подтверждения
key_code = str(generate_accept_code())  # Пример кода, замените его на ваш реальный код

# Создание тела сообщения (в виде обычного текста и версии HTML).
text = f"Привет!\nВот ваш код подтверждения: {key_code}"
html = f"""
<html>
  <head></head>
  <body style="background-color: #E6FFE6; border-radius: 15px; padding: 20px;">
    <div style="background-color: #4CAF50; padding: 10px; border-radius: 10px;">
      <p style="font-family: Arial, sans-serif; font-size: 16px; color: #FFFFFF;">Привет!<br>
      Вот ваш код подтверждения: <strong>{key_code}</strong></p>
    </div>
  </body>
</html>
"""

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
