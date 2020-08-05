import requests
from bs4 import BeautifulSoup
import time


class Currency:
    DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+&aqs=chrome.0.0j69i57j0l6.2649j0j7&sourceid=chrome&ie=UTF-8'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    currentConvertedPrice = 0

    upDifference = 5
    downDifference = 5

    def __init__(self):
        self.currentConvertedPrice = float(self.getCurrencyPrice().replace(',', '.'))

    def getCurrencyPrice(self):
        try:
            full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')
            convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
            return convert[0].text
        except requests.ConnectionError:
            print('Проблемы с соединением. Проверьте подключение к сети')
        except requests.RequestException:
            print('Информация по данному запросу недоступна')

    def checkCurrency(self):
        currency = float(self.getCurrencyPrice().replace(',', '.'))
        if currency > self.currentConvertedPrice + self.upDifference:
            print('Курс превысил установленную отметку!')
        elif currency == self.currentConvertedPrice + self.upDifference:
            print('Курс достиг верхней установленной отметки!')
        elif currency < self.currentConvertedPrice - self.downDifference:
            print('Курс пренизил установленную отметку!')
        elif currency == self.currentConvertedPrice - self.downDifference:
            print('Курс достиг нижней установленной отметки!')
        else:
            print('Курс находится в допустимых нормах')
        print('Курс доллара составляет', currency, 'рубля', '\n')
        time.sleep(3)
        self.checkCurrency()


currency = Currency()

currency.checkCurrency()
