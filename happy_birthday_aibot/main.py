from dotenv import load_dotenv
import os
from ai_bot import generate_text
import telebot
from add_data_to_bd import append_data_to_google_sheet

from datetime import datetime
import time

load_dotenv()  # Загружает переменные из .env

# Токен Telegram-бота
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Напиши, информацию про человека, и я помогу придумать персональное поздравление с днем рождения."
    )
    bot.send_message(
        message.chat.id,
        "Ты в любой момент можешь написать информацию про человека и я пришлю поздравление."
    )
    user_input = 'start'
    user_id = message.chat.id
    username = message.from_user.username if message.from_user.username else "Unknown"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response_text = None
    response_time = None
    error = None
    try:
        log_entry = [timestamp, user_id, username, user_input, response_text, response_time, error]
        # Вызываем функцию записи в Google Таблицу
        append_data_to_google_sheet(data=log_entry, sheet_name="Logs_start")
    except Exception as e:
        pass
        print('Ошибка записи в табилцу')
        # bot.send_message(user_id, compliment) Сообщение мне об ошибки


# Обработчик текстовых сообщений
@bot.message_handler(content_types=["text"])
def handle_text(message):
    user_input = message.text
    user_id = message.chat.id
    username = message.from_user.username if message.from_user.username else "Unknown"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        start_time = time.time()  # Начало измерения времени ответа
        response_text = generate_text(user_input)
        response_time = round(time.time() - start_time, 3)  # Время обработки
        error = None
        bot.send_message(user_id, response_text)
    except Exception as e:
        response_text = "Ошибка!"
        response_time = None
        error = str(e)
        # print(f"Ошибка: {e}")
        # bot.send_message(user_id, compliment) Сообщение мне об ошибки
    try:
        log_entry = [timestamp, user_id, username, user_input, response_text, response_time, error]
        # Вызываем функцию записи в Google Таблицу
        append_data_to_google_sheet(data=log_entry, sheet_name="Logs_data")
    except Exception as e:
        pass
        print('Ошибка записи в табилцу')
        # bot.send_message(user_id, compliment) Сообщение мне об ошибки


if __name__ == "__main__":
    # Запуск бота
    bot.polling()