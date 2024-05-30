class Hasta:
    def __init__(self, isim, soyisim, Hasta_no, Dogum_tarihi, Hastalik, Tedavi_suresi=None):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__Hasta_no = Hasta_no
        self.__Dogum_tarihi = Dogum_tarihi
        self.__Hastalik = Hastalik
        self.__Tedavi_suresi = Tedavi_suresi


    def get_isim(self):
        return self.__isim

    def get_soyisim(self):
        return self.__soyisim
    
    def get_hasta_no(self):
        return self.__Hasta_no
    
    def get_dogum_tarihi(self):
        return self.__Dogum_tarihi
    
    def get_hastalik(self):
        return self.__Hastalik
    
    def get_tedavi(self):
        return self.__Tedavi_suresi
    
    
    def set_isim(self, yeni_isim):
        self.__isim = yeni_isim

    def set_soyisim(self, yeni_soyisim):
        self.__soyisim = yeni_soyisim   

    def set_hasta_no(self, yeni_hasta_no):
        self.__Hasta_no = yeni_hasta_no

    def set_dogum_tarihi(self, yeni_dogum_tarihi):
        self.__Dogum_tarihi = yeni_dogum_tarihi

    def set_hastalik(self, yeni_hastalik):
        self.__Hastalik = yeni_hastalik

    def set_tedavi(self, yeni_tedavi):
        self.__Tedavi_suresi = yeni_tedavi


    def tedavi_suresi_hesapla(self):
        en_az_hastalik = 3
        if self.__Hastalik == 'grip':
            return en_az_hastalik 
        elif self.__Hastalik == 'ozel tedavi':
            return en_az_hastalik + 7
        elif self.__Hastalik == 'normal tedavi':
            return en_az_hastalik + 2
        else:
            return en_az_hastalik + 3
    
    def __str__(self):
        return f"Hasta: {self.__isim} {self.__soyisim}, Hasta no: {self.__Hasta_no}, Dogum tarihi: {self.__Dogum_tarihi}, Hastalik: {self.__Hastalik}, Tedavi suresi: {self.__Tedavi_suresi} ay"

hasta1 = Hasta("Arda", "Donmez", 12347,  2005, "grip")
hasta2 = Hasta("Ayse", "Tas", 56412, 1987, "ozel tedavi")
hasta3 = Hasta("Mustafa", "Oztekin", 78913,  2002, "normal tedavi")

hasta1.set_tedavi(hasta1.tedavi_suresi_hesapla())
hasta2.set_tedavi(hasta2.tedavi_suresi_hesapla())
hasta3.set_tedavi(hasta3.tedavi_suresi_hesapla())