import googletrans 


class Translator:

    def __init__(self):
        self.translator = googletrans.Translator()
        self.text = ''

    def set_text(self, text):
        self.text = text


    def kor_to_eng(self, text):
        result1 = self.text.translator.translate(self.text, dest='en', src='auto')
        return result1

    def eng_to_kor(self, text):
        result2 = self.translator.translate(self.text, dest='ko', src='en')
        return result2



if __name__ == '__main__':
    t = Translator()

    while 1:
        menu = input('0.종료 / 1. 문장 입력 / 2.한글->영어 / 3. 영어->한글')
        if menu == '0':
            print('프로그램을 종료합니다')
            break
        elif menu == '1':
            text = input('번역할 문장 입력 : ')
            t.set_text(text)
        elif menu == '2':
            a = t.eng_to_kor()
            print(f'영어 -> 한글 : {a}')
        elif menu == '3':
            a = t.kor_to_eng()
            print(f'영어 -> 한글 : {a}')
        else:
            print('잘못된 번호입니다.')
            continue




