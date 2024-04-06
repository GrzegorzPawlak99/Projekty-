# Funkcja do obliczania calkowitej kalorycznosci posilku na podstawie podanych wartosci
def oblicz_kalorie(bialko, weglowodany, tluszcze):
    # Wartosci kaloryczne w gramach dla bialka, weglowodanow i tluszczu
    kcal_na_gram_bialka = 4
    kcal_na_gram_weglowodanow = 4
    kcal_na_gram_tluszczy = 9

    # Obliczanie calkowitej kalorycznosci
    kalorie = (bialko * kcal_na_gram_bialka) + (weglowodany * kcal_na_gram_weglowodanow) + (tluszcze * kcal_na_gram_tluszczy)

    return kalorie


# Funkcja do pobierania danych od uzytkownika i obliczania kalorii
def main():
    print("Witaj w kalkulatorze kalorii!")
    bialko = float(input("Podaj ilosc bialka (w gramach): "))
    weglowodany = float(input("Podaj ilosc weglowodanow (w gramach): "))
    tluszcze = float(input("Podaj ilosc tluszczu (w gramach): "))

    kalorie = oblicz_kalorie(bialko, weglowodany, tluszcze)

    print("Calkowita kalorycznosc posilku wynosi:", kalorie, "kcal")


if __name__ == "__main__":
    main()
