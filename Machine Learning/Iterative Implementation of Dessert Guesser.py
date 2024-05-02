import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset from a CSV file and strip any whitespace from column names.
test = pd.read_csv('desserts.csv')
test.columns = test.columns.str.strip()

# Separate the target variable (dessert names) and the feature variables.
y = test["dessertName"]
X = test[[ "cookie", "brownie", "bar", "cake", "parfait", "pie", "cupcakeMuffin", "breakfast", "heavy", "tart", "sweet", "fluffy", "gooey", "dye", "chocolate", "extraChocolate", "fudge", "peanutButter", "whiteChocolate", "butterscotch", "sprinkles", "cinnamon", "brownSugar", "powederSugar", "oreo", "cookieDough", "marshmallow", "mintMocha", "mAndMs", "pretzels", "caramel", "pumpkin", "banana", "strawberry", "blueberry", "cherry", "orange", "lemon", "carrot", "differentVegetable", "diffFruit"]]

# Split the dataset into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Initialize and train a RandomForestClassifier.
model = RandomForestClassifier(random_state=0)
model.fit(X_train, y_train)

# Dictionary mapping each feature to a question, used in the user interaction for predictions.
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
# Valid ranges for binary feature answers, ensuring user input is either 0 or 1.
valid_ranges = {
    "cookie": range(0, 2),
    "brownie": range(0, 2),
    "bar": range(0, 2),
    "cake": range(0, 2),
    "parfait": range(0, 2),
    "pie": range(0, 2),
    "cupcakeMuffin": range(0, 2),
    "breakfast": range(0, 2),
    "heavy": range(0, 2),
    "tart": range(0, 2),
    "sweet": range(0, 2),
    "fluffy": range(0, 2),
    "gooey": range(0, 2),
    "dye": range(0, 2),
    "chocolate": range(0, 2),
    "extraChocolate": range(0, 2),
    "fudge": range(0, 2),
    "peanutButter": range(0, 2),
    "whiteChocolate": range(0, 2),
    "butterscotch": range(0, 2),
    "sprinkles": range(0, 2),
    "cinnamon": range(0, 2),
    "brownSugar": range(0, 2),
    "powederSugar": range(0, 2),
    "oreo": range(0, 2),
    "cookieDough": range(0, 2),
    "marshmallow": range(0, 2),
    "mintMocha": range(0, 2),
    "mAndMs": range(0, 2),
    "pretzels": range(0, 2),
    "caramel": range(0, 2),
    "pumpkin": range(0, 2),
    "banana": range(0, 2),
    "strawberry": range(0, 2),
    "blueberry": range(0, 2),
    "cherry": range(0, 2),
    "orange": range(0, 2),
    "lemon": range(0, 2),
    "carrot": range(0, 2),
    "differentVegetable": range(0, 2),
    "diffFruit": range(0, 2)
}
# Dictionary translating dessert indices into human-readable names.
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


# Function to predict the type of dessert based on user input.
def predict_dessert(model):
    # Initialize an array for user inputs.
    inputs = np.full((1, len(questions)), np.nan)
    threshold_confidence = 0.85  # Confidence threshold for making a prediction.

    best_overall_guess = None
    highest_overall_confidence = 0  

    # Iterate through each question and get user responses.
    for i, (feature, question) in enumerate(questions.items()):
        while True:
            try:
                answer = int(input(f"{question} "))
                # Validate and store the answer if it's in the valid range.
                if answer in valid_ranges[feature]:
                    inputs[0, i] = answer
                    break
                else:
                    print(f"Please enter a valid option: {valid_ranges[feature]}", flush=True)
            except ValueError:
                print("Invalid input. Please enter an integer.", flush=True)

        # Predict the dessert type based on current inputs.
        if not np.isnan(inputs).all():
            probas = model.predict_proba(inputs)
            max_proba = np.max(probas)
            current_guess = model.classes_[np.argmax(probas)]

            # Update the best guess and its confidence if it's the highest so far.
            if max_proba > highest_overall_confidence:
                highest_overall_confidence = max_proba
                best_overall_guess = current_guess

            # If the confidence meets the threshold, make a final prediction.
            if max_proba >= threshold_confidence:
                print(f"\nConfident guess based on the characteristics provided: {dessert_dict[current_guess]}", flush=True)
                return
            else:
                print(f"Current confidence: {max_proba:.2f}. Continuing...", flush=True)

    # If no confident prediction was made, display the best guess.
    if best_overall_guess is not None:
        print(f"\nBest overall guess (highest confidence reached: {highest_overall_confidence:.2f}): {dessert_dict[best_overall_guess]}", flush=True)
    else:
        print("\nUnable to make a confident guess.")

# Call the prediction function with the trained model.
predict_dessert(model)
