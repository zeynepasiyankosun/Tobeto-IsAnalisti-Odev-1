#Soru-5: Kullanıcıdan alınan bir sayının palindrom olup olmadığını yazan bir program yazınız.

#Kullanıcıdan sayının istenmesi
sayi = input("Bir Sayı Giriniz: ")

#Girilen sayının tersinin alınması
tersSayi = sayi[::-1]  #[::-1], Python'da bir dilimleme (slicing) tekniği kullanılarak bir diziyi veya karakter dizisini ters çevirmek için kullanılan bir ifadedir. Bu ifade, bir diziyi veya karakter dizisini sondan başa doğru okur.

#Girilen sayı ile ters sayının karşılaştırılması ve sayının palindrom olup olmadığına karar verilmesi
if sayi == tersSayi:
    print("Bu sayı bir palindrom sayıdır.")
else: 
    print("Bu sayı bir palindrom sayı değildir.")
