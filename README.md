# Happy birthday AIBot

Happy_birthday_aibot — Telegram-бот, который создает поздравление с днем рождения на основе информации о человеке. Использует API Gemini и поддерживает прокси.
Вы можете взаимодействовать с ботом по ссылке: [https://t.me/happy_birthday_aibot](https://t.me/happy_birthday_aibot)

## Описание проекта

Бот написан на Python с использованием `python-telegram-bot`. Генерирует поздравления через API Gemini и поддерживает SOCKS5-прокси.

## Установка и запуск

### 1. Клонирование репозитория

Склонируйте репозиторий на локальную машину:

```bash
git clone https://github.com/KrutilinNikita/happy_birthday_aibot.git
cd happy_birthday_aibot
```

### 2. Создание виртуального окружения (рекомендуется)

```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Создайте файл `.env` в корневой директории на основе `.env.template` и заполните его:

```
GEMINI_API_KEY=your_gemini_api_key
TELEGRAM_TOKEN=your_telegram_token
PROXY=socks5h://username:password@host:port
```

- **`GEMINI_API_KEY`** — ключ API для доступа к Gemini.
- **`TELEGRAM_TOKEN`** — токен бота в Telegram (получить через [BotFather](https://t.me/BotFather)).
- **`PROXY`**  — прокси для работы бота, если он недоступен без VPN.

### 5. Запуск бота

```bash
python happy_birthday_aibot/main.py
```

**Примечание:**  
Если сервис Gemini доступен без VPN, закомментируйте следующие строки в файле `ai_bot.py`:

```python
PROXY = os.getenv("PROXY")

# Настройка прокси
os.environ['HTTP_PROXY'] = PROXY
os.environ['HTTPS_PROXY'] = PROXY
```

## Контакты

Если у вас есть вопросы или предложения, пишите на почту krutilin.n@yandex.ru или в телеграм [@Krutilin_Nikita](https://t.me/Krutilin_Nikita)
