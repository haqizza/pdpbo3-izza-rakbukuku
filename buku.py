class Buku():
    def __init__(self, judul, kategori, penulis, genre, tahun_terbit, penerbit, keadaan, path_foto):
        self.judul = judul
        self.kategori = kategori
        self.penulis = penulis
        self.genre = genre
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit
        self.keadaan = keadaan
        self.path_foto = path_foto

    def get_judul(self):
        return self.judul

    def get_penulis(self):
        return self.penulis

    def get_genre(self):
        return self.genre

    def get_tahun_terbit(self):
        return self.tahun_terbit

    def get_penerbit(self):
        return self.penerbit

    def get_path_foto(self):
        return self.path_foto