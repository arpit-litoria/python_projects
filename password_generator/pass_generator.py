import random 

import string 

  

def generate_password(num_letters, num_symbols, num_numbers): 

    # Define the character pools 

    letters = string.ascii_letters 

    symbols = string.punctuation 

    numbers = string.digits 

     

    # Ensure there are enough characters to choose from 

    all_chars = { 

        'letters': letters, 

        'symbols': symbols, 

        'numbers': numbers 

    } 

     

    # Check if requested numbers are within reasonable bounds 

    if (num_letters > len(letters) or 

        num_symbols > len(symbols) or 

        num_numbers > len(numbers)): 

        raise ValueError("Requested number exceeds available characters in pool.") 

         

    # Combine all characters 

    password_chars = random.sample(letters, num_letters) + random.sample(symbols, num_symbols)  + random.sample(numbers, num_numbers)

     

    # Shuffle the characters to ensure randomness 

    random.shuffle(password_chars) 

     

    # Join characters into a single string 

    password = ''.join(password_chars) 

     

    return password 

  

# Example usage 

num_letters = int(input("Enter the number of letters: ")) 

num_symbols = int(input("Enter the number of symbols: ")) 

num_numbers = int(input("Enter the number of numbers: ")) 

  

try: 

    password = generate_password(num_letters, num_symbols, num_numbers) 

    print(f"Generated password: {password}") 

except ValueError as e: 

    print(e) 