import string
import random

password_criteria = {}

password_criteria['length'] = int(input("password Length: "))
password_criteria['Lowercase'] = input("would you like Lowercase letters, Y or N: ")
password_criteria['Uppercase'] = input("would you like Uppercase letters, Y or N: ")
password_criteria['Numbers'] = input("Would you like Numbers in your password, Y or N: ")
password_criteria['Randomized_symbols'] = input("Would you like Randomized symbols in your password, Y or N: ")

# print(password_criteria)

new_password = ""

while password_criteria['length'] > 0:
    password_criteria['length'] = password_criteria['length'] - 1

    password_list = []

    if ('y' or 'Y') in password_criteria['Lowercase']:
        random_char = random.choice(string.ascii_lowercase)
        password_list.append(random_char)

    if ('y' or 'Y') in password_criteria['Uppercase']:
        random_char_CAPS = random.choice(string.ascii_uppercase)
        password_list.append(random_char_CAPS)

    if ('y' or 'Y') in password_criteria['Numbers']:
        random_int = random.choice(string.digits)
        password_list.append(random_int)

    if ('y' or 'Y') in password_criteria['Randomized_symbols']:
        random_symbols = random.choice(string.punctuation)
        password_list.append(random_symbols)

#    print(password_list)

    new_char = random.choice(password_list)
    new_password = new_password + new_char
    password_list.clear()

#    print(new_password)

print(f"Your new password is - {new_password}")