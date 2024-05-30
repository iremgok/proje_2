class Doktor:
    def __init__(self, isim, soyisim, Uzmanlik, Deneyim_yili, Hastane, Maas):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__Uzmanlik = Uzmanlik
        self.__Deneyim_yili = Deneyim_yili
        self.__Hastane = Hastane
        self.__Maas = Maas


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


    def maas_arttir(self):
        if self.__Deneyim_yili >= 5:
            self.__Maas += 2000
            return self.__Maas
        else:
            return self.__Maas

    def __str__(self):
        return f"Doktor: {self.__isim} {self.__soyisim}, Uzmanlik: {self.__Uzmanlik}, Deneyim Yili: {self.__Deneyim_yili}, Hastane: {self.__Hastane}, Maas: {self.__Maas}"

doktor1 = Doktor("irem", "Gok", "Kardiyoloji", 3, "Sehir Hastanesi", 25000)
doktor2 = Doktor("ikra", "Saygun", "Genel Cerrahi", 5, "Ozel Hastane", 14000)
doktor3 = Doktor("Ali", "Demir", "Ortopedi", 7, "Sehir Hastanesi", 18000)

doktor1.set_maas(doktor1.maas_arttir())
doktor2.set_maas(doktor2.maas_arttir())
doktor3.set_maas(doktor3.maas_arttir())