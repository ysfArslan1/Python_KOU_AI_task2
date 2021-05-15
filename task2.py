

import os

yeni_dosya = os.open('text.txt',os.O_RDWR)

istatistik = os.stat(yeni_dosya)
uzunluk =os.stat(yeni_dosya).st_size
icerik = os.read(yeni_dosya,uzunluk)
icerik = icerik.decode()

print(icerik)


metin = list(icerik)
kasa = ''
i = 0

while i < len(metin):
    if metin[i].isalpha():
        kasa = kasa + metin[i]
    i += 1


os.close(yeni_dosya)
os.unlink('text.txt')


yeni_dosya = os.open('text.txt',os.O_RDWR|os.O_CREAT)
os.write(yeni_dosya,kasa.encode())
print(kasa)
os.close(yeni_dosya)




