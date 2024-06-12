from Personel import Personel

class Doktor(Personel):
    # initializer method ile değişkenler tanımlandı
    def __init__(self, personel_no, isim, soyisim, uzmanlik, deneyim_yili, hastane, maas):
        super().__init__(personel_no, isim, soyisim, "Doktor", maas)    # 'Doktor' departman genel olarak atanır
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    # Doktor sınıfı için accessor methodu
    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane

    # Doktor sınıfı için mutator methodu
    def set_uzmanlik(self, yeni_uzmanlik):
        self.__uzmanlik = yeni_uzmanlik

    def set_deneyim_yili(self, yeni_deneyim_yili):
        self.__deneyim_yili = yeni_deneyim_yili

    def set_hastane(self, yeni_hastane):
        self.__hastane = yeni_hastane


    # Deneyim yılı 5 ve üstü olan doktorlar için maaşı %20 artırır
    def maas_arttir(self):
        if self.get_deneyim_yili() >= 5:
            yeni_maas = self.get_maas() * 1.20
            self.set_maas(yeni_maas)
        return self.get_maas()

    # Str method ile verileri ekrana yazdırır
    def __str__(self):
        return f"Doktor: {self.get_isim()} {self.get_soyisim()}, Uzmanlik: {self.get_uzmanlik()}, Deneyim Yili: {self.get_deneyim_yili()}, Hastane: {self.get_hastane()}, Maas: {self.get_maas()}"
