def celsius_na_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_na_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    print("Witaj w aplikacji do przeliczania temperatury!")
    print("1. Przelicz z Celsiusza na Fahrenheita")
    print("2. Przelicz z Fahrenheita na Celsjusza")
    wybor = input("Wybierz opcje (1 lub 2): ")

    if wybor == '1':
        temp_c = float(input("Podaj temperature w stopniach Celsiusza: "))
        temp_f = celsius_na_fahrenheit(temp_c)
        print(f"{temp_c} stopni Celsiusza to {temp_f} stopni Fahrenheita.")
    elif wybor == '2':
        temp_f = float(input("Podaj temperature w stopniach Fahrenheita: "))
        temp_c = fahrenheit_na_celsius(temp_f)
        print(f"{temp_f} stopni Fahrenheita to {temp_c} stopni Celsiusza.")
    else:
        print("Nieprawidlowy wybor.")


if __name__ == "__main__":
    main()
