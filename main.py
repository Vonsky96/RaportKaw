from report import generuj_raport
import os

def main():
    print("=" * 50)
    print("        RAPORT KAW")
    print("=" * 50)

    plik = input("Podaj nazwę pliku (.xls): ").strip()

    if not os.path.exists(plik):
        print("\n❌ Nie znaleziono pliku.")
        return

    try:
        generuj_raport(plik)
        print("\n✅ Raport został wygenerowany.")
        print("Plik: Raport_Kawy.xlsx")
    except Exception as e:
        print("\n❌ Wystąpił błąd:")
        print(e)

if __name__ == "__main__":
    main()
