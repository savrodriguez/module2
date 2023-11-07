## Fro Yo ##
import random
from flask import Flask, request, render_template
app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        <input type="submit" value="Submit!"><br/>

        Topping Choices: Brownie, MnMs, Strawberry, Mango, Fudge, Cereal,
        CookieDough, Mango, Cherries, Whip Cream<br/>

        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!"><br/>
    </form>
    """
@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f"You ordered {users_froyo_flavor} flavored Fro-Yo with {users_froyo_toppings}!"


## Favorite Things ##
@app.route('/favorites')
def favorites():
    """Shows a from to collect user's favorites"""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color?<br/>
        <input type="text" name="color"><br/>

        How about your favorite animal?<br/>
        <input type="text" name="animal"><br/>

        What's your favorite city?<br/>
        <input type="text" name="city"><br/>

        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def show_favorites_results():
    users_color = request.args.get('color')
    users_animal = request.args.get('animal')
    users_city = request.args.get('city')

    return f"Wow, I didn't know {users_color} {users_animal} lived in {users_city}!"


## Secret Message ##
@app.route('/secretMessage', methods=['GET','POST'])
def secretMessage():
    if request.method == 'POST':
        users_message = request.form.get('message')
        sorted_message = sort_letters(users_message)
        return f"Here's your secret message: {sorted_message}"
    
    return """
    <form action="/secretMessage" method="POST">
        Enter a message below:
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit"><br/>
    </form>
    """



## Calculator ##
@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    number1 = int(request.args.get('operand1'))
    number2 = int(request.args.get('operand2'))
    operation = request.args.get('operation')

    if operation == "add":
        total = number1 + number2
    elif operation == "subtract":
        total = number1 - number2
    elif operation == "multiply":
        total = number1 * number2
    elif operation == "divide":
        if number2 != 0:
            total = number1 / number2
        else: 
            return "Error: Division by zero"
    else:
        return "Error: Invalid Operation"
    
    return f"You chose to {operation} {number1} and {number2}. Your result is: {total}"


## REFACTOR FRO-YO ##
@app.route('/froyo')
def froyo():
    return render_template('froyo_form.html')

# Define the Fro-Yo order results route
@app.route('/froyo_results')
def froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')

    context = {
        'users_froyo_flavor': users_froyo_flavor,
        'users_froyo_toppings': users_froyo_toppings
    }

    return render_template('froyo_results.html', **context)

## REFACTOR CALCULATOR ##
@app.route('/calculator', methods=['GET'])
def calculator_form():
    return render_template('calculator_form.html')

# Define the Calculator results route for POST requests
@app.route('/calculator_results', methods=['POST'])
def calc_results():
    number1 = int(request.form.get('operand1'))
    number2 = int(request.form.get('operand2'))
    operation = request.form.get('operation')

    if operation == "add":
        total = number1 + number2
    elif operation == "subtract":
        total = number1 - number2
    elif operation == "multiply":
        total = number1 * number2
    elif operation == "divide":
        if number2 != 0:
            total = number1 / number2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid Operation"

    context = {
        'number1': number1,
        'number2': number2,
        'operation': operation,
        'total': total
    }

    return render_template('calculator_results.html', **context)



## Horoscope Personas ##
HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    user_name = request.args.get('users_name')

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign)

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1,99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number,
        'users_name': user_name
    }

    return render_template('horoscope_results.html', **context)




if __name__ == '__main__':
    app.config["ENV"] = 'development'
    app.run(debug=True)