#Soru-3: Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız. 

#Kullanıcının üç sayı gireceği alanın oluşturulması
sayi1 = (float(input("Lütfen Birinci Sayıyı Giriniz:")))
sayi2 = (float(input("Lütfen İkinci Sayıyı Giriniz:")))
sayi3 = (float(input("Lütfen Üçüncü Sayıyı Giriniz:")))

#En büyük sayının bulunması için:
enBuyukSayi = max(sayi1, sayi2, sayi3)

#Sonuç
print("En büyük sayı:", enBuyukSayi)