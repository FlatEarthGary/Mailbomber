import sys

print("What is the text you want to encrypt?")
text_encrypt = str(input("> "))
print("What shift do you want (chose number please)? (kind of encryption)")
try:
    shift_encrypt = int(input("> "))
except ValueError:
    print("Not correct encryption, please type a number and try again.")
    sys.exit(1)


def encrypt(text, shift):
    lower_case_alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    upper_case_alphabet = lower_case_alphabet.upper()
    cipher = ""
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():  # checks if all the characters in the variable, char, is uppercase, if so it results in True, else it results in False
            # Find index of char in upper_case_alphabet and shift it.
            cipher = cipher + \
                upper_case_alphabet[(
                    upper_case_alphabet.index(char) - shift) % 26]
        else:
            # Find index of char in lower_case_alphabet and shift it.
            cipher = cipher + \
                lower_case_alphabet[(
                    lower_case_alphabet.index(char) - shift) % 26]
    return cipher


def decrypt(text, shift):
    pass


print("You encrypted text is: " + encrypt(text_encrypt, shift_encrypt))
