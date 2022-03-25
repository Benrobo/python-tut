import sys
import os
import time
from pyfiglet import figlet_format
from colors import Red, Green, Black, Cyan
from createAccount import createAccount
from depositFund import depositFund
from transferCash import transferCash
from redrawCash import redrawCash
from checkBalance import checkAccountBalance
from listAllCustomers import listAllCustomers
from findCustomer import findCustomer
from deleteAccount import deleteBankAccount
from updatePin import updateCustomerPin
from globalVar import database as dbFile


class BATM:

    title = figlet_format("B-ATM", font = "banner3"  )
    desc= """
        A basic CLI ATM .
        
        --help, -h : list all common options for interacting witth this ATM
        
        --start, -s : Begin the ATM operations. or 
    """
    bankoptions = """
        To start, choose from the options below.
        
        [1]. Create Customer account.
        [2]. Withdraw Funds
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
        loading = False
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
        print("")
            
        time.sleep(2)
        
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                self.Success(result["message"])
                print("")
                print("------------------------")
                print(f"{'Account Number':10} | {'PIN':10}")
                print(f"{result['data']['account_number']} | {result['data']['pin']}")
                print("------------------------")
        
    # redraw funds
    def withDrawFunds(self):
        print("")
        accountNumber = input("Enter account number: ")
        pin = input("Enter Pin: ")
        amount = input("Amount: ")
        
        # validate inputs
        if accountNumber == "":
            self.Error("accountNumber cant be empty!!")
        if pin == "":
            self.Error("pin cant be empty!!")
        if amount == "":
            self.Error("amount cant be empty!!")
        
        # validate phonenumber
        try:
            if type(int(accountNumber)) != int or type(int(pin)) or type(int(amount)):
                pass
        except:
            self.Error("Invalid details")
        
        
        result = redrawCash(accountNumber, pin, amount)
        print("")
            
        time.sleep(2)
        
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                self.Success(result["message"])
                print("")
                print("------------------------")
                Cyan(f"Account From: $: {result['data']['acct_name']}.00 ")
                print("")
                Cyan(f"Account Number: $: {result['data']['acct_number']} ")
                print("")
                Cyan(f"Amount withdrawn: $: {result['data']['amount_withdrawn']} ")
                print("")
                Cyan(f"Current Balance: $: {result['data']['current_balance']}.00 ")
                print("------------------------")
    
    # check balance
    def checkAccountBalance(self):
        print("")
        error = ""
        accountNumber = input("Enter account number: ")
        pin = input("Enter Pin: ")
        
        # validate inputs
        if accountNumber == "":
            self.Error("accountNumber cant be empty!!")
        if pin == "":
            self.Error("pin cant be empty!!")
        
        # validate
        try:
            if type(int(accountNumber)) != int or type(int(pin)):
                error = "Invalid details"
        except:
            self.Error("Invalid details")
        
        
        result = checkAccountBalance(accountNumber, pin)
        print("")
            
        time.sleep(2)
        
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                self.Success(result["message"])
                print("")
                print("---------------------------------")
                Cyan(f"Account Name: $: {result['data']['acct_name']} ")
                print("")
                Cyan(f"Account Number: $: {result['data']['acct_number']} ")
                print("")
                Cyan(f"Current Balance: $: {result['data']['current_balance']}.00 ")
                print("---------------------------------")
    
    # change pin
    def changePin(self):
        print("")
        accountNumber = input("Enter your account number: ")
        # pin = input("Enter Pin: ")
        oldpin = input("Enter Old Pin: ")
        newpin = input("Enter New Pin: ")
        
        # validate inputs
        if accountNumber == "":
            self.Error("accountNumber cant be empty!!")
        if oldpin == "":
            self.Error("oldpin cant be empty!!")
        if newpin == "":
            self.Error("newpin cant be empty!!")
        
        # validate
        try:
            if type(int(accountNumber)) != int or type(int(oldpin)) or type(int(newpin)):
                error = "Invalid details"
        except:
            self.Error("Invalid details")
        
        
        result = updateCustomerPin(accountNumber, oldpin, newpin)
        print("")
            
        time.sleep(2)
        
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                self.Success(result["message"])
                print("")
     
    # deposit
    def depositFunds(self):
        print("")
        error = ""
        accountNumber = input("Enter account number: ")
        pin = input("Enter Pin: ")
        amount = input("Amount to be deposited: ")
        
        # validate inputs
        if accountNumber == "":
            self.Error("accountNumber cant be empty!!")
        if pin == "":
            self.Error("pin cant be empty!!")
        if amount == "":
            self.Error("amount cant be empty!!")
        
        # validate phonenumber
        try:
            if type(int(accountNumber)) != int or type(int(pin)) or type(int(amount)):
                pass
        except:
            self.Error("Invalid details")
        
        
        result = depositFund(accountNumber, pin, amount)
        print("")
            
        time.sleep(2)
        
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                self.Success(result["message"])
                print("")
                print("------------------------")
                Cyan(f"Account From: $: {result['data']['acct_name']}.00 ")
                Cyan(f"Amount: $: {result['data']['amount_deposit']} ")
                Cyan(f"Current Balance: $: {result['data']['current_balance']}.00 ")
                print("------------------------")
    
    # transfer funds
    def transferFunds(self):
        print("")
        senderAcctNumber = input("Enter your account number: ")
        recieverAcctNumber = input("Enter reciever account number: ")
        # pin = input("Enter Pin: ")
        amount = input("Amount to be transfered: ")
        
        # validate inputs
        if senderAcctNumber == "":
            self.Error("senderAcctNumber cant be empty!!")
        if recieverAcctNumber == "":
            self.Error("recieverAcctNumber cant be empty!!")
        # if pin == "":
        #     self.Error("pin cant be empty!!")
        if amount == "":
            self.Error("amount cant be empty!!")
        
        # validate phonenumber
        try:
            if type(int(senderAcctNumber)) != int or type(int(recieverAcctNumber)) or type(int(amount)):
                error = "Invalid details"
        except:
            self.Error("Invalid details")
        
        
        result = transferCash(senderAcctNumber, recieverAcctNumber, amount)
        print("")
            
        time.sleep(2)
        
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                self.Success(result["message"])
                print("")
                print("---------------------------------")
                Cyan(f"Account From: $: {result['data']['acct_name_from']} ")
                Cyan(f"Account To: $: {result['data']['acct_name_to']} ")
                Cyan(f"Amount: $: {result['data']['amount_transfer']} ")
                Cyan(f"Current Balance: $: {result['data']['current_balance']}.00 ")
                print("---------------------------------")
    
    # delete funds
    def deleteAccount(self):
        print("")
        validNoCheck = ["NO", "No", "no", "nO", "N", "n"]
        validYesCheck = ["Yes", "YES", "yes", "YeS", "Y", "y", "yeS"]
        confirm = input("Are you sure you wanna delete your account? this process is inreversible: Y/N : ")
        
        if confirm in validNoCheck:
            return False
        if confirm in validYesCheck:
            
            accountNumber = input("Enter your account number: ")
            pin = input("Enter Pin: ")
            
            # validate inputs
            if accountNumber == "":
                self.Error("accountNumber cant be empty!!")
            if pin == "":
                self.Error("pin cant be empty!!")

            # validate
            try:
                if type(int(accountNumber)) != int or type(int(pin)):
                    pass
            except:
                self.Error("Invalid details")
            
            
            result = deleteBankAccount(accountNumber, pin)
            print("")
                
            time.sleep(2)
            
            if result:
                if result["error"] == True:
                    return self.Error(result["message"])
                elif result["error"] == False:
                    self.Success(result["message"])
                    print("")
    
    def displayAllCustomers(self):
        print("")
       
        result = listAllCustomers()
        print("")
            
        if result:
            if result["error"] == True:
                return self.Error(result["message"])
            elif result["error"] == False:
                print("")
                print("------------------------------------------------------")
                Cyan("Name | Account Number | Cash | Phone Number |")
                
                customers = result["customers"]
                
                for index, users in enumerate(customers):
                    print("------------------------------------------------------")
                    Green(f""" {users["name"]} | {users["account_number"]} | ${users["cash"]}.00 | {users["phone_number"]} """)
                
                print("------------------------------------------------------")
    
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
            elif cliArgs == "--help" or cliArgs == "-h":
                return self.start()
            elif cliArgs == str(1):
                pass
                return self.createCustomerAccount()
            elif cliArgs == str(2):
                return self.withDrawFunds()
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