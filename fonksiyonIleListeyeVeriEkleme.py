liste=[]

def ekle(ad):
    liste.append(ad)
    print(f"{ad} adlı kişi Listeye Eklendi")

def veriGir(mesaj):
    return input(mesaj)

def verileriListe():
    print("Verileriniz Listeleniyor.....")
    siraNo=1
    for herbirAd in liste:
        print(f"{siraNo}:{herbirAd}")
        siraNo=siraNo+1

for i in range(1,6):
    ekle(veriGir(f"{i}. Adı Giriniz:"))

verileriListe()
