from gtts import gTTS
from playsound import playsound

class TextToVoice:

    def __init__(self):
        self.text = ''

    def set_text(self, text):
        self.text = text

    def save_mp3(self, title):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(f'./{title}.mp3')

if __name__ == '__main__':
    t = TextToVoice()
    title = input('제목을 입력하세요 : ')
    text = input('변환하려는 문장을 입력하세요 : ')
    t.set_text(text)
    t.save_mp3(title)

    playsound(f'./{title}.mp3')

