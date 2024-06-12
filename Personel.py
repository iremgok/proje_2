class Personel:
    # initializer method ile değişkenler tanımlandı
    def __init__(self, personel_no, isim, soyisim, departman, maas):
        self.__personel_no = personel_no
        self.__isim = isim
        self.__soyisim = soyisim
        self.__departman = departman
        self.__maas = maas


    # Personel sınıfı için accessor methodları
    def get_personel_no(self):
        return self.__personel_no

    def get_isim(self):
        return self.__isim

    def get_soyisim(self):
        return self.__soyisim

    def get_departman(self):
        return self.__departman

    def get_maas(self):
        return self.__maas


    # Personel sınıfı için mutator methodları
    def set_personel_no(self, yeni_personel_no):
        self.__personel_no = yeni_personel_no

    def set_isim(self, yeni_isim):
        self.__isim = yeni_isim

    def set_soyisim(self, yeni_soyisim):
        self.__soyisim = yeni_soyisim

    def set_departman(self, yeni_departman):
        self.__departman = yeni_departman

    def set_maas(self, yeni_maas):
        self.__maas = yeni_maas


    # Str methodu ile ekrana yazdırır
    def __str__(self):
        return f"Personel: {self.get_isim()} {self.get_soyisim()}, Personel no: {self.get_personel_no()}, Departman: {self.get_departman()}, Maas: {self.get_maas()}"
