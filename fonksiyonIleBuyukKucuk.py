def enBuyukSayiyiBul(sayi1,sayi2):
    if (sayi1>sayi2):
        return  sayi1
    else:
        return sayi2



s1=int(input("1. sayıyı Giriniz:"))
s2=int(input("2. sayıyı Giriniz:"))

print(f"Büyük Sayi={enBuyukSayiyiBul(s1,s2)}")
