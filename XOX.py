print("""
                ********************************************
                        XOX Oyununa Hoş Geldiniz. V0.1
                                YAZAR: S.K
                ********************************************
""")

oyunTahtasi = ["_" for x in range(10)]

def ekrandaGoster():
    print(""" ► OYUN TAHTASI 
    """)
    print("" + oyunTahtasi[1] + " " + "║" + " " + "" + oyunTahtasi[2] + " " + "║" + " " + "" + oyunTahtasi[3])
    print("▬▬▬▬▬▬▬▬▬")
    print("" + oyunTahtasi[4] + " " + "║" + " " + "" + oyunTahtasi[5] + " " + "║" + " " + "" + oyunTahtasi[6])
    print("▬▬▬▬▬▬▬▬▬")
    print("" + oyunTahtasi[7] + " " + "║" + " " + "" + oyunTahtasi[8] + " " + "║" + " " + "" + oyunTahtasi[9])

def harfKoy(harf,konum):
    oyunTahtasi[konum] = harf

def alanBosMu(konum):
    return oyunTahtasi[konum] == "_"

def tahtaDolu():
    if oyunTahtasi.count("_") > 1:
        return False
    else:
        return True

def kazanan(oyunTahtasi,harf):
    return (oyunTahtasi[1] == harf and oyunTahtasi[2] == harf and oyunTahtasi[3] == harf) or (oyunTahtasi[4] == harf and oyunTahtasi[5] == harf and oyunTahtasi[6] == harf) or (oyunTahtasi[7] == harf and oyunTahtasi[8] == harf and oyunTahtasi[9] == harf) or (oyunTahtasi[1] == harf and oyunTahtasi[4] == harf and oyunTahtasi[7] == harf) or (oyunTahtasi[2] == harf and oyunTahtasi[5] == harf and oyunTahtasi[8] == harf) or (oyunTahtasi[3] == harf and oyunTahtasi[6] == harf and oyunTahtasi[9] == harf) or (oyunTahtasi[1] == harf and oyunTahtasi[5] == harf and oyunTahtasi[9] == harf) or (oyunTahtasi[3] == harf and oyunTahtasi[5] == harf and oyunTahtasi[7] == harf)

def oyuncuHareketi():
    konum = int(input("1-9 arasında bir konum giriniz: "))
    if alanBosMu(konum):
        harfKoy("X",konum)
        if kazanan(oyunTahtasi,"X"):
            ekrandaGoster()
            print("Tebrikler kazandınız.")
            exit()
        ekrandaGoster()
    else:
        print("Girdiğiniz konum dolu. Tekrar seçiniz.")
        oyuncuHareketi()

def bilgisayarHareketi():
    import random
    musait_konumlar = [konum for konum, harf in enumerate(oyunTahtasi) if harf == "_" and konum != 0]
    hareket = 0

    for harf in ["O","X"]:
        for i in musait_konumlar:
            kopya_tahta = oyunTahtasi[:]
            kopya_tahta[i] = harf
            if kazanan(kopya_tahta,harf):
                hareket = i
                return hareket


    koseler = []

    for i in musait_konumlar:
        if i in [1,3,7,9]:
            koseler.append(i)
    if len(koseler) > 0:
        hareket = random.choice(koseler)
        return hareket

    if 5 in musait_konumlar:
        hareket = 5
        return hareket

    icerisi = []

    for i in musait_konumlar:
        if i in [2,4,6,8]:
            icerisi.append(i)
    if len(icerisi) > 0:
        hareket = random.choice(icerisi)
        return hareket

def oyun():


    ekrandaGoster()

while not tahtaDolu():
    oyuncuHareketi()
    if tahtaDolu():
        ekrandaGoster()
        print("Oyun bitti kazanan yok!")
        exit()

    print("--------------------------------")

    bilgisayar_hareket = bilgisayarHareketi()
    harfKoy("O",bilgisayar_hareket)
    if kazanan(oyunTahtasi,"O"):
        ekrandaGoster()
        print("Bilgisayar kazandı.")
        exit()

    ekrandaGoster()
    if tahtaDolu():
        ekrandaGoster()
        print("Oyun bitti kazanan yok!")
        exit()

    print("--------------------------------")

oyun()