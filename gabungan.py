from abc import ABC, abstractmethod

# Contoh Abstraksi: Kelas Abstrak Produk
class Produk(ABC):
  
    def __init__(self, kode, nama, harga):
        # Contoh Encapsulasi: Atribut privat _
        self._kode = kode
        self._nama = nama
        self._harga = harga

    # Getter untuk mendapatkan informasi produk (Encapsulasi)
    def get_info(self):
        return f"Kode: {self._kode}, Nama: {self._nama}, Harga: Rp{self._harga}"
    # Metode abstrak yang harus diimplementasikan oleh kelas turunan
    @abstractmethod
    def hitung_diskon(self):
        pass

class Elektronik(Produk):
    
    def __init__(self, kode, nama, harga, merk, garansi):
        # Memanggil konstruktor kelas induk
        super().__init__(kode, nama, harga)
        self._merk = merk
        self._garansi = garansi

    # Contoh Polymorphism: Implementasi metode abstrak
    def hitung_diskon(self):
        # Elektronik mendapat diskon 10%
        return self._harga * 0.1

    # Metode tambahan spesifik untuk kelas Elektronik
    def get_info(self):
        # Polymorphism: Override metode dari kelas induk
        info_dasar = super().get_info()
        return f"{info_dasar}, Merk: {self._merk}, Garansi: {self._garansi} tahun"

# Contoh Inheritance: Kelas Makanan yang mewarisi dari Produk
class Makanan(Produk):
    
    def __init__(self, kode, nama, harga, tanggal_kadaluarsa):
        super().__init__(kode, nama, harga)
        self._tanggal_kadaluarsa = tanggal_kadaluarsa

    # Contoh Polymorphism: Implementasi metode abstrak berbeda
    def hitung_diskon(self):
        # Makanan mendapat diskon 5%
        return self._harga * 0.05

    # Metode tambahan spesifik untuk kelas Makanan
    def get_info(self):
        # Polymorphism: Override metode dari kelas induk
        info_dasar = super().get_info()
        return f"{info_dasar}, Kadaluarsa: {self._tanggal_kadaluarsa}"

# Kelas Utama untuk Manajemen Inventaris
class InventarisGudang:
    
    def __init__(self):
        # Contoh Encapsulasi: Atribut privat untuk menyimpan produk
        self._daftar_produk = []

    def tambah_produk(self, produk):
        """Menambahkan produk ke inventaris"""
        self._daftar_produk.append(produk)

    def tampilkan_inventaris(self):
        print("=== INVENTARIS GUDANG ===")
        for produk in self._daftar_produk:
            # Polymorphism: Metode get_info() berbeda untuk setiap jenis produk
            print(produk.get_info())
            print(f"Diskon: Rp{produk.hitung_diskon()}")
            print("---")

# Contoh Penggunaan
def main():
    gudang = InventarisGudang()

    laptop = Elektronik("E001", "Laptop Gaming", 15000000, "ASUS", 2)
    smartphone = Elektronik("E002", "Smartphone", 8000000, "Samsung", 1)
    roti = Makanan("M001", "Roti Tawar", 20000, "2024-12-31")
    keju = Makanan("M002", "Keju Cheddar", 50000, "2024-06-30")

    gudang.tambah_produk(laptop)
    gudang.tambah_produk(smartphone)
    gudang.tambah_produk(roti)
    gudang.tambah_produk(keju)

    gudang.tampilkan_inventaris()

# Menjalankan program utama
if __name__ == "__main__":
    main()