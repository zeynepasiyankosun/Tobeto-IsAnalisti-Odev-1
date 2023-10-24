#Soru-2: Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

#İşçinin mevcut maaşının ve zam oranının girilmesi:
maas = float(input("Lütfen mevcut maaşınızı giriniz: "))
zamOrani = float(input("Lütfen zam oranınızı(% olarak) giriniz: "))

#Zam miktarının hesaplanması
zamMiktari = maas * (zamOrani / 100)

#Zamlı maaşın hesaplanması
zamliMaas = maas + zamMiktari 

#Sonuç
print("Zamlı Maaşınız:", zamliMaas)