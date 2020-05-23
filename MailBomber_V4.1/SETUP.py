import MailBomber
import os
import time


print("\x1b[35m" + "{+}{-} Email Bomber V1.0 {-}{+}")
print("\nDo you want to automatically install the requirements? (Y/N) This is highly recommended, it does not hurt to do it even though you already have them installed!")
req = str(input("> ")).lower()
if req == "n":
    pass
else:
    print("Installing requirements")
    os.system("pip install smtplib")
    os.system("pip install getpass")
    os.system("pip install time")
    os.system("pip install colorama")
    os.system("pip install PySimpleGUI")
    print("\x1b[94m" +
          "Successfully installed all the requirements.")
    print("Press ENTER to start the program.")
    input()
    print("Booting up the main program")
    time.sleep(1)
    os.system("cls")

MailBomber.STARTUP()
