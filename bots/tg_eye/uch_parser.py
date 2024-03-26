from pyrogram import Client, filters
import os
# Настройки доступа к аккаунту и каналу
api_id = '27476103'
api_hash = '61343303593c3cc763b09e21a0fe5cb5'
phone_number = '+79800770417'  # Номер телефона, связанный с вашим аккаунтом
channel_id = -1002083751969  # Идентификатор вашего канала

# Создание клиента Pyrogram
client = Client("session_name", api_id=api_id, api_hash=api_hash)

# Путь к директории бота
bot_directory = "./"  # Укажите правильный путь к директории вашего бота

# Создание клиента Pyrogram
client = Client("session_name", api_id=api_id, api_hash=api_hash)

# Функция для обработки текстовых сообщений и скачивания медиафайлов
@client.on_message(filters.chat(channel_id))
async def process_messages(client, message):
    print(f"Message ID: {message.id}")
    
    # Относительный путь к директории media внутри директории бота
    media_directory = os.path.join(bot_directory, "media")
    
    # Если сообщение содержит медиафайл
    if message.media:
        print("Downloading media...")
        try:
            # Скачиваем медиафайл в директорию media внутри директории бота
            file_path = await client.download_media(message, file_name=media_directory)
            
            # Получаем путь к временному файлу
            temp_file_path = file_path + ".temp"
            
            # Переименовываем временный файл, убирая расширение ".temp"
            os.rename(temp_file_path, file_path)
            
            print("Media downloaded successfully.")
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
