#Uygulama klavyeden döngü yardımıyla 10 adet sayı girmemizi ister 
#Sonra bu sayıları toplayıp ekrana toplamı yazar
#Ancak klavyeden girilen sayının if Yapılan kontrolü sonrasında
#Eğer Sayı 0'a eşitse döngü break komutu ile kırılacaktır ve
# o ana kadar girilen sayıların toplamı ekrana yazılacaktır.
toplam=0
for i in range(1,11):
    sayi=int(input(f"{i}. Sayıyı Giriniz"))
    toplam=toplam+sayi
    if sayi==0:
        break
print(f"Toplam={toplam}")
print("Program Bitti..")

# Program Çalıştırıldığında Aşağıdaki Çıktı Alınmıştır
# 1. Sayıyı Giriniz95
# 2. Sayıyı Giriniz45
# 3. Sayıyı Giriniz36
# 4. Sayıyı Giriniz0
# Toplam=176
# Program Bitti..

