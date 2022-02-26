# Türkçe Karakterleri Eng Dönüştürme
def engDonustur(veri):
    Tr2Eng = str.maketrans("çğıöşüÜÖÇİĞŞ", "cgiosuUOCIGS")
    veri_eng = veri.translate(Tr2Eng)
    return veri_eng