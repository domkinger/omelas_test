from bs4 import BeautifulSoup
import requests

def get_html(url):
    ok_ru = requests.get(url)
    html = BeautifulSoup(ok_ru.text, 'html.parser')
    return html

ok_html = get_html('https://ok.ru/mil')
print(ok_html)