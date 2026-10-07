class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def hitung_total(self, jumlah_beli):
        return self.harga * jumlah_beli

    def hitung_diskon(self, total):
        if total > 5000:
            return total * 5 / 100
        return 0


total_semua = 0

jumlah_produk = int(input("Masukkan jumlah produk = "))

for i in range(jumlah_produk):
    print("\nProduk ke-", i + 1)

    nama = input("Nama produk = ")
    harga = int(input("Harga produk = Rp"))
    jumlah_beli = int(input("Jumlah beli = "))

    produk = Produk(nama, harga)

    total_produk = produk.hitung_total(jumlah_beli)
    total_semua += total_produk

    print("Total", nama, "= Rp.", int(total_produk))


diskon = produk.hitung_diskon(total_semua)
total_bayar = total_semua - diskon

print("\n=== HASIL PEMBELIAN ===")
print("Total Pembelian : Rp.", int(total_semua))
print("Diskon 5%       : Rp.", int(diskon))
print("Total Bayar     : Rp.", int(total_bayar))