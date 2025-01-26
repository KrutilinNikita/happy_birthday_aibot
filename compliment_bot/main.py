from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

SECRET_KEY = os.getenv("API_KEY")
print(SECRET_KEY)