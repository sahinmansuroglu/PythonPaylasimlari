adList=["Arda","Erkan"]
yaziliList=[65,34]
performansList=[85,56]

def ogrenciEkle():
    print("Öğrenci Ekleme İşlemleri")
    adSoyad=input("Ad Soyad Giriniz:")
    yazili=int(input("Yazılı Notunuzu Giriniz:"))
    performans = int(input("Performans Notunuzu Giriniz:"))
    adList.append(adSoyad)
    yaziliList.append(yazili)
    performansList.append(performans)
    print("Kayıt Başarılı Bir şekilde Eklendi")

def ogrenciSil():
    print("Öğrenci Silme İşlemleri")
    adSoyad = input("Silinicek Ad Soyad'ı Giriniz:")
    if adSoyad in adList:
        silinecekSn=adList.index(adSoyad)
        adList.pop(silinecekSn)
        yaziliList.pop(silinecekSn)
        performansList.pop(silinecekSn)
        print("Silme İşlemi Başarı ile Gerçekleştirildi")
    else:
        print("Silmek İstedğiniz Kişi Listede Kayıtlı Deği")

def ogrenciArama():
    print("Öğrenci Arama İşlemleri")
    adSoyad = input("Aranacak Ad Soyad'ı Giriniz:")
    if adSoyad in adList:
        arananSn = adList.index(adSoyad)
        print(f"{'Ad Soyad':10} {'Yazılı':10} {'Perf.':10} {'Ortalama':10} {'Durum':10}")

        ortalama = (yaziliList[arananSn] + performansList[arananSn]) / 2
        durum = "Kaldı"
        if ortalama >= 50:
            durum = "Getçi"
        print(f"{adList[arananSn]:10} {yaziliList[arananSn]:10} {performansList[arananSn]:10} {ortalama:10} {durum:10}")

    else:
        print("Aramak İstedğiniz Kişi Listede Kayıtlı Değil")
def tumunuListele():
    print("Tüm Öğrenci Listesi")
    print(f"{'Ad Soyad':10} {'Yazılı':10} {'Perf.':10} {'Ortalama':10} {'Durum':10}")
    for sn in range(len(adList)):
        ortalama=(yaziliList[sn]+performansList[sn])/2
        durum ="Kaldı"
        if ortalama>=50 :
            durum="Getçi"
        print(f"{adList[sn]:10} {yaziliList[sn]:10} {performansList[sn]:10} {ortalama:10} {durum:10}")

def guncelleme():
    print("Öğrenci Güncelleme İşlemleri")
    adSoyad = input("Güncellemek İstediğiniz Ad Soyad'ı Giriniz:")
    if adSoyad in adList:
        arananSn = adList.index(adSoyad)
        print(f"{'Ad Soyad':10} {'Yazılı':10} {'Perf.':10} {'Ortalama':10} {'Durum':10}")

        ortalama = (yaziliList[arananSn] + performansList[arananSn]) / 2
        durum = "Kaldı"
        if ortalama >= 50:
            durum = "Getçi"
        print(f"{adList[arananSn]:10} {yaziliList[arananSn]:10} {performansList[arananSn]:10} {ortalama:10} {durum:10}")

        yeniadSoyad = input("Yeni Ad Soyadı Giriniz:")
        yeniyazili = int(input("Yeni Yazılı Notunuzu Giriniz:"))
        yeniperformans = int(input("Yeni Performans Notunuzu Giriniz:"))
        adList[arananSn]=yeniadSoyad
        yaziliList[arananSn]=yeniyazili
        performansList[arananSn]=yeniperformans

        print("Güncelleme İşlemi Başarılı Bir şekilde gerçekleştirilmiştir.")



    else:
        print("Aramak İstedğiniz Kişi Listede Kayıtlı Değil")
def kalanListele():
    print("Kalan  Öğrencilerin Listesi")
    print(f"{'Ad Soyad':10} {'Yazılı':10} {'Perf.':10} {'Ortalama':10} {'Durum':10}")
    for sn in range(len(adList)):
        ortalama = (yaziliList[sn] + performansList[sn]) / 2
        if ortalama < 50:
            print(f"{adList[sn]:10} {yaziliList[sn]:10} {performansList[sn]:10} {ortalama:10} {'Kaldı':10}")
def gecenleriListeleme():

    print("Geçen  Öğrencilerin Listesi")
    print(f"{'Ad Soyad':10} {'Yazılı':10} {'Perf.':10} {'Ortalama':10} {'Durum':10}")
    for sn in range(len(adList)):
        ortalama = (yaziliList[sn] + performansList[sn]) / 2
        if ortalama >= 50:
            print(f"{adList[sn]:10} {yaziliList[sn]:10} {performansList[sn]:10} {ortalama:10} {'Geçti':10}")

def menu():

    fonksiyonListesi=[ogrenciEkle,ogrenciSil,ogrenciArama,tumunuListele,guncelleme,kalanListele,gecenleriListeleme]
    while True:
        print("1-Öğrenci Ekle")
        print("2-Öğrenci sil")
        print("3-Öğrenci Arama")
        print("4-Tümünü Listele")
        print("5-Güncelleme")
        print("6-Kalan Öğrencileri Listele")
        print("7-Geçen Öğrencileri Listele")
        print("0-Programdan Çık")
        seciminiz=int(input("Lütfen Yapmak İstediğiniz İşlem Seçiniz (0-7):"))
        print("\n"*40)
        if seciminiz<=7 and seciminiz>=1:
            fonksiyonListesi[seciminiz-1]()

            print("\n" * 2)
        elif seciminiz==0:
            print("Çıkış Yapılıyor")
            break
        else:
            print("Lütfen Seçim İçin 0 ile 7 arası bir rakam giriniz!")

menu()
