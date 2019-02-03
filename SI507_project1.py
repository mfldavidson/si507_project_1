from flask import Flask
import lab3_code as classes

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')
def welcome():
    return '<h1>Welcome to the banking application!</h1>'

@app.route('/bank/<bankname>')
def createBankDefault(bankname):
    bank = classes.Bank(bankname, classes.Currency)
    return '<h1>Welcome to {}</h1>'.format(bank.name)

@app.route('/bank/<bankname>/<specific_currency>')
def createBankSpecified(bankname, specific_currency):
    bank = classes.Bank(bankname, specific_currency)
    return '<h1>Welcome to {}</h1>'.format(bank.name)

@app.route('/dollar/<amt>')
def showDollar(amt):
    dollar = classes.Dollar(int(amt))
    return "<h1>{} Dollar</h1>".format(dollar.value)



if __name__ == '__main__':
    app.run()
