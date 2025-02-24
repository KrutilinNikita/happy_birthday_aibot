from gspread import Client, Spreadsheet, service_account
from gspread.exceptions import WorksheetNotFound
import os
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env

TABLE_URL = os.getenv("TABLE_URL")
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")

# Таблица для загрузки данных
table_url = TABLE_URL

def client_init_json() -> Client:
    """Создание клиента для работы с Google Sheets."""
    return service_account(filename=GOOGLE_CREDENTIALS_PATH)


def get_table_by_url(client: Client, table_url: str) -> Spreadsheet:
    """Получение таблицы из Google Sheets по ссылке."""
    return client.open_by_url(table_url)

def append_data_to_google_sheet(data, sheet_name: str) -> None:
    try:
        client = client_init_json()
        table = get_table_by_url(client, table_url)
        worksheet = table.worksheet(sheet_name)
        rows = [data]
        worksheet.insert_rows(rows, row=2, value_input_option='RAW')
    except WorksheetNotFound:
        pass
    #     Сделать, что бы отправлял мне сообщение когда буду знать свой ЧатID

