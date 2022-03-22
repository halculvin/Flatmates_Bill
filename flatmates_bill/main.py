from flat import Bill, Flatmate
from report import PdfReport


# Get command line inputs
bill_amount = float(input("Hey User, enter the bill amount: "))
bill_period = input("What is the bill period? Eg. December 2022: ")
first_mate = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {first_mate} stay in the house during the bill period? "))
second_mate = input("What is the name of the other flat mate? ")
days_in_house2 = int(input(f"How many days did {second_mate} stay in the house during the bill period? "))

the_bill = Bill(bill_amount, bill_period)
mate1 = Flatmate(first_mate, days_in_house1)
mate2 = Flatmate(second_mate, days_in_house2)

print(f"{mate1.name} pays: ", mate1.pays(the_bill, mate2))
print(f"{mate2.name} pays: ", mate2.pays(the_bill, mate1))

# Create the pdf report
pdf_report = PdfReport(f"{the_bill.period}.pdf")
pdf_report.generate_pdf(mate1, mate2, the_bill)
