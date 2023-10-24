# SORU-1: Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle endeksini (VKİ=ağırlıkk/(boy*boy)) hesaplayınız.

#Kullanıcıya ait boy ve ağırlık bilgilerinin girilmesi
boy = float(input("Lütfen boyunuzu (santimetre cinsinden) giriniz: ")) #input() fonksiyonu, kullanıcının klavyeden veri girmesine izin verir ve bu girdiyi bir metin (string) olarak alır.input() fonksiyonu ile alınan metin verilerini sayılara dönüştürmek için float() fonksiyonunu kullanılır.
agirlik = float(input("Lütfen ağırlığınızı (kilogram cinsinden) giriniz: "))

#Vücut Kitle Endeksinin hesaplanması
VKİ = agirlik / (boy * boy)

#Sonuç
print("Vücut Kitle İndeksiniz:", VKİ)