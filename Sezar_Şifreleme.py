alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

def caesar(metin, kaydirma, yon):
    sonuc = ""
    if yon == "çöz":
        kaydirma = -kaydirma
        
    for karakter in metin:
        if karakter in alfabe:
            yeni_indeks = (alfabe.index(karakter) + kaydirma) % 29
            sonuc += alfabe[yeni_indeks]
        else:
            sonuc += karakter
            
    print(f"Sonuç: {sonuc}")

print("--- Türkçe Sezar Şifreleme Algoritması ---")

while True:
    islem = input("Şifrelemek için 'şifrele', çözmek için 'çöz' yazın: ").lower()
    mesaj = input("Mesajınızı yazın: ").lower()
    
    sayi = int(input("Kaydırma sayısını girin: ")) % 29
    
    caesar(mesaj, sayi, islem)
    
    devam = input("\nBaşka bir işlem yapmak ister misiniz? (evet/hayır): ").lower()
    if devam != "evet":
        print("Program sonlandırıldı. İyi günler!")
        break