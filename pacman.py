class PacMan:
    def __init__(self, warna_awal):
        self.warna = warna_awal
        self.skor = 0
        self.is_hidup = True

    def makan_pelet(self):
        if self.is_hidup:
            self.skor += 10
            print("Pac-Man memakan pelet. Skor bertambah 10.")

    def makan_hantu(self, warna_baru):
        if self.is_hidup:
            self.warna = warna_baru
            print("Pac-Man memakan hantu!")
            print("Warna Pac-Man berubah menjadi:", self.warna)

    def info_status(self):
        print("Warna Pac-Man:", self.warna)
        print("Skor:", self.skor)
        print("Status hidup:", self.is_hidup)


pacman = PacMan("Kuning")
pacman.info_status()
pacman.makan_pelet()
pacman.makan_pelet()
pacman.makan_hantu("Biru")
pacman.info_status()