import pandas as pd
from bs4 import BeautifulSoup
import requests
class BugsMusic:
    def __def__(self):
        pass


    def __init__(self):
        self.domain = 'https://music.bugs.co.kr/'
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
        ls1 = soup.find_all(name='p', attrs=({"class":'title'}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        return self.title_ls

    def get_artist(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls2 = soup.find_all(name='p', attrs=({"class": 'artist'}))
        for i in ls2:
            self.artist_ls.append(i.find("a").text)
        return self.artist_ls

    def insert_dict(self): #리스트 데이터를 딕셔너리로 옮긴다. 엑셀로 저장하기 위해서.
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]


    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')

    def df_to_excel(self):
        path = './data/bugs.xlsx'
        self.df.to_excel(path)


if __name__ == '__main__':
    b = BugsMusic()
    url = input('크롤링 대상 url을 입력하세요:')
    #https://music.bugs.co.kr/chart/track/day/total
    b.set_url(url)
    u2 = b.get_url()

    print(f'당신이 원하는 url은 {u2} 입니다.')

    ls = b.get_ranking()

    print(f'최종리스트 확인 {ls}')

    ls2 = b.get_artist()
    print(f'최종리스트 확인 {ls2}')

    b.insert_dict()
    b.dict_to_dataframe()
    b.df_to_excel()