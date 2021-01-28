# Faktöriyeli, fonskiyon içinde for
# döngüsü kullanarak hesaplatma
def faktoriyel(sayi):
    if (sayi==0 & sayi==1):
        return 1
    sonuc=1
    for i in range(2,sayi+1):
        sonuc=sonuc*i
    return  sonuc

for i in range(1,11):
    print(f"{i}!={faktoriyel(i)}")

# Programın Çıktısı Aşağıdadır.
# 1!=1
# 2!=2
# 3!=6
# 4!=24
# 5!=120
# 6!=720
# 7!=5040
# 8!=40320
# 9!=362880
# 10!=3628800
