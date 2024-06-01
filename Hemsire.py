class Hemsire:
    def __init__(self, isim, soyisim, Calisma_saati, Sertifika, Hastane, Maas):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__Calisma_saati = Calisma_saati
        self.__Sertifika = Sertifika
        self.__Hastane = Hastane
        self.__Maas = Maas

    def get_isim(self):
        return self.__isim
    
    def get_soyisim(self):
        return self.__soyisim

    def get_calisma_saati(self):
        return self.__Calisma_saati

    def get_sertifika(self):
        return self.__Sertifika

    def get_hastane(self):
        return self.__Hastane
    
    def get_maas(self):
        return self.__Maas
    
    
    def set_isim(self, yeni_isim):
        self.__isim = yeni_isim
    
    def set_soyisim(self, yeni_soyisim):
        self.__soyisim = yeni_soyisim
    
    def set_calisma_saati(self, yeni_calisma_saati):
        self.__Calisma_saati = yeni_calisma_saati

    def set_sertifika(self, yeni_sertifika):
        self.__Sertifika = yeni_sertifika

    def set_hastane(self, yeni_hastane):
        self.__Hastane = yeni_hastane

    def set_maas(self, yeni_maas):
        self.__Maas = yeni_maas

    def maas_arttir(self):
        yeni_maas = self.get_maas() + self.get_calisma_saati() * 10
        self.set_maas(yeni_maas)
        return self.get_maas()

    def __str__(self):
        return f"Hemsire: {self.get_isim()} {self.get_soyisim()}, Calisma saati: {self.get_calisma_saati()}, Sertifika: {self.get_sertifika()}, Hastane: {self.get_hastane()}, Maas: {self.get_maas()}"


hemsire1 = Hemsire("Zeynep", "Sahin", 13, "Yasli Bakim", "Ozel Hastane", 6500)
hemsire2 = Hemsire("Efe", "Baransel", 11, "Hastane Sekreteri", "Ozel Hastane", 7000)
hemsire3 = Hemsire("Zehra", "Acıkgoz", 9, "Cocuk Gelisimi", "Sehir Hastanesi", 9000)

hemsire1.set_maas(hemsire1.maas_arttir())
hemsire2.set_maas(hemsire2.maas_arttir())
hemsire3.set_maas(hemsire3.maas_arttir())
