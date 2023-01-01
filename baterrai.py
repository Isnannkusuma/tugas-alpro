class Baterai():
    def __init__(self, merek, harga):
        self.merk = merek
        self.harga = harga
        self.laku = int(input("Berapa jumlah baterai yang anda beli :"))
    def tampil(self):
        print(f"Baterai Merk {self.merek} dengan harga Rp. {self.harga} terjual {self.laku} biji")

baterai_terjual = Baterai("Versi ALKALINE", 15000)

baterai_terjual.tampil()