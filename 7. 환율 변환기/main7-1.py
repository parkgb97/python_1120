from currency_converter import CurrencyConverter
import requests
from bs4 import BeautifulSoup

class Exchanger:

    def __init__(self):
        pass

    def get_all_currencies(self):
        cc = CurrencyConverter()
        return cc.currencies

    def change_usd_to_krw(self):
        cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
        return cc.convert(1, 'USD', 'KRW')

    def realtime_usd_to_krw(self, target1, target2):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }

        response = requests.get(f"https://kr.investing.com/currencies/{target1}-{target2}", headers=headers)
        content = BeautifulSoup(response.content, 'html.parser')
        containers = content.find(name='span', attrs={'data-test': 'instrument-price-last'})
        return containers.text

if __name__ == '__main__':
    e = Exchanger()
    while 1:
        menu = input('0.종료 / 1.전체 화폐 단위 보기 / 2.1달러당 원화 환율 / 3. 환전')
        if menu == '0':
            print('프로그램을 종료합니다.')
            break
        elif menu == '1':
            c = e.get_all_currencies()
            print(f'모든 화폐 단위 : {c}')
        elif menu == '2':
            c= e.change_usd_to_krw()
            print(f'웓달러 환율 : {c}')
        elif menu == '3':
            target1 = input('바꾸려고 하는 화폐단위 : ')
            target2 = input('바뀌는 화폐단위 : ')
            c= e.realtime_usd_to_krw(target1, target2)
            print(f'실시간 원달러 환율 : {c}')
        else:
            print('잘못된 번호입니다.')
            continue

    print(cc.currencies)