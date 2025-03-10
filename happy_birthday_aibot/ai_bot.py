import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PROXY = os.getenv("PROXY")

# Настройка прокси
os.environ['HTTP_PROXY'] = PROXY
os.environ['HTTPS_PROXY'] = PROXY

# Переопределение метода requests.post для работы с прокси

def generate_text(text: str):
    genai.configure(api_key=GEMINI_API_KEY, transport='rest')

    try:
        # Создание модели
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Подготовка запроса
        s1 = 'Действуй как умный сильный, независимый и уверенный человек.\n'
        s2 = f'Напиши теплое, изысканное и доброе поздравление с днем рождения для: {text}.\n'
        s3 = '\nВ ответе можешь использовать смайлы и добрый, молодежный стиль'
        prompt = s1 + s2 + s3

        # Генерация текста
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Произошла ошибка: {e}"
