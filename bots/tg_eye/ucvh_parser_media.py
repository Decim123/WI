import os
from pyrogram import Client, filters
import asyncio

# Настройки доступа к аккаунту и каналу
api_id = '27476103'
api_hash = '61343303593c3cc763b09e21a0fe5cb5'
phone_number = '+79800770417'  # Номер телефона, связанный с вашим аккаунтом
channel_id = -1002083751969  # Идентификатор вашего канала

# Создание клиента Pyrogram
client = Client("session_name", api_id=api_id, api_hash=api_hash)

# Путь к директории бота
bot_directory = "./"  # Укажите правильный путь к директории вашего бота

# Функция для обработки сообщений
@client.on_message(filters.chat(channel_id))
async def process_messages(client, message):
    print(f"Message ID: {message.id}")
    
    # Относительный путь к директории media внутри директории бота
    media_directory = os.path.join(bot_directory, "media")
    
    # Если сообщение содержит медиафайл
    if message.media:
        print("Downloading media...")
        try:
            # Получаем расширение медиафайла
            file_extension = ""
            if message.photo:
                file_extension = ".jpg"
            elif message.video:
                file_extension = ".mp4"
            elif message.audio:
                file_extension = ".mp3"
            elif message.document:
                file_extension = os.path.splitext(message.document.file_name)[1]
            
            # Формируем имя файла с использованием ID сообщения и расширения
            file_name = f"{message.id}{file_extension}"
            
            # Скачиваем медиафайл в директорию media внутри директории бота
            file_path = await client.download_media(message, file_name=os.path.join(media_directory, file_name))
            
            # Дожидаемся завершения скачивания перед переименованием файла
            while not os.path.exists(file_path):
                await asyncio.sleep(0.1)
            
            # Убеждаемся, что файл загружен
            if os.path.exists(file_path):
                # Получаем путь к временному файлу
                temp_file_path = file_path + ".temp"
                
                # Переименовываем временный файл, убирая расширение ".temp"
                os.rename(temp_file_path, file_path)
                
                print("Media downloaded successfully.")
            else:
                print("Error: File download failed.")
        except Exception as e:
            print(f"Error downloading media: {e}")
    # Если сообщение текстовое
    elif message.text:
        print(f"Text: {message.text}")
    # Если сообщение не содержит ни медиа, ни текст
    else:
        print("Unsupported message type")

# Запуск основной программы
client.run()
