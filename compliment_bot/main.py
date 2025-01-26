from dotenv import load_dotenv
import os
from chat_gpt import generate_compliment
import telebot

load_dotenv()  # Загружает переменные из .env

# Токен Telegram-бота
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Напиши, что тебе нравится в девушке, и я помогу придумать красивый комплимент."
    )

# Обработчик текстовых сообщений
@bot.message_handler(content_types=["text"])
def handle_text(message):
    user_input = message.text
    try:
        # Генерация комплимента
        compliment = generate_compliment(user_input)
        bot.send_message(message.chat.id, compliment)
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.send_message(
            message.chat.id,
            "Произошла ошибка при генерации комплимента. Попробуйте снова!"
        )

if __name__ == "__main__":
    # Запуск бота
    bot.polling()