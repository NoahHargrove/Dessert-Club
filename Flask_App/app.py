from flask import Flask, render_template, request, session, redirect, url_for
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load and prepare the dataset
# Load the dataset from a CSV file.
data = pd.read_csv('desserts.csv')
# Strip any leading or trailing whitespace characters from the column names.
data.columns = data.columns.str.strip()

# Separate the target variable and feature variables
# Target variable (the dessert name)
y = data["dessertName"]
# Feature variables (attributes of the desserts)
X = data[["cookie", "brownie", "bar", "cake", "parfait", "pie", "cupcakeMuffin", "breakfast", "heavy", "tart", "sweet", "fluffy", "gooey", "dye", "chocolate", "extraChocolate", "fudge", "peanutButter", "whiteChocolate", "butterscotch", "sprinkles", "cinnamon", "brownSugar", "powederSugar", "oreo", "cookieDough", "marshmallow", "mintMocha", "mAndMs", "pretzels", "caramel", "pumpkin", "banana", "strawberry", "blueberry", "cherry", "orange", "lemon", "carrot", "differentVegetable", "diffFruit"]]

# Split the dataset into training and test sets
# The data is split with 30% reserved for testing and the rest for training.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Initialize and train the RandomForestClassifier
model = RandomForestClassifier(random_state=0)
# Fit the model on the training data.
model.fit(X_train, y_train)

# Initialize the Flask application
app = Flask(__name__)
# Set a secret key for session management
app.secret_key = 'Hoan3'

#A dictionary of questions to ask users about dessert characteristics
questions = {
    "cookie": "Is it a cookie?",
    "brownie": "Is it a brownie?",
    "bar": "Is it a bar?",
    "cake": "Is it cake/cakey?",
    "parfait": "Is it a parfait?",
    "pie": "Is it a pie?",
    "cupcakeMuffin": "Is it a cupcake/muffin?",
    "breakfast": "Is it eaten at breakfast?",
    "heavy": "Is it a heavy dessert?",
    "tart": "Is it tart?",
    "sweet": "Is it very sweet?",
    "fluffy": "Is it fluffy?",
    "gooey": "Is it gooey?",
    "dye": "Contains food dye?",
    "chocolate": "Contains chocolate?",
    "extraChocolate": "Contains extra chocolate?",
    "fudge": "Contains fudge?",
    "peanutButter": "Contains peanut butter?",
    "whiteChocolate": "Contains white chocolate?",
    "butterscotch": "Contains butterscotch?",
    "sprinkles": "Contains sprinkles?",
    "cinnamon": "Contains cinnamon?",
    "brownSugar": "Contains brown sugar?",
    "powederSugar": "Contains powdered sugar?",
    "oreo": "Contains Oreo?",
    "cookieDough": "Contains cookie dough?",
    "marshmallow": "Contains marshmallow?",
    "mintMocha": "Contains mint/mocha?",
    "mAndMs": "Contains M&Ms?",
    "pretzels": "Contains pretzels?",
    "caramel": "Contains caramel?",
    "pumpkin": "Contains pumpkin?",
    "banana": "Contains banana?",
    "strawberry": "Contains strawberry?",
    "blueberry": "Contains blueberry?",
    "cherry": "Contains cherry?",
    "orange": "Contains orange?",
    "lemon": "Contains lemon?",
    "carrot": "Contains carrot?",
    "differentVegetable": "Contains different vegetable?",
    "diffFruit": "Contains different fruit?"
}

#A dictionary mapping numerical indices to dessert names for the output of the model
dessert_dict = {
    0: "Amish Cookies",
    1: "Amish Pastries",
    2: "Angel Food Cake",
    3: "Apple Cinnamon Coffee Cake",
    4: "Apple Danish",
    5: "Apple Turnover",
    6: "Assorted Donut Holes",
    7: "Assorted Scones",
    8: "Banana Bread",
    9: "Banana Cake and Cream Cheese Icing",
    10: "Banana Chocolate Chip Cookies",
    11: "Banana Cream Pie Parfait",
    12: "Blueberry Buckle",
    13: "Blueberry Crumb Muffins",
    14: "Boston Cream Cupcake",
    15: "Brown Sugar Cookie",
    16: "Buckeye Bar",
    17: "Buckeye Parfait",
    18: "Cake Batter Cupcakes",
    19: "Caramel Pretzel Brownie",
    20: "Caramel Apple Blondies",
    21: "Carmelita's",
    22: "Carrot Cake Bar",
    23: "Carrot Cupcake",
    24: "Chai Tea Snickerdoodle",
    25: "Cheesecake Swirled Brownie",
    26: "Cherry Berry Crisp",
    27: "Cherry Cheesecake Brownies",
    28: "Cherry Coke Cupcake",
    29: "Cherry Nanaimo Bar",
    30: "Cherry Turnovers",
    31: "Chocolate Chip Miso Blondie",
    32: "Chocolate Chip Banana Espresso Muffin",
    33: "Chocolate Chip Blondies",
    34: "Chocolate Chip Brookie",
    35: "Chocolate Chip Cookie",
    36: "Chocolate Chip Cookie Sandwich",
    37: "Chocolate Iced Bavarian Donuts",
    38: "Chocolate M&M Cookie",
    39: "Chocolate Mint Bar",
    40: "Chocolate Molasses Cookie",
    41: "Cinnamon Roll Cookie",
    42: "Cinnamon Rolls",
    43: "Cinnamon Sugar Cake Donuts",
    44: "Cookie Dough Cheesecake Bar",
    45: "Cookie Dough Cupcake",
    46: "Cookies and Cream Oreo Blondie",
    47: "Cowboy Cookie",
    48: "Cracker Toffee",
    49: "Cranberry Orange Muffins",
    50: "Donut Holes",
    51: "Double Chocolate Bundt Cake",
    52: "Double Chocolate Chip Cookie",
    53: "Double Chocolate Cookie",
    54: "Double Chocolate Muffins",
    55: "Five Layer Bar",
    56: "Frosted Flake Treat",
    57: "Fruity Pebbles Krispy Treat",
    58: "Fudge Iced Brownies",
    59: "Fudge Lava Cake",
    60: "Fudge Oat Bar",
    61: "Hot Apple Crisp",
    62: "Hot Fudge Brownie",
    63: "Iced Cream Stick",
    64: "Jam Oat Bar",
    65: "Kenyon Brownie",
    66: "Kenyon Cookie",
    67: "Lemon Bar",
    68: "Lemon Danish",
    69: "Lemon Poppy Muffins",
    70: "Luscious Lemon Parfait",
    71: "M&M Blondie",
    72: "M&M Brookie",
    73: "M&M Cookie",
    74: "M&M Cookie Sandwich",
    75: "M&M Sugar Cookies",
    76: "Mini Apple Pastries",
    77: "Mini Blueberry Pastries",
    78: "Mini Cherry Pastries",
    79: "Mini Key Lime Pies",
    80: "Mini Pumpkin Spiced Strussel Cheesecake",
    81: "Mint Chip Sugar Cookie",
    82: "Mocha Chip Brownie",
    83: "Molasses Cookie",
    84: "Monster Cookies",
    85: "Morning Glory Muffins",
    86: "N.Y. Crumble Cake",
    87: "NY Cheesecake Bar",
    88: "NY Strawberry Cheesecake Bar",
    89: "Oatmeal Raisin Sandwich",
    90: "Ooey Gooey Cake",
    91: "Orange Brownie",
    92: "Orange Citrus Bar",
    93: "Orange Vanilla Cookie",
    94: "Oreo Brookie",
    95: "Oreo Cheesecake Bars",
    96: "Oreo Sugar Cookie",
    97: "Oatmeal Raisin Five Spice Cookie",
    98: "Powder Sugar Brownie",
    99: "Powder Sugar Donut Holes",
    100: "Pretzel Chocolate Chip Cookies",
    101: "Pumpkin Bar w Cream Cheese Icing",
    102: "Pumpkin Bread",
    103: "Pumpkin Bundt Cake",
    104: "Pumpkin Chai Latte Blondie",
    105: "Pumpkin Chocolate Chip Cookies",
    106: "Rainbow Sugar Cookie",
    107: "Raspberry Danish",
    108: "Raspberry Swirl Blondie",
    109: "Raspberry White Chocolate Cupcake",
    110: "Red Velvet Bundt Cake",
    111: "Red Velvet Cake Bars",
    112: "Rice Krispy",
    113: "S'mores Bar",
    114: "S'mores Cupcakes",
    115: "S'mores Parfait",
    116: "Salted Caramel Brownie Parfait",
    117: "Samoa Blondie",
    118: "Snickerdoodle Cheesecake Bar",
    119: "Snickerdoodle Cookie",
    120: "Soft Ginger Snap Cookies",
    121: "Sopapilla Cheesecake Bar",
    122: "Sour Cream Cookies",
    123: "Texas Sheet Cake",
    124: "Tiramisu Cupcake",
    125: "Toll House Mini Pies",
    126: "Triple Chocolate Chip Cookie",
    127: "Triple Chocolate Cupcake",
    128: "Triple Chocolate Oreo Parfait",
    129: "Twix Rice Krispy Treat",
    130: "White Chocolate Lemon Cookie",
    131: "Zucchini Bread"
}

# Define a route for the root URL which serves a welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')  # Serve the welcome.html template

# Define a route for starting the quiz, which initializes session data
@app.route('/start', methods=['POST'])
def start():
    # Initialize session data with a list of None values for user responses
    session['inputs'] = [None] * len(questions)
    session['question_index'] = 0  # Start with the first question
    return redirect(url_for('ask_question'))  # Redirect to the question asking route

# Define a route to handle displaying and processing questions
@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    # Retrieve current question index and list of questions from the session
    question_index = session.get('question_index', 0)
    questions_list = list(questions.items())

    # Handle POST request when a user submits an answer
    if request.method == 'POST':
        user_input = int(request.form['response'])  # Get user response
        inputs = session.get('inputs', [None] * len(questions))  # Get current inputs

        # Update inputs and question index in session
        if question_index < len(inputs):
            inputs[question_index] = user_input
            session['inputs'] = inputs
            session['question_index'] += 1

        # If there are more questions, continue to the next; otherwise, go to results
        if question_index + 1 < len(questions):
            feature, question = questions_list[question_index + 1]
            return render_template('question.html', question=question)
        else:
            return redirect(url_for('result'))
    # Handle GET request to show the current question
    else:
        if question_index < len(questions):
            feature, question = questions_list[question_index]
            return render_template('question.html', question=question)
        else:
            return redirect(url_for('result'))

# Define a route to display the final result after all questions have been answered
@app.route('/result')
def result():
    # Get the user inputs from the session
    inputs = session.get('inputs', [None] * len(questions))
    inputs_array = np.array([inputs])  # Convert inputs to a NumPy array for model prediction
    guess_index = model.predict(inputs_array).item()  # Predict the dessert index
    guess = dessert_dict[guess_index]  # Get the dessert name from the dictionary
    return render_template('result.html', guess=guess)  # Serve the result page with the guess

# Run the Flask application only if the script is run directly (not imported)
if __name__ == '__main__':
    app.run(debug=True)  # Run with debugging enabled
