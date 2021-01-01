liste=["Ali","Veli","Mehmet", "Arda"]
#Alttaki komut tüm listeyi listeler
print(f"Tüm Liste={liste}")
# Dizinin İlk elemanını Listelem
print(f"Listenin ilk Elamanı={liste[0]}")
print(f"Listenin Son Elamanı={liste[3]}")


# Listeye Eleman Ekleme
liste.append("Erkan")
# Listenin 2. Elamanından Sonra Serkan İsmini Ekleme
liste.insert(2,"Serkan")
print(f"Ekleme Sonrası Tüm Liste={liste}")
# listeden eleman Sileme
liste.remove("Ali")
print("Dizinin Tüm elemanlarını Alt alta yazdırma")


for herbirEleman in liste:
    print(f"{herbirEleman}")
