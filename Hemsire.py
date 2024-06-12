from Personel import Personel

class Hemsire(Personel):
    # initializer method ile değişkenler tanımlandı
    def __init__(self, personel_no, isim, soyisim, calisma_saati, sertifika, hastane, maas):
        super().__init__(personel_no, isim, soyisim, "Hemsire", maas)  # 'Hemsire' departman genel olarak atanır
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane


    # Hemsire sınıfı için accessor methodları
    def get_calisma_saati(self):
        return self.__calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def get_hastane(self):
        return self.__hastane


    # Hemsire sınıfı için mutator methodları
    def set_calisma_saati(self, yeni_calisma_saati):
        self.__calisma_saati = yeni_calisma_saati

    def set_sertifika(self, yeni_sertifika):
        self.__sertifika = yeni_sertifika

    def set_hastane(self, yeni_hastane):
        self.__hastane = yeni_hastane


    # Hemşirelerin çalışma saatinin 10 katını maaşa ekler
    def maas_arttir(self):
        yeni_maas = self.get_maas() + self.get_calisma_saati() * 10
        self.set_maas(yeni_maas)
        return self.get_maas()

    # Str method ile veriler ekrana yazdırır
    def __str__(self):
        return f"Hemsire: {self.get_isim()} {self.get_soyisim()}, Calisma saati: {self.get_calisma_saati()}, Sertifika: {self.get_sertifika()}, Hastane: {self.get_hastane()}, Maas: {self.get_maas()}"
    
