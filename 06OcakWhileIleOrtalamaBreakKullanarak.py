# Program while döngüsü ile kulanacıdan  sürekli sayı girmesini isteyecektir.
# Eğer kullanıcı 0 girdiyse o ana kadar girlen sayıların toplamını adedini
# ve ortalamasını ekrana yazdıracaktır.
# Ancak Sonsuz Döngü kurulmuştur ve bu sonsuz döngü
# girilen sayının if ile  0 'a eşit olup olmadıgı test edilerek;
# Eğer sayı==0 ise  break ile döngü kırılarak sonlandırılmıştır.

toplam=0
sayi=45
adet=0
while(True):
    adet=adet+1
    sayi=int(input(f"{adet}. Sayıyı Giriniz:"))
    toplam=toplam+sayi
    if sayi==0:
        break

print("Döngü Sonlandı")
print(f"{adet} tane sayı girdiniz")
ortalama=toplam/adet
print(f"Toplam={toplam}")
print(f"Ortalam={ortalama}")

# Program Çalıştığında Aşağıdaki çıktıyı verir.
1. Sayıyı Giriniz:85
2. Sayıyı Giriniz:45
3. Sayıyı Giriniz:63
4. Sayıyı Giriniz:85
5. Sayıyı Giriniz:41
6. Sayıyı Giriniz:0
Döngü Sonlandı
6 tane sayı girdiniz
Toplam=319
Ortalam=53.166666666666664
