import pandas as pd # type: ignore
from Doktor import doktor1, doktor2, doktor3
from Hemsire import hemsire1, hemsire2, hemsire3
from Hasta import hasta1, hasta2, hasta3
from Personel import personel1, personel2

try:

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
    personeller.fillna(0, inplace=True)

    def get_personeller():
        global personeller
        return personeller
    
    siralanmis_isimler = get_personeller().sort_values(by='Ad')
    print(siralanmis_isimler)
    print("\n")

    doktor_sayisi = 0
    for deneyim_yili in get_personeller()['Deneyim_yili']:
        deneyim_yili = int(deneyim_yili)
        if deneyim_yili >= 5:
            doktor_sayisi += 1
    print("5 Yıl ve Daha Fazla Calisan Doktor Sayisi: ", doktor_sayisi)
    print("\n")

    uzmanlik_sayisi = {}
    for uzmanlik in get_personeller()['Uzmanlik']:
        if uzmanlik != None:
            if uzmanlik in uzmanlik_sayisi:
                uzmanlik_sayisi[uzmanlik] += 1
            else:
                uzmanlik_sayisi[uzmanlik] = 1
    for uzmanlik, sayi in uzmanlik_sayisi.items():
        print(f"{uzmanlik}: {sayi}")

    toplam_doktor = 0
    for uzmanlik in get_personeller()['Uzmanlik']:
        if uzmanlik != None:
            toplam_doktor += 1
    print("Toplam Doktor Sayisi: ", toplam_doktor)
    print("\n")

    for idx, row in get_personeller().iterrows():
        maas = int(row['Maas'])
        if maas > 7000:
            print("Maasi 7000'den Fazla Olan Personeller: ")
            print(row)
            print("\n")

    for idx, row in get_personeller().iterrows():
        tarih = int(row['Dogum_tarihi'])
        if tarih > 1990:
            print("1990 Yilindan Sonra Dogan Hastalar: ")
            print(row)
            print("\n")

    yeni_df = get_personeller()[["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim_yili", "Hastalik", "Tedavi_suresi"]]
    print(yeni_df)
    print("\n")

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
