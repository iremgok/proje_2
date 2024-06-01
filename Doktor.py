class Doktor:
    # initializer method ile değişkenler tanımlandı
    def __init__(self, isim, soyisim, Uzmanlik, Deneyim_yili, Hastane, Maas):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__Uzmanlik = Uzmanlik
        self.__Deneyim_yili = Deneyim_yili
        self.__Hastane = Hastane
        self.__Maas = Maas

    #Doktor sınıfı için accessor methodu
    def get_isim(self):
        return self.__isim
    
    def get_soyisim(self):
        return self.__soyisim
    
    def get_uzmanlik(self):
        return self.__Uzmanlik

    def get_deneyim_yili(self):
        return self.__Deneyim_yili

    def get_hastane(self):
        return self.__Hastane

    def get_maas(self):
        return self.__Maas
    
    
    #Doktor sınıfı için mutator methodu
    def set_isim(self, yeni_isim):
        self.__isim = yeni_isim
    
    def set_soyisim(self, yeni_soyisim):
        self.__soyisim = yeni_soyisim

    def set_uzmanlik(self, yeni_uzmanlik):
        self.__Uzmanlik = yeni_uzmanlik

    def set_deneyim_yili(self, yeni_deneyim_yili):
        self.__Deneyim_yili = yeni_deneyim_yili

    def set_hastane(self, yeni_hastane):
        self.__Hastane = yeni_hastane

    def set_maas(self, yeni_maas):
        self.__Maas = yeni_maas


    # Maaş arttırma metodu, deneyim yılı 5 ve üstü olan doktorlar için maaşı 2000 artırır
    def maas_arttir(self):
        if self.get_deneyim_yili() >= 5:
            yeni_maas = self.get_maas() + 2000
            self.set_maas(yeni_maas)
        return self.get_maas()

    # Str method ile ekrana yazdırır
    def __str__(self):
        return f"Doktor: {self.get_isim()} {self.get_soyisim()}, Uzmanlik: {self.get_uzmanlik()}, Deneyim Yili: {self.get_deneyim_yili()}, Hastane: {self.get_hastane()}, Maas: {self.get_maas()}"


# Doktor nesneleri oluşturma
doktor1 = Doktor("irem", "Gok", "Kardiyoloji", 3, "Sehir Hastanesi", 25000)
doktor2 = Doktor("ikra", "Saygun", "Genel Cerrahi", 5, "Ozel Hastane", 14000)
doktor3 = Doktor("Ali", "Demir", "Ortopedi", 7, "Sehir Hastanesi", 20000)

# Doktorların maaşlarını arttırma
doktor1.set_maas(doktor1.maas_arttir())
doktor2.set_maas(doktor2.maas_arttir())
doktor3.set_maas(doktor3.maas_arttir())
