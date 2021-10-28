from time import sleep

class StatisticalAnalysis:

    def __init__(self, stats):
        print("can this analysis BE any slower")
        sleep(10)
        self._stats = stats

    def get_result(self):
        return self._stats

class DataReconfiguration:

    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def reconfigure(self):
        self._data = [5, 4, 3, 2, 1]

    def data(self):
        return self._data

class Product:

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

class Campaign:

    def __init__(self, name: str, product: Product):
        self._product = product

    @property
    def product(self):
        return self._product

    @property
    def name(self):
        return self._name

class Advertisement:

    def __init__(self, name: str, campaign: Campaign):
        self._campaign = campaign

    @property
    def campaign(self):
        return self._campaign

    @property
    def name(self):
        return self._name
class Copywriting:

    def __init__(self, name: str, advertisement: Advertisement):
        self._advertisement = advertisement

    @property
    def advertisement(self):
        return self._advertisement

    @property
    def name(self):
        return self._name

    def write(self) -> str:
        campaign = self.advertisement.campaign
        product = campaign.product

        text = "{p} {c} {a} {c}"
        text.format(
            product.name,
            campaign.name,
            self.advertisement.name,
            self.name
        )

        return text