# Project #4 - Passwords
# Write a password generator. Be creative with how you generate passwords.
# - The passwords should be random, generating a new password every time the user asks for a new password.
# - Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list. Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# - Use function, not only your main

import random
import string


def get_user_choice():
    user_input = input('User Choice : ')
    return user_input


def psw_len():
    user_len = input('password length? ')
    return user_len


words = ['Strong', 'Weak', 'Very', 'little',
         'Big', 'Small', 'word', 'something']


waiting_for_input = True

while waiting_for_input:
    print('Please choose:')
    print('1: For weak password')
    print('2: For strong password')
    print('3: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        psw = random.choice(words) + random.choice(words)
        print("Your password is: ", psw)
    elif user_choice == '2':
        strong_ch = int(psw_len())
        if strong_ch > 8:
            characters = string.ascii_letters + string.punctuation + string.digits
            password = ''.join(random.choice(characters)
                               for i in range(strong_ch))
            print("Your password: ", password)
        else:
            print("Strong Password's length must be greater than 8 characters ")

    elif user_choice == "3":
        break

