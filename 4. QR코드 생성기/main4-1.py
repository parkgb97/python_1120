import qrcode

class QrMaker:
    def __init__(self):
        self.domain = ''

    def set_domain(self, domain):
        self.domain = domain

    def save_qr(self, title):
        qr_data = self.domain
        qr_img = qrcode.make(qr_data)

        save_path = f'./{title}.png'
        qr_img.save(save_path)


    def save_multi_qr(self, fname):

        with open(fname, 'rt', encoding='UTF8') as f:
            read_lines = f.readlines()

            for line in read_lines:
                line = line.strip()
                print(line)ㄹ

                qr_data = line
                qr_img = qrcode.make(qr_data)

                save_path = f'./QR Code/' + qr_data + '.png'
                qr_img.save(save_path)


if __name__ == '__main__':
    q = QrMaker()
    while 1 :
        menu = input('0.종료', '1.QR 1개 생성', '3.QR 여러개 생성')
        if menu == '0'
        print('프로그램 종료')
    break

    title = input('타이틀을 입력하세요 : ')
    domain = input('도메인을 입력하세요 : ')
    q.set_domain(domain)
    q.save_qr(title)
