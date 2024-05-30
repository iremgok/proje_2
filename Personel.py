class Personel:
    def __init__(self, Personel_no, isim, soyisim, Departman, Maas):
        self.__Personel_no = Personel_no
        self.__isim = isim
        self.__soyisim = soyisim
        self.__Departman = Departman
        self.__Maas = Maas


    def get_personel_no(self):
        return self.__Personel_no

    def get_isim(self):
        return self.__isim

    def get_soyisim(self):
        return self.__soyisim

    def get_departman(self):
        return self.__Departman

    def get_maas(self):
        return self.__Maas


    def set_personel_no(self, yeni_personel_no):
        self.__Personel_no = yeni_personel_no

    def set_isim(self, yeni_isim):
        self.__isim = yeni_isim

    def set_soyisim(self, yeni_soyisim):
        self.__soyisim = yeni_soyisim

    def set_departman(self, yeni_departman):
        self.__Departman = yeni_departman

    def set_maas(self, yeni_maas):
        self.__Maas = yeni_maas


    def __str__(self):
        return f"Personel: {self.__isim} {self.__soyisim}, Personel no: {self.__Personel_no}, Departman: {self.__Departman}, Maas: {self.__Maas}"
    
personel1 = Personel(15621, "Hatice", "Gungor", "Temizlik", 5000)
personel2 = Personel(12389, "Burak", "Yilmaz", "Guvenlik", 8000)