import datetime
import argparse
import requests

parser = argparse.ArgumentParser(
    description='Sprawdzanie kursu waluty z ostatnich 5 dni z NBP',
    epilog='Przykład użycia:\n python3 NBPAPI.py currencycode',
    formatter_class=argparse.RawDescriptionHelpFormatter)


parser.add_argument('currency', type=str, help='Waluta kod')

args = parser.parse_args()

startDate = datetime.date.today() - datetime.timedelta(days=5)
endDate = datetime.date.today()
# url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency}"
url2 = f"https://api.nbp.pl/api/exchangerates/rates/A/{args.currency}/{startDate}/{endDate}"

# response = requests.get(url)
response2 = requests.get(url2)


if response2.status_code == 200:
    data = response2.json()
    poprzednikwota = 0
    dzieńpoprz = ""
    czyPierwszy = True

    for key in data:
        if key == 'currency':
            print(f"\nWaluta: {data[key]}")
        elif key == 'rates':
            dane = data[key]
            for tabela in dane:
                aktualna_data = tabela['effectiveDate']
                aktualny_kurs = tabela['mid']

                print(f"\nData na którą czytamy stan walut: {aktualna_data}")
                print(f"Stan waluty (średnia wartość): {aktualny_kurs}")

                if czyPierwszy:
                    # Pierwszy dzień — nie ma jeszcze z czym porównać
                    czyPierwszy = False
                else:
                    różnica = round(float(aktualny_kurs) - float(poprzednikwota), 4)
                    print(f"Różnica między {aktualna_data} a {dzieńpoprz} to: {różnica}")

                # Zapisz bieżące wartości jako "poprzednie" na następną iterację
                poprzednikwota = aktualny_kurs
                dzieńpoprz = aktualna_data

else:
    print(f"Błąd: otrzymano status {response2.status_code}")
