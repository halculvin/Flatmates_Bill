import webbrowser

from fpdf import FPDF


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
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return bills.amount * weight


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates
    such as their names, their due amount and the period
    of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family="Times", size=12)
        # Insert name and due amount of first flatmate name
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of second flatmate name
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        # Windows computer
        webbrowser.open(self.filename)
        # # Linux or Mac computer
        # webbrowser.open('file://' + os.path.realpath(self.filename))


the_bill = Bill(120, "April 2021")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)

print("John pays: ", john.pays(the_bill, mary))
print("Mary pays: ", mary.pays(the_bill, john))

pdf_report = PdfReport("Report1.pdf")
pdf_report.generate_pdf(john, mary, the_bill)
