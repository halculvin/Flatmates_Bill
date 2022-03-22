from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill.flat import Bill, Flatmate

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data
        name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)
        name2 = billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)

        the_bill = Bill(amount, period)
        flatmate1 = Flatmate(name1, days_in_house1)
        flatmate2 = Flatmate(name2, days_in_house2)

        return render_template("bill_form_page.html",
                               result=True,
                               billform=billform,
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(the_bill, flatmate1)
                               )


class ResultsPage(MethodView):
    pass



class BillForm(Form):
    amount = StringField("Bill Amount:", default=100)
    period = StringField("Bill Period: ", default="December 2022")
    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Days in the house: ", default="20")

    name2 = StringField("Name: ", default="Mary")
    days_in_house2 = StringField("Days in the house: ", default="12")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
