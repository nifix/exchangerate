import urllib.request
import json

class ExchangeRate:

    def __init__(self, dest, date):

        self.dateOf = date
        self.rateTo = dest
        self.rate = 0
        self.data = ""
        self.url = "https://api.exchangeratesapi.io/"

        self.get_json()

    def get_json(self):

        full_url = "{}{}".format(self.url,self.dateOf)
        response = urllib.request.urlopen(full_url)
        self.data = json.loads(response.read())
        self.parse_json()

    def parse_json(self):

        self.rate = self.data['rates'][self.rateTo]
        if (self.dateOf != self.data['date']):
            self.dateOf = self.data['date'];
        print("Taux au {} (1 EUR = {} {})".format(self.dateOf, self.rate, self.rateTo))

if __name__ == '__main__':
    ex_rate = ExchangeRate("CAD", "2018-06-12")
