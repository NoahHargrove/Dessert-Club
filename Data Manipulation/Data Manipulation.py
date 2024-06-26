import csv
import random
import pandas as pd
import numpy as np

# Define file paths for the CSV files.
file_path = 'desserts.csv'  # Original data file.
csv_file_path = 'desserts.csv'  # Another reference to the original data file.
csv_file_path_noise = 'desserts_noise.csv'  # File path for the output with added noise.

# Define column headers for the CSV file.
headers = ["dessertName", "cookie", "brownie", "bar", "cake", "parfait", "pie", "cupcakeMuffin", "breakfast", "heavy", "tart", "sweet", "fluffy", "gooey", "dye", "chocolate", "extraChocolate", "fudge", "peanutButter", "whiteChocolate", "butterscotch", "sprinkles", "cinnamon", "brownSugar", "powederSugar", "oreo", "cookieDough", "marshmallow", "mintMocha", "mAndMs", "pretzels", "caramel", "pumpkin", "banana", "strawberry", "blueberry", "cherry", "orange", "lemon", "carrot", "differentVegetable", "diffFruit", "time"]

# Create a new CSV file and write the headers.
with open(csv_file_path_noise, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

# Read the original data from the CSV file.
original_data = pd.read_csv(file_path)

# Remove the 'time' column if it exists in the data.
if 'time' in original_data.columns:
    original_data = original_data.drop(columns='time')

# Define columns by the level of noise to be added.
even_more_noise_cols = ['heavy', 'sweet']
most_noise_cols = ['tart', 'fluffy', 'gooey', 'extra_chocolate']
more_noise_cols = ['brownie', 'bar', 'cake',  'cupcake_muffin'] 
less_noise_cols = ['breakfast', 'dye', 'chocolate', 'fudge', 'peanutButter', 'white_chocolate', 'butterscotch', 'sprinkles', 'cinnamon', 'brown_sugar', 'powder_sugar', 'oreo', 'cookie_dough', 'marshmallow', 'mint_mocha', 'm_and_ms', 'pretzels', 'caramel', 'pumpkin', 'banana', 'strawberry', 'blueberry', 'cherry', 'orange', 'lemon', 'carrot', 'different_vegetable', 'diff_fruit']  
no_noise_cols = ['dessert_name', 'cookie','parfait', 'pie']

# Define noise levels for each category.
even_more_noise_level = 1.25
most_noise_level = .25
more_noise_level = .15 
less_noise_level = .07
number_copies = 50  # Number of times to replicate and add noise to the data.

# Initialize count for tracking iterations.
count = 0

# Loop through the number of copies.
for _ in range(number_copies):
    data = original_data.copy()  # Make a copy of the data for each iteration.
    # Loop through each column in the data.
    for col in original_data:
        # Determine the level of noise based on the column category.
        if col in more_noise_cols:
            noise_level = more_noise_level
        elif col in most_noise_cols:
            noise_level = most_noise_level
        elif col in less_noise_cols:
            noise_level = less_noise_level
        elif col in no_noise_cols:
            noise_level = 0 
        else:
            noise_level = 0.25  # Default noise level for unspecified columns.

        # Generate noise and add it to the column data.
        noise = np.random.normal(loc=0.0, scale=noise_level, size=data[col].shape)
        noisy_data = data[col] + noise
        noisy_data_rounded = np.round(noisy_data)
        # Clip the data to valid values (0 or 1) unless it's the 'dessertName' column.
        if col != 'dessertName':
            noisy_data_clipped = np.clip(noisy_data_rounded, 0, 1)
            data[col] = noisy_data_clipped
        else:
            data[col] = noisy_data_rounded
    
    # Append the modified data to the noise-added CSV file.
    data.to_csv(csv_file_path_noise, mode='a', header=False, index=False)

# Print the count (although it is not incremented within the loop and will print 0).
print(count)
