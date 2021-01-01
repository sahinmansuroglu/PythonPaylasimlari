sayi1=int(input("1. Sayıyı Giriniz:"))
sayi2=int(input("2. Sayıyı Giriniz:"))

islem=input("İşlem Seçiniz (+,-,/,*):")

islemGecerliMi="Gecerli"
sonuc=0
if islem=="+":
    sonuc = sayi1+sayi2
elif islem=="-":
    sonuc = sayi1 - sayi2
elif islem=="*":
    sonuc = sayi1 * sayi2
elif islem=="/":
    sonuc = sayi1 / sayi2
else:
    print("Lütfen Doğru bir işlem giriniz")
    islemGecerliMi="Geçersiz"


if islemGecerliMi=="Gecerli":
    print(f"Sonuc:{sonuc}")
    print(f"{sayi1}{islem}{sayi2}={sonuc}")