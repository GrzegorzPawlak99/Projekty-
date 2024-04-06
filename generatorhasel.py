import random
import string


def generuj_haslo(dl):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ''.join(random.choice(znaki) for _ in range(dl))
    return haslo


def main():
    while True:
        dlugosc_hasla = int(input("Podaj długość hasła: "))

        if dlugosc_hasla < 6:
            print("Długość hasła musi być większa lub równa 6.")
            continue

        nowe_haslo = generuj_haslo(dlugosc_hasla)
        print("Wygenerowane hasło:", nowe_haslo)

        ponowna_proba = input("Czy chcesz wygenerować kolejne hasło? (tak/nie): ")
        if ponowna_proba.lower() != "tak":
            break


if __name__ == "__main__":
    main()
