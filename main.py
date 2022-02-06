class Bill:
    """
    Object that contains data about a bill
    such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and
    pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bills, flatmate2):
        weight = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        return bills.amount * weight


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates
    such as their names, their due amount and the period
    of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(120, "March 2021")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)

print(john.pays(the_bill, mary))