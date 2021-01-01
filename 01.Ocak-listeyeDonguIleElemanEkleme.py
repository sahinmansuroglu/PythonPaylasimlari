adet=int(input("Kaç kişnini Adını girmek İstiyorsunuz:"))
adListesi=[]
for i in range(1,adet+1):
    ad=input(f"{i}. kişinin  adını giriniz:")
    adListesi.append(ad)

for herbirAd in adListesi:
    print(f"{herbirAd}")