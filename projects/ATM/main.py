import sys
import time
from pyfiglet import figlet_format
from colors import Red, Green, Black, Cyan
from helpers.createAccount import createAccount
# import helpers.createAccount

# sys.path.append('./helpers')

class BATM:

    title = figlet_format("B-ATM", font = "banner3"  )
    desc= """
        A basic CLI ATM .
        
        --help, -h : list all common options for interacting witth this ATM
        
        --start, -s : Begin the ATM operations.
    """
    bankoptions = """
        To start, choose from the options below.
        
        [1]. Create Customer account.
        [2]. Redraw Funds
        [3]. Check account balance
        [4]. Change Pin.
        [5]. Deposit.
        [6]. Transfer money from your account to other account.
        [7]. Delete bank account
        [8]. Displays all customer account 
    """
    
    def Error(self, msg=""):
        print("")
        return Red(msg)
    
    def Success(self, msg=""):
        print("")
        return Green(msg)
    
    #   show intro
    def showIntro(self):
        print("")
        Green(self.title)
        Green(self.desc)
    
    def start(self):
        print("")
        Green(self.bankoptions)
        
    
    # Create customer account
    def createCustomerAccount(self):
        print("")
        error = ""
        fullname = input("Enter fullname: ")
        phonenumber = input("Enter your phone number: ")
        dob = input("Enter Date of Birth: ")
        
        # validate inputs
        if fullname == "":
            self.Error("Fullname cant be empty!!")
        if phonenumber == "":
            self.Error("Phonenumber cant be empty!!")
        if dob == "":
            self.Error("Date of birth cant be empty!!")
        
        # validate phonenumber
        try:
            if type(int(phonenumber)) != int:
                error = "Invalid phonenumber: {}".format(phonenumber)
        except:
            self.Error("Invalid phonenumber: {}".format(phonenumber))
        
        if len(phonenumber) > 11 or len(phonenumber) < 11:
            self.Error("You entered invalid phonenumber, of length {}".format(len(phonenumber)))
        
        payload = {
            "fullname": fullname,
            "dob": dob,
            "phonenumber": phonenumber
        }
        
        result = createAccount(payload)
        
        Green("Loading...")
        
        time.sleep(2)
        
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                return self.Success(result["message"])
        
    # redraw funds
    def redrawFunds(self):
        print("redraw funds")
    
    # check balance
    def checkAccountBalance(self):
        print("check Balance")
    
    # change pin
    def changePin(self):
        print("change pin")
    
    # deposit
    def depositFunds(self):
        print("deposit")
    
    # transfer funds
    def transferFunds(self):
        print("transfer funds")
    
    # delete funds
    def deleteAccount(self):
        print("delete account")
    
    def displayAllCustomers(self):
        print("display all customer")
    
    
    def init(self):
        # show intro
        self.showIntro()
        
        # parced some arguments
        argLen = len(sys.argv)
        
        if argLen == 1:
            return False
        elif argLen > 1:
            cliArgs = sys.argv[1]
            
            if cliArgs == "--start" or cliArgs == "-s":
                return self.start()
            elif cliArgs == str(1):
                return self.createCustomerAccount()
            elif cliArgs == str(2):
                return self.redrawFunds()
            elif cliArgs == str(3):
                return self.checkAccountBalance()
            elif cliArgs == str(4):
                return self.changePin()
            elif cliArgs == str(5):
                return self.depositFunds()
            elif cliArgs == str(6):
                return self.transferFunds()
            elif cliArgs == str(7):
                return self.deleteAccount()
            elif cliArgs == str(8):
                return self.displayAllCustomers()
            else:
                self.Error("Invalid arguments passed: {}".format(cliArgs))
                


BATM().init()