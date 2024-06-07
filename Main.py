import pandas as pd # type: ignore
from Doktor import doktor1, doktor2, doktor3
from Hemsire import hemsire1, hemsire2, hemsire3
from Hasta import hasta1, hasta2, hasta3
from Personel import personel1, personel2


<<<<<<< HEAD
# try-except bloğu
=======
>>>>>>> 0d82bce51ecdb7081d7ef1d63f9bb85867450c35
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
        "Tedavi_suresi": [None, None, None, None, None, None, None, None, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()]
    })
    # Boş olan alanları 0 ile doldur
    personeller.fillna(0, inplace=True)

    # Personel bilgilerini döndüren fonksiyon
    def get_personeller():
        global personeller
        return personeller
    
<<<<<<< HEAD
    
=======
>>>>>>> 0d82bce51ecdb7081d7ef1d63f9bb85867450c35
    # Alfabetik göre sıralama
    siralanmis_isimler = get_personeller().sort_values(by='Ad')
    print(siralanmis_isimler)
    print("\n")


    # 5 yıl ve daha fazla süredir çalışan doktor sayısı
    doktor_sayisi = 0
    for deneyim_yili in get_personeller()['Deneyim_yili']:
        if deneyim_yili != 0 and int(deneyim_yili) >= 5:
            doktor_sayisi += 1
    print("5 Yıl ve Daha Fazla Süredir Çalışan Doktor Sayısı: ", doktor_sayisi)
    print("\n")


    # Uzmanlık sayıları
    uzmanlik_sayisi = {}
    for uzmanlik in get_personeller()['Uzmanlik']:
        if uzmanlik != 0:
            if uzmanlik in uzmanlik_sayisi:
                uzmanlik_sayisi[uzmanlik] += 1
            else:
                uzmanlik_sayisi[uzmanlik] = 1
    for uzmanlik, sayi in uzmanlik_sayisi.items():
        print(f"{uzmanlik}: {sayi}")


    # Toplam doktor sayısı
    toplam_doktor = sum(1 for uzmanlik in get_personeller()['Uzmanlik'] if uzmanlik != 0)
    print("Toplam Doktor Sayısı: ", toplam_doktor)
    print("\n")


    # Maaşı 7000'den fazla olan personeller
    print("Maaşı 7000'den Fazla Olan Personeller: ")
    for idx, row in get_personeller().iterrows():
<<<<<<< HEAD
        if int(row['Maas']) > 7000:     # row, her bir satırı temsil eder ve bu satırdaki verilere sütun isimleri ile erişilebilir
=======
        if int(row['Maas']) > 7000:
>>>>>>> 0d82bce51ecdb7081d7ef1d63f9bb85867450c35
            print(row)
            print("\n")


    # 1990 yılından sonra doğan hastalar
    print("1990 Yılından Sonra Doğan Hastalar: ")
    for idx, row in get_personeller().iterrows():
        if row['Dogum_tarihi'] != 0 and int(row['Dogum_tarihi']) > 1990:
            print(row)
            print("\n")


<<<<<<< HEAD
    # Belli sütunlara yeni DataFrame
=======
    # Yeni DataFrame
>>>>>>> 0d82bce51ecdb7081d7ef1d63f9bb85867450c35
    yeni_df = get_personeller()[["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim_yili", "Hastalik", "Tedavi_suresi"]]
    print(yeni_df)
    print("\n")


<<<<<<< HEAD
    # Tüm nesneleri ekrana yazdırma
=======
>>>>>>> 0d82bce51ecdb7081d7ef1d63f9bb85867450c35
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
