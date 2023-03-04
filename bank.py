import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.conversion_rates = {}

        url = 'https://bank.gov.ua/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        usd_div = soup.find('div', {'class': 'value'})
        usd = usd_div.text.strip()

        self.conversion_rates['USD'] = float(usd)

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.conversion_rates[from_currency]

        amount = round(amount * self.conversion_rates[to_currency], 2)
        return amount

converter = CurrencyConverter()
amount = float(input('Enter the amount of currency: '))

converted_amount = converter.convert(from_currency, to_currency, amount)

print(f'{amount} {from_currency} = {converted_amount} {to_currency}')