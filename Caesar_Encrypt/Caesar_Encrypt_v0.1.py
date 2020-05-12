import sys


class MainEncryption(object):

    def __init__(self):

        print("What text do you want to encrypt?")
        self.encryptionText = str(input("> "))
        print("What shift do you want?")
        try:
            self.encryptionShift = int(input("Number: "))
        except ValueError:
            print("That is not a number, try again!")
            sys.exit(1)

    def encryption(self):

        self.lowerCaseAlphabet = "abcdefghijklmnopqrstuvwxyzåäö"
        self.upperCaseAlphabet = self.lowerCaseAlphabet.upper()
        self.cipher = ""

        for self.character in self.encryptionText:
            if self.character == " ":
                self.cipher += self.character
            elif self.character.isupper():
                self.cipher += self.upperCaseAlphabet[(
                    self.upperCaseAlphabet.index(self.character) - self.encryptionShift) % 29]
            elif self.character.islower():
                self.cipher += self.lowerCaseAlphabet[(
                    self.lowerCaseAlphabet.index(self.character) - self.encryptionShift) % 29]
            else:
                print("ERROR.")
                sys.exit(1)
        return self.cipher


Run = MainEncryption()
print("Your encrypted text is: " + Run.encryption())
