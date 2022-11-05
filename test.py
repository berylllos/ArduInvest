# подключаем urlopen из модуля urllib
from urllib.request import urlopen

# подключаем библиотеку BeautifulSout
from bs4 import BeautifulSoup

url = [
"https://intelinvest.ru/public-portfolio/499056",
]



# перебираем все адреса из списка
for x in url:
    # получаем исходный код очередной страницы из списка
    html_code = str(urlopen(x).read(),'utf-8')
    # отправляем исходный код страницы на обработку в библиотеку
    soup = BeautifulSoup(html_code, "html.parser")

    # находим название страницы с помощью метода find()
    s = soup.find("div", "dashboard-card-big-nums rub").text

    # выводим его на экран
    print(s)
