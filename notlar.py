#Bu bir yorum satırıdır

#Ekrana yazdırma
print("Merhaba Dünya!")

#Kulanıcıdan veri alma
isim = input("Adın nedir? ")

#Temel Veri Tipleri
x = 5           # int
y = 3.14        # float
isim = "Zeynep" # str
aktif = True    # bool

#Tip Dönüşümü
yas = int("19") #19 str halindeyken başına int yazıp inte çevirdik
metin = str(42) #49 bir intken başına str yazarak str haline getirdik

isim = "Zeynep"
print(isim.upper())   # ZEYNEP
print(isim[0:3])      # Zey (başlangıç dahil edilir,bitiş dahil edilmez)
print(f"Merhaba {isim}")  # formatted string

#Operatörler

# Aritmetik: + - * / // % **
# Karşılaştırma: == != > < >= <=
# Mantıksal: and or not
# Üyelik: "a" in "zeynep" → False

#if-elif-else
yas = 18
if yas >= 18:
    print("Reşit")
else:
    print("Değil")

#for döngüsü
for i in range(5): #0,1,2,3,4 sayılarının hepsini tek tek yazar.Bir dizideki tüm elemanlara aynı işlem yapılacağı zaman kullanılır
    print(i)

#while döngüsü
x = 0
while x < 3:
    print("Merhaba")
    x += 1

#fonksiyonlar
def topla(a, b):
    return a + b

print(topla(2, 3))

#varsayılan parametre
def selamla(isim="Zeynep"):
    print(f"Merhaba {isim}!")
    #kullanıcı parametre yazarsa o kullanılır,yazmazsa "zeynep" değeri otomatik devreye girer

#lambda (kısa ve basit fonk tanımlamaları)
kare = lambda x: x ** 2 #x parametre,x**2 ise return yerine geçer yani döndürülecek ifade
print(kare(5))   # 25

#Koleksiyonlar
#Listeler-değiştirilebilir veri tipi (mutable)
liste = [1, 2, 3]
liste.append(4)
liste.remove(2)
print(len(liste))

#tuple-değiştirilemez veri tipi(immutable)
renkler = ("kırmızı", "mavi", "yeşil")
renkler.append("sarı")  # Hata verir
renkler.remove("mavi")  # Hata verir

#kümeler-değiştirilebilir ama sıralı değil(index yok)
#her değerden bir tane vardır tekrar olmaz
sayilar = {1, 2, 3}

#dictionary 
ogrenci = {"isim": "Zeynep", "yas": 19}
print(ogrenci["isim"])


#Hata yönetimi (try-except-finally)
try:
    #hata çıkma ihtimali olan kod
    x = int(input("Sayı gir: "))
except ValueError:
    #hata olursa burası çalışır
    print("Geçersiz giriş!")
else:
    #hata olmazsa çalışır
    print("hata yok,işlem başarılı")
finally: 
    #ne olursa olsun çalışır
    print("Bitti.")


#Dosya İşlemleri
dosya = open("deneme.txt", "r") #eğr dosya kod ile aynı klasördeyse bu iekilde yazabilirsin,değilse tam yolu belirtmen gerek
dosya = open("C:/Users/Zeynep/Desktop/veriler/deneme.txt", "r") #bu şekilde

#dosyayı açıp okumak
dosya = open("deneme.txt", "r")
icerik = dosya.read()
print(icerik)
dosya.close() #dosyayı kapatmazsan arka planda açık kalabilir,büyük projelerde sıkıntı oluşturur

#dosyaya yazmak
dosya = open("deneme.txt", "w")
dosya.write("Merhaba Zeynep!\n") #dosyayı tamamen sıfırlar ve yeni metni yazar,önceden içinde olanlar silinir
dosya.write("Python öğreniyorum :)\n")
dosya.close() 

#ekleme yapmak
dosya = open("deneme.txt", "a") 
dosya.write("Bu satır sona eklendi.\n") #silmeden sadece sona ekleme yapar
dosya.close()


#with kullanarak dosya açmak
with open("deneme.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)
# with biter bitmez dosya otomatik kapanır,bir daha close yazmaya gerek yok

#finally kullanımı
try:
    dosya = open("deneme.txt", "r") #burada with kullanmaya gerek yok çünkü zaten sonda her türlü kapatıyoruz
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı!")
finally:
    dosya.close()   # hata olsa bile dosya kapanır

#dosya açma modları

# r--sadece okuma
# w--sadece yazma
# a--ekleme
# x-sadece tebi dosya oluşturur(zaten varsa hata verir)

#OOP
class Araba:
    def __init__(self, marka, model): #sınıf çağırıldığında otomatik çalışan yapıcı fonksiyon
        #self : o sınıftan türetilen nesneyi temsil eder
        self.marka = marka
        self.model = model

    def bilgi(self):
        print(f"Marka: {self.marka}, Model: {self.model}")

araba1 = Araba("Toyota", "Corolla")
araba1.bilgi()

#Inheritance
class ElektrikliAraba(Araba): #elektrikli araba adında yeni sınıf oluşturdum,araba sınıfının özelliklerini devraldı
    def __init__(self, marka, model, batarya):
        super().__init__(marka, model) #araba sınıfının (parentın) fonksiyonlarına erişir super() ile
        self.batarya = batarya #marka ve modeli arabanın init fonk ile tanımladık,elektrikli arabaya özel batarya da ekledi

#Kavramlar
#Encapsulation (Kapsülleme) : Veriyi ve metotları bir sınıf içinde toplamak
#Inheritance (Kalıtım) : Bir sınıfın başka bir sınıftan özellik alması
#Polymorphism (Çok biçimlilik) : Aynı isimli metodun farklı davranabilmesi
#Abstraction (Soyutlama) : Gereksiz detayları gizleyip sadece gerekli fonksiyonları göstermek
