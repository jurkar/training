import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        # Проверяем успешность запроса по коду состояния HTTP
        if response.status_code == 200:
            print(f"Сайт {url} доступен. Код состояния: {response.status_code}")
        else:
            print(f"Сайт {url} вернул код состояния: {response.status_code}")
    except requests.ConnectionError:
        print(f"Не удалось подключиться к сайту {url}")

website_url = 'https://www.example.com'

while True:
    check_website(website_url)
    # Пауза на 60 секунд перед следующей проверкой
    time.sleep(60)
