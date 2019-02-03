# Define classes to represent currencies
class Currency:
    unit_name = "Currency"
    base_rate = 1

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value <= 1:
            return "{} {}".format(self.value,self.unit_name)
        elif self.unit_name[-1] == "y":
            return "{} {}ies".format(self.value,self.unit_name[:-1])
        else:
            return "{} {}s".format(self.value,self.unit_name)

    def conversion(self, result_currency_reference):
        if(type(self) == Pound):
            rate = Pound.rate
        elif (type(self) == Yuan):
            rate = Yuan.rate
        elif (type(self) == Dollar):
            rate = Dollar.rate
        else:
            return "Can't convert. Please enter a valid currency."

        #Conversion
        value_in_currency = self.value * rate
        value_at_reference_rate = value_in_currency / result_currency_reference.rate
        return result_currency_reference(value_at_reference_rate)

class Dollar(Currency):
    unit_name = "Dollar"
    rate = 20

    def __init__(self, value):
        super().__init__(value)

class Yuan(Currency):
    unit_name = "Yuan"
    rate = 8

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return "{} {}".format(self.value,self.unit_name)

class Pound(Currency):
    unit_name = "Pound"
    rate = 15

    def __init__(self, value):
        super().__init__(value)

# Define code for a class Bank
class Bank:

    def __init__(self, name, currency, init_value=0):
        self.name = name
        if isinstance(currency,type(Currency)):
            self.unit = currency
        else:
            if currency == "Dollar":
                self.unit = Dollar
            elif currency == "Yuan":
                self.unit = Yuan
            elif currency == "Pound":
                self.unit = Pound
            else:
                self.unit = Currency
        if self.unit == Dollar:
            self.current_account = Dollar(init_value)
        elif self.unit == Yuan:
            self.current_account = Yuan(init_value)
        elif self.unit == Pound:
            self.current_account = Pound(init_value)
        else:
            self.current_account = Currency(init_value)

    def __str__(self):
        return "{} Bank holds the {} currency and currently holds {} of {}".format(self.name, self.unit.unit_name, self.current_account.value, self.unit.unit_name)

    def deposit(self, currency):
        if isinstance(currency,type(self.current_account)):
            print("{} is an instance of {}".format(currency,type(self.current_account)))
            self.current_account.value += currency.value
            return "successful deposit"
        else:
            return "ERROR: cannot deposit that currency."

bank = Bank("Suzie","Dollar")
print(type(bank.unit))
