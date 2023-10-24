#Soru-4: Dairenin alanını ve çevresini hesaplayan python kodunu yazınız. (dairenin yarıçapını kullanıcıdan alınız)

import math  #import math ifadesi, Python'da yerleşik olarak gelen math modülünü içe aktarmak veya içe dahil etmek için kullanılır.

#Kullanıcının dairenin yarıçapını belirtmesi
yaricap = float(input("Lütfen Dairenin Yarıçapını Giriniz: "))

#Dairenin alanının hesaplanması
alan = math.pi * yaricap**2

#Dairenin çevresinin hesaplanması
cevre = 2 * math.pi * yaricap

#Sonuçlar
print("Dairenin Alanı:", alan)
print("Dairenin Çevresi", cevre)

