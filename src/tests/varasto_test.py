import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_varastoon_laitto(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastoon_laitto_negatiivinen(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liikaa_varastosta_otto(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)

    def test_arastosta_otto_negatiivinen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0.0)
    
    def test_varasto_tulostuu(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

class TestVarastoB(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-10, -10)

    def test_varaston_virheellinen_tilavuus_korjataan(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_varaston_virheellinen_saldo_korjataan(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestVarastoC(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, 15)
    
    def test_varaston_virheellinen_saldo_korjataan(self):
        self.assertAlmostEqual(self.varasto.saldo, 10)