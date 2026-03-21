import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_luodun_kassapaatteen_myydyt_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_kun_ostetaan_edullinen_lounas_ja_maksu_riittaa_oikea_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)

    def test_kateisosto_toimii_kun_ostetaan_maukas_lounas_ja_maksu_riittaa_oikea_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500),100)

    def test_kateisosto_toimii_kun_ostetaan_edullinen_lounas_ja_maksu_riittaa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_toimii_kun_ostetaan_maukas_lounas_ja_maksu_riittaa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_toimii_kun_ostetaan_edullinen_ja_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_kun_ostetaan_maukas_ja_myydyt_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_toimii_kun_edulliseen_maksu_ei_riita_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_kun_maukkaaseen_maksu_ei_riita_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_kun_edulliseen_maksu_ei_riita_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(20), 20)

    def test_kateisosto_toimii_kun_maukkaaseen_maksu_ei_riita_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(20), 20)

    def test_kateisosto_toimii_kun_edulliseen_maksu_ei_riita_myydyt_lounaat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_kun_maukkaaseen_maksu_ei_riita_myydyt_lounaat_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_kun_edulliseen_tarpeeksi_rahaa_veloitetaan_summa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_korttiosto_toimii_kun_maukkaaseen_tarpeeksi_rahaa_veloitetaan_summa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_korttiosto_toimii_kun_edulliseen_tarpeeksi_rahaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_korttiosto_toimii_kun_maukkaaseen_tarpeeksi_rahaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_korttiosto_toimii_kun_kortilla_tarpeeksi_rahaa_edulliseen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_toimii_kun_kortilla_tarpeeksi_rahaa_maukkaaseen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_toimii_kun_kortilla_ei_tarpeeksi_rahaa_edulliseen_kortin_rahamaara_ei_muutu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)


    def test_korttiosto_toimii_kun_kortilla_ei_tarpeeksi_rahaa_maukkaaseen_kortin_rahamaara_ei_muutu(self):
        self.maksukortti.saldo = 200
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)


    def test_korttiosto_toimii_kun_kortilla_ei_tarpeeksi_rahaa_edulliseen_lounaiden_maara_ei_muutu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_korttiosto_toimii_kun_kortilla_ei_tarpeeksi_rahaa_maukkaaseen_lounaiden_maara_ei_muutu(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_korttiosto_toimii_kun_kortilla_ei_tarpeeksi_rahaa_edulliseen_palautetaan_false(self):
        self.maksukortti.saldo = 100
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)


    def test_korttiosto_toimii_kun_kortilla_ei_tarpeeksi_rahaa_maukkaaseen_palautetaan_false(self):
        self.maksukortti.saldo = 100
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_kortille_rahaa_ladatessa_kassassa_oleva_rahamäärä_kasvaa_samalla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_ladataan_negatiivinen_summa_kortin_saldo_säilyy(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_kortille_ladataan_negatiivinen_summa_kassan_saldo_säilyy(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
