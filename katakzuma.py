class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        print("Warna peluru telah diganti menjadi:", self.warna_peluru)

    def tembak(self):
        if self.is_active:
            self.skor += 50
            print("Skor bertambah 50.")

    def info_status(self):
        print("Warna peluru:", self.warna_peluru)
        print("Skor:", self.skor)
        print("Status aktif:", self.is_active)

katak_zuma = KatakZuma("Hijau")
katak_zuma.info_status()
katak_zuma.ganti_warna("biru")
katak_zuma.tembak()
katak_zuma.info_status()