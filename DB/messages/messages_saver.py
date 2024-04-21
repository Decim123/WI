import sqlite3
import os

# Словари с данными
texts = {199: 'Ура', 200: None, 201: None}
images = {199: None, 200: '/media/200.png', 201: '/media/201.png'}
texts_with_images = {199: 'Ура', 200: None, 201: 'Ура'}


# Создание подключения к базе данных
conn = sqlite3.connect('uch_messages.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS media
                (id INTEGER PRIMARY KEY,
                text TEXT,
                mp3_path TEXT,
                image_path TEXT)''')

# Функция для сохранения данных одного сообщения в базу данных
def save_message_to_database(message_id, text, image_path):
    cursor.execute('''INSERT INTO media (id, text, image_path)
                      VALUES (?, ?, ?)''',
                   (message_id, text, image_path))
    conn.commit()

#Сохранение данных каждого сообщения в базу данных
for message_id in texts:
    text = texts[message_id]
    image_path = images[message_id]
    text_with_image = texts_with_images[message_id]
    # Выбор текста в зависимости от наличия изображения
    if image_path:
        text_to_save = text_with_image if text_with_image else text
    else:
        text_to_save = text
    save_message_to_database(message_id, text_to_save, image_path)

conn.close()


