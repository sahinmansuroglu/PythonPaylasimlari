# Klavyeden sürekli Öğrencilerin Adı ve puanı girilecek
# Ne zaman ad'a "Çıkış" değeri girilirse o anda bilgi girişi
# sonlandırılacak  girilen puanların ortalaması hesaplatılacak
#ve son olarak puanı ortalamanın altında olan öğrencilerin
#ad'ları ve puanları' listelenecek

adListesi=[]
puanListesi=[]
i=1
puanToplam=0
while(True):
    ad=input(f"{i}. Öğrencini Adını Giriniz:")
    if ad=="Çıkış":
        break
    puan=int(input(f"{i}. Öğrencini puanını Giriniz:"))
    puanToplam=puanToplam+puan
    adListesi.append(ad)
    puanListesi.append(puan)
    i=i+1
ortalama=puanToplam/len(puanListesi)
print(f"Ortalam={ortalama}")
print(f"Ad Listesi:{adListesi}")
print(f"Puan Listesi:{puanListesi}")

print("Puanı Ortalamanın Altında Olan Öğrenci Listesi")

for i in range(len(adListesi)):
    if (puanListesi[i]<ortalama):
        print(f"{adListesi[i]}: {puanListesi[i]}")

# Program Çalıştığında aşağıdaki çıktıyı vermiştir.
# 1. Öğrencini Adını Giriniz:arda
# 1. Öğrencini puanını Giriniz:65
# 2. Öğrencini Adını Giriniz:veli
# 2. Öğrencini puanını Giriniz:95
# 3. Öğrencini Adını Giriniz:serkan
# 3. Öğrencini puanını Giriniz:25
# 4. Öğrencini Adını Giriniz:ahmet
# 4. Öğrencini puanını Giriniz:50
# 5. Öğrencini Adını Giriniz:serdar
# 5. Öğrencini puanını Giriniz:55
# 6. Öğrencini Adını Giriniz:Çıkış
# Ortalam=58.0
# Ad Listesi:['arda', 'veli', 'serkan', 'ahmet', 'serdar']
# Puan Listesi:[65, 95, 25, 50, 55]
# Puanı Ortalamanın Altında Olan Öğrenci Listesi
# serkan: 25
# ahmet: 50
# serdar: 55
