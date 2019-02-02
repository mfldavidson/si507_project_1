from flask import Flask
import lab3_code as classes

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def welcome(): # Route function names can be anything unique
    return '<h1>Welcome to the banking application!</h1>' # Route functions can return plain old text, or text in correctly formatted HTML (or the return values of many special functions we haven't looked at yet)

# Something else to note is that the functions don't get INVOKED the way you may be used to. Running the application and *going to a URL that matches the path in the @app.route() business IS what runs that function!

@app.route('/user/<yourname>')
def hello_name(yourname): # Note how the word in < > carats / angle-brackets is the SAME as the input to the function - that means the URL is what sends the input along
    return 'Hello {}'.format(yourname)

@app.route('/showvalues/<name>/<greeting>')
def showvalues(name, greeting): # Check this out -- what's going on here? A useful pattern to think about.
    return "{}, {}!".format(greeting, name)



if __name__ == '__main__':
    app.run()
