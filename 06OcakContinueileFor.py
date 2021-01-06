# 1 ile 20 arasındaki çift sayıları ekrana yazdırma
# Bu işlem yapılırken döngü değişkeni olan i'nin tek olup olmadığı mod alma ile 
# test edilir eğer i  tek  ise continue komutu çalışıtırılarak döngü o tek sayı
# ekrana yazdıılmadan bir sonraki değerden devam etmesini sağlayacaktır. Böylece ekrana 
#yazdırma işlemi sadece çift sayılarda olacaktır.

for i in range(1,21):

    if i % 2 ==1:
        continue
    print(f"{i}")
print("Program Bitti")

# Programın Çıktısı Aşağıdadır.
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# Program Bitti
