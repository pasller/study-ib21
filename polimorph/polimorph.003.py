import self


class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def set_year(self, year):
        self.year = year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def format(self):
        return "{1}.{0}.{2}".format(self.day, self.month, self.year)

class EuropeanDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def set_year(self, year):
        self.year = year

    def get_month(self):
        return self.month

    def get_day(self):
        return day

    def get_year(self):
        return self.year

    def format(self):
        return "{0}.{1}.{2}".format(self.day, self.month, self.year)













american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())