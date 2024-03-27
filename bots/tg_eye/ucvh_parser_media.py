import os
from pyrogram import Client, filters

# Настройки доступа к аккаунту и каналу
api_id = '27476103'
api_hash = '61343303593c3cc763b09e21a0fe5cb5'
phone_number = '+79800770417'  # Номер телефона, связанный с вашим аккаунтом
channel_id = -1002083751969  # Идентификатор вашего канала
feed_text = {} # словарь для текста
feed_media = {} # словарик для медиа
feed_caption = {}
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
    if message.photo:
        print("Downloading media...")
        try:
            # Получаем расширение медиафайла
            file_extension = ".jpg"
            
            # Формируем имя файла с использованием ID сообщения и расширения
            file_name = f"{message.id}{file_extension}"
            full_file_path = os.path.join(media_directory, file_name)
            
            # Скачиваем медиафайл в директорию media внутри директории бота
            file_path = await client.download_media(message, file_name=full_file_path)
            
            # Убеждаемся, что файл загружен
            if os.path.exists(file_path):
                print("Media downloaded successfully.")
                feed_media[message.id] = f'/media/{file_name}' # добавляем путь к файлу в словарь
                print(feed_media)
                
               
            else:
                print("Error: File download failed.")

        except Exception as e:
            print(f"Error downloading media: {e}")
    else:
        feed_media[message.id] = None
        print(feed_media)

     # Если у сообщения есть текст, выводим его
    if message.caption:
        feed_text[message.id] = message.caption
        print(feed_text)
    else:
        feed_text[message.id] = None
        print(feed_text)    

    # Если сообщение текстовое
    if message.text:
        feed_text[message.id] = message.text
        print(feed_text)
    # Если сообщение не содержит текст
    else:
        feed_text[message.id] = None
        print(feed_text)

# Запуск основной программы
client.run()
