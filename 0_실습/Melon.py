from bs4 import BeautifulSoup
import requests
class MelonMusic:
    def __init__(self):
        self.domain = 'https://www.melon.com'
        self.url = ''
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []
        self.title_ls = []
        self.artist_ls = []
        self.dict = {}
        self.df = None

    def set_url(self, url):
        self.url = requests.get(f'{self.domain}{url}', headers=self.headers).text

    def get_url(self):
        return self.url

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='div', attrs=({"class": 'ellipsis rank01'}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        return self.title_ls

    def get_artist(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls2 = soup.find_all(name='div', attrs=({"class": 'ellipsis rank02'}))
        for i in ls2:
            self.artist_ls.append(i.find("a").text)
        return self.artist_ls


if __name__ == '__main__':
    m = MelonMusic()
    url = input('멜론에서 크롤링 할 url을 입력하세요:')
    #https://www.melon.com/chart/index.htm?dayTime=
    m.set_url(url)
    u2 = m.get_url()
    print(f'당신이 원하는 url은 {u2} 입니다.')

    ls1 = m.get_ranking()

    print(f'최종리스트 확인 {ls1}')

    ls2 = m.get_artist()
    print(f'최종리스트 확인 {ls2}')