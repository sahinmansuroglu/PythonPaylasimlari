# Özyinelemeli fonskiyon tanımlaması 
# ile faktöriyel hesabı
def faktoriyel(sayi):
    if (sayi==0):
        return 1
    return sayi*faktoriyel(sayi-1)

for i in range(1,11):
    print(f"{i}!={faktoriyel(i)}")
    
# Programın Çıktısı Aşağıdadır.

1!=1
# 2!=2
# 3!=6
# 4!=24
# 5!=120
# 6!=720
# 7!=5040
# 8!=40320
# 9!=362880
# 10!=3628800
