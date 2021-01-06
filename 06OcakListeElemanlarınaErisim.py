# Liste Elemanlarını Görüntüleyebilmek için 2 farklı yöntem vardır 
# 1. yöntemde döngü ile direk elemanlar üzerinde gezinilir ve ekranda görüntülenir
# 2. Yöntemde ise herbir elemana index(Sıra) numarası ile erişilir ve ardından ekrana yazdırılır

adListesi=["Ali","Veli","Mehmet","Arda","Ayça","Akın"]



print("1. Yöntem (Liste Elemanlarını Görünütlemek İçin)")
for herbirAd in adListesi:
    print(f"1. Yöntem Ad:{herbirAd}")

print("2. Yöntem (Liste Elemanlarını Görünütlemek İçin)")
for i in range(len(adListesi)):
    print(f"2. Yöntem Ad:{adListesi[i]}")

# Bu Program Aşağıdaki çıktıyı vermiştir.
# 1. Yöntem (Liste Elemanlarını Görünütlemek İçin)
# 1. Yöntem Ad:Ali
# 1. Yöntem Ad:Veli
# 1. Yöntem Ad:Mehmet
# 1. Yöntem Ad:Arda
# 1. Yöntem Ad:Ayça
# 1. Yöntem Ad:Akın
# 2. Yöntem (Liste Elemanlarını Görünütlemek İçin)
# 2. Yöntem Ad:Ali
# 2. Yöntem Ad:Veli
# 2. Yöntem Ad:Mehmet
# 2. Yöntem Ad:Arda
# 2. Yöntem Ad:Ayça
# 2. Yöntem Ad:Akın
