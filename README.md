# SI 507 Project 1: Banking App
## About the Banking App
This program in SI507_project1.py is a Flask app that uses classes defined in lab3_code.py (by importing lab3_code.py into SI507_project1.py) to create routes that create instances of Bank and instances of four different types of currency (Currency, Dollar, Pound, and Yuan) depending on the route entered.

### The classes defined in lab3_code.py include:
- Currency (which takes one argument, its initial value as an integer)
- Dollar (which is a child of Currency)
- Yuan (which is a child of Currency)
- Pound (which is a child of Currency)
- Bank (which takes three arguments: the name of the bank as a string, the currency as either a string represenging Currency, Dollar, Yuan, or Pound, or a type object representing the former currency types, and an initial amount, defaulting to 0)

### The routes available in the banking app include:
- The home route (/) welcomes the user to the banking application but does not do anything else.
- The route `bank/<bankname>` creates an instance of class Bank with name `<bankname>`, currency type Currency, and initial value 0, and returns the string `"Welcome to <bankname>"`.
- the route `dollar/<amt>` creates an instance of class Dollar with amount `<amt>` and returns the string `"<amt> Dollar"`.
- the route `pound/<amt>` creates an instance of class Pound with amount `<amt>` and returns the string `"<amt> Pound"`.
- the route `yuan/<amt>` creates an instance of class Yuan with amount `<amt>` and returns the string `"<amt> Yuan"`.
- the route `bank/<name>/<currency>/<value>` creates an instance of class Bank with name `<name>`, currency type `<currency>`, and initial value `<value>` and returns the string `"Welcome to the <name> bank! <name> Bank holds the <currency> currency and currently holds <value> of <currency>"`.

### The classes defined in lab3_code.py include:
- Currency (which takes one argument, its initial value as an integer)
- Dollar (which is a child of Currency)
- Yuan (which is a child of Currency)
- Pound (which is a child of Currency)
- Bank (which takes three arguments: the name of the bank as a string, the currency as either a string represenging Currency, Dollar, Yuan, or Pound, or a type object representing the former currency types, and an initial amount, defaulting to 0)

# How to Run the Program
This program was written with Python 3.7.1 and the Flask module using a virtual environment. Requirements to run the program can be found in requirements.txt. To install everything from requirements.txt, download the requirements.txt file, activate your virtual environment, and then enter the following in your shell: `pip install -r requirements.txt`.

In order to run the program, make sure you are in the same directory as all the files, and then enter the following in your shell: `python SI507_project1.py runserver`. The program can then be found running at `localhost:5000` plus the correct route in your browser.
