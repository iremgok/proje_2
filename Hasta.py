class Hasta:
    # initializer method ile değişkenler tanımlandı
    def __init__(self, isim, soyisim, dogum_tarihi, hastalik, hasta_no=None, tedavi_suresi=None):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__hasta_no = hasta_no
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi_suresi = tedavi_suresi


    # Hasta sınıfı için accessor methodları
    def get_isim(self):
        return self.__isim

    def get_soyisim(self):
        return self.__soyisim
    
    def get_hasta_no(self):
        return self.__hasta_no
    
    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    
    def get_hastalik(self):
        return self.__hastalik
    
    def get_tedavi_suresi(self):
        return self.__tedavi_suresi
    

    # Hasta sınıfı için mutator methodları
    def set_isim(self, yeni_isim):
        self.__isim = yeni_isim

    def set_soyisim(self, yeni_soyisim):
        self.__soyisim = yeni_soyisim   

    def set_hasta_no(self, yeni_hasta_no):
        self.__hasta_no = yeni_hasta_no

    def set_dogum_tarihi(self, yeni_dogum_tarihi):
        self.__dogum_tarihi = yeni_dogum_tarihi

    def set_hastalik(self, yeni_hastalik):
        self.__hastalik = yeni_hastalik

    def set_tedavi_suresi(self, yeni_tedavi_suresi):
        self.__tedavi_suresi = yeni_tedavi_suresi


    # Tedavi çeşidine göre tedavi süresi hesaplayan method
    def tedavi_suresi_hesapla(self):
        en_az_hastalik = 2
        if self.get_hastalik() == 'grip':
            return en_az_hastalik 
        elif self.get_hastalik() == 'kirik':
            return en_az_hastalik + 5
        elif self.get_hastalik() == 'zature':
            return en_az_hastalik + 4
        else:
            return en_az_hastalik + 1
  
    # Str method ile verileri ekrana yazdırır
    def __str__(self):
        return f"Hasta: {self.get_isim()} {self.get_soyisim()}, Hasta no: {self.get_hasta_no()}, Dogum tarihi: {self.get_dogum_tarihi()}, Hastalik: {self.get_hastalik()}, Tedavi suresi: {self.get_tedavi_suresi()} ay"


# Hasta nesneleri oluşturma
hasta1 = Hasta("Mustafa", "Donmez", 2005, "grip", 12347)
hasta2 = Hasta("Elif", "Tas", 1987, "kirik", 56412)
hasta3 = Hasta("Arda", "Oztekin", 2002, "zature", 78913)

# Tedavi süresi hesapla fonksiyonu çağrılır
hasta1.set_tedavi_suresi(hasta1.tedavi_suresi_hesapla())
hasta2.set_tedavi_suresi(hasta2.tedavi_suresi_hesapla())
hasta3.set_tedavi_suresi(hasta3.tedavi_suresi_hesapla())
