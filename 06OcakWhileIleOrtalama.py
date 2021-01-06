# Program while döngüsü ile kulanacıdan  sürekli sayı girmesini isteyecektir.
# Eğer kullanıcı 0 girdiyse o ana kadar girlen sayıların toplamını adedini
# ve ortalamasını ekrana yazdıracaktır.

toplam=0
sayi=45
adet=0
while(sayi!=0):
    adet=adet+1
    sayi=int(input(f"{adet}. Sayıyı Giriniz:"))
    toplam=toplam+sayi

print("Döngü Sonlandı")
print(f"{adet} tane sayı girdiniz")
ortalama=toplam/adet
print(f"Toplam={toplam}")
print(f"Ortalam={ortalama}")

# Program Çalıştığında Aşağıdaki çıktıyı verir.
# 1. Sayıyı Giriniz:95
# 2. Sayıyı Giriniz:45
# 3. Sayıyı Giriniz:26
# 4. Sayıyı Giriniz:85
# 5. Sayıyı Giriniz:0
# Döngü Sonlandı
# 5 tane sayı girdiniz
# Toplam=251
# Ortalam=50.2
