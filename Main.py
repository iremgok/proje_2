import pandas as pd # type: ignore
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
from Personel import Personel


# Nesneleri oluşturma
doktor1 = Doktor(30026, "irem", "Gok", "Ortopedi", 3, "Denizli Sehir Hastanesi", 25000)     # indeks hatası olmaması için personel_no verdim
doktor2 = Doktor(30213, "ikra", "Saygun", "Genel Cerrahi", 5, "Medicana Ozel Hastane", 14000)
doktor3 = Doktor(30854, "Ali", "Demir", "Kardiyoloji", 7, "izmir Sehir Hastanesi", 20000)
hemsire1 = Hemsire(23569, "Zeynep", "Sahin", 13, "Yasli Bakim", "Gazi Ozel Hastane", 6000)      
hemsire2 = Hemsire(23458, "Efe", "Baransel", 11, "Hastane Sekreteri", "Gazi Ozel Hastane", 7000)
hemsire3 = Hemsire(23751, "Zehra", "Acikgoz", 9, "Cocuk Gelisimi", "Izmir Sehir Hastanesi", 9000)
personel1 = Personel(12761, "Hatice", "Gungor", "Temizlik Görevlisi", 5000)
personel2 = Personel(12389, "Burak", "Yılmaz", "Güvenlik Görevlisi", 8000)
hasta1 = Hasta("Mustafa", "Donmez", 2005, "grip", 12347)
hasta2 = Hasta("Elif", "Tas", 1987, "kirik", 56412)
hasta3 = Hasta("Arda", "Oztekin", 2002, "zature", 78913)

# Doktorlar için maaş arttır fonksiyonu çağrılır
doktor1.set_maas(doktor1.maas_arttir())
doktor2.set_maas(doktor2.maas_arttir())
doktor3.set_maas(doktor3.maas_arttir())

# Hemşirelerin maaşlarını arttırma donksiyonları çağrılır
hemsire1.set_maas(hemsire1.maas_arttir())
hemsire2.set_maas(hemsire2.maas_arttir())
hemsire3.set_maas(hemsire3.maas_arttir())

# Tedavi süresi hesapla fonksiyonu çağrılır
hasta1.set_tedavi_suresi(hasta1.tedavi_suresi_hesapla())
hasta2.set_tedavi_suresi(hasta2.tedavi_suresi_hesapla())
hasta3.set_tedavi_suresi(hasta3.tedavi_suresi_hesapla())


# try-except bloğu
try:
    # Personel bilgilerini DataFrame'e dönüştürme
    personeller = pd.DataFrame({
        "Ad": [personel1.get_isim(), personel2.get_isim(), doktor1.get_isim(), doktor2.get_isim(), doktor3.get_isim(), hemsire1.get_isim(), hemsire2.get_isim(), hemsire3.get_isim(), hasta1.get_isim(), hasta2.get_isim(), hasta3.get_isim()],
        "Soyad": [personel1.get_soyisim(), personel2.get_soyisim(), doktor1.get_soyisim(), doktor2.get_soyisim(), doktor3.get_soyisim(), hemsire1.get_soyisim(), hemsire2.get_soyisim(), hemsire3.get_soyisim(), hasta1.get_soyisim(), hasta2.get_soyisim(), hasta3.get_soyisim()],
        "Personel_no": [personel1.get_personel_no(), personel2.get_personel_no(), None, None, None, None, None, None, None, None, None],
        "Departman": [personel1.get_departman(), personel2.get_departman(), doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), None, None, None, None, None, None],
        "Maas": [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(), hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), None, None, None],
        "Uzmanlik": [None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), None, None, None, None, None, None],
        "Deneyim_yili": [None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), None, None, None, None, None, None],
        "Hastane": [None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane(), None, None, None],
        "Calisma_saati": [None, None, None, None, None, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(), None, None, None],
        "Sertifika": [None, None, None, None, None, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(), None, None, None],
        "Hasta_no": [None, None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
        "Dogum_tarihi": [None, None, None, None, None, None, None, None, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
        "Hastalik": [None, None, None, None, None, None, None, None, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
        "Tedavi_suresi": [None, None, None, None, None, None, None, None, hasta1.get_tedavi_suresi(), hasta2.get_tedavi_suresi(), hasta3.get_tedavi_suresi()]
    })
    personeller.fillna(0, inplace=True)     # Boş olan alanları 0 ile doldur
    
    
    # Hastaların isimlerini alfabetik sıraya göre sıralama
    print("\n")
    print("Hastalarin Alfabetik Siraya Gore Dataframe: ")
    hastalar = personeller[personeller['Hasta_no'] != 0]     # personeller listesinden hasta_no sütununu çekerek yeni personeller datafremi oluşturur
    siralanmis_hastalar = hastalar.sort_values(by='Ad')
    print(siralanmis_hastalar)
    print("\n")   


    # 5 yıl ve daha fazla süredir çalışan doktor sayısı
    doktor_sayisi = 0
    for deneyim_yili in personeller['Deneyim_yili']:
        if int(deneyim_yili) >= 5:
            doktor_sayisi += 1
    print("5 Yil ve Daha Uzun Suredir Calisan Doktor Sayisi: ", doktor_sayisi)
    print("\n")


    # Uzmanlık sayıları
    uzmanlik_sayisi = {}    # uzmanlık dictionarysi oluşturulur ve uzmanlik değerleri buraya atanır
    for uzmanlik in personeller['Uzmanlik']:
        if uzmanlik != 0:
            if uzmanlik in uzmanlik_sayisi:
                uzmanlik_sayisi[uzmanlik] += 1
            else:
                uzmanlik_sayisi[uzmanlik] = 1
    for uzmanlik, sayi in uzmanlik_sayisi.items():
        print(f"{uzmanlik}: {sayi}")


    # Toplam doktor sayısı
    toplam_doktor = 0
    for idx, row in personeller.iterrows():
        if row['Uzmanlik'] != 0:
            toplam_doktor += 1
    print("Toplam Doktor Sayisi: ", toplam_doktor)
    print("\n")


    # Maaşı 7000'den fazla olan personeller, doktorlar ve hemşireler
    print("Maasi 7000'den Fazla Olan Personeller: ")
    for idx, row in personeller.iterrows():
        if int(row['Maas']) > 7000:     # row, her bir satırı temsil eder ve iterrows ile bu satırları döndürmayi sağlar
            print(row)
            print("\n")


    # 1990 yılından sonra doğan hastalar
    print("1990 Yilindan Sonra Dogan Hastalar: ")
    for idx, row in personeller.iterrows():
        if int(row['Dogum_tarihi']) > 1990:
            print(row)
            print("\n")


    # Belli sütunlarla yeni DataFrame
    print("istenilen Sutunlara Gore Yeni Dataframe: ")
    yeni_df = personeller[["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim_yili", "Hastalik", "Tedavi_suresi"]]
    print(yeni_df)
    print("\n")


    # Tüm nesneleri ekrana yazdırma
    print(str(doktor1))
    print(str(doktor2))
    print(str(doktor3))
    print(str(hemsire1))
    print(str(hemsire2))
    print(str(hemsire3))
    print(str(hasta1))
    print(str(hasta2))
    print(str(hasta3))
    print(str(personel1))
    print(str(personel2))


except ValueError:
    print("Hata!")
    
