def polimer_molekul_agirligi_hesapla(monomer_sayisi, monomer_molekul_agirligi):
    return monomer_sayisi * monomer_molekul_agirligi

def main():
    monomer_sayisi = int(input("Lütfen polimerdeki monomer sayısını girin: "))
    monomer_molekul_agirligi = float(input("Lütfen monomerin molekül ağırlığını girin (g/mol): "))

    polimer_molekul_agirligi = polimer_molekul_agirligi_hesapla(monomer_sayisi, monomer_molekul_agirligi)

    print("İletken polimerin molekül ağırlığı: {:.2f} g/mol".format(polimer_molekul_agirligi))

if __name__ == "__main__":
    main()