import requests
from bs4 import BeautifulSoup
import json

# URL сайта
url = "https://www.scrapethissite.com/pages/simple/"

# Запрос к сайту
response = requests.get(url)

data = []

# Проверка успешности запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    countries = soup.find_all('div', class_='country')
    
    for country in countries:
        country_name = country.find('h3', class_='country-name').text.strip()
        capital = country.find('span', class_='country-capital').text.strip()
        data.append({"Country": country_name, "Capital": capital})
    
    # Сохранение данных в файл data.json
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
else:
    print("Failed to retrieve the website.")
