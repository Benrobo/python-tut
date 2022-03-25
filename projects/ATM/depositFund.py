import random
from datetime import datetime as date
import time
import os
import json
from globalVar import database as dbFile
from findCustomer import findCustomer
from findCustomer import findCustomerPhonenumber as findCusNumber

# currdir = os.getcwd()
# dbFile = os.path.join(currdir, "projects", "ATM", "db.json")

def depositFund(accountNumber, pin, amount=""):
    sendData = {}
    
    if accountNumber == None or accountNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'accountNumber' but got none"
        return sendData
    
    if pin == None or pin == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'pin' but got none"
        return sendData
    
    if amount == None or amount == "":
        sendData["error"] = True
        sendData["message"] = "expecting current 'amount' balance but got none"
        return sendData
    
    if os.path.exists(dbFile) == False:
        sendData["error"] = True
        sendData["message"] = "database file doesnt exist: "+ dbFile
        return sendData
    
    # Check if customer exist in db with that account number
    sender = findCustomer(accountNumber)
    
    # check if sender account exist
    if sender["error"] == True:
        sendData["error"] = False
        sendData["message"] = f"""{sender["message"]}: invalid account number"""
        return sendData

    # check if sender exists
    elif sender["error"] == False and sender["rowCount"] == 0:
        sendData["error"] = True
        sendData["message"] = "Failed to deposit with this: {}".format(senderAcctNumber)
        return sendData
    
    
    try:
        f = open(dbFile, "r")
        dbdata = f.read()
        result = json.loads(dbdata)
        customer = result['customers']
        
        for index, users in enumerate(customer):
            # validate pin
            if accountNumber == users["account_number"]:

                if pin != users["pin"]:
                    sendData["error"] = True
                    sendData["message"] = "Pin is incorrect"
                    return sendData
                
                # if pin is correct, 
                currBal = int(users["cash"])
                users["cash"] = currBal + int(amount) 
                
                # update file database
                fo = open(dbFile, "w")
                fo.write(json.dumps(result))
                fo.close()
                
                formatedData = {
                    "acct_name": users["name"],
                    "acct_number": users["account_number"],
                    "amount_deposit": amount,
                    "current_balance": users["cash"]
                }
                
                sendData["error"] = False
                sendData["message"] = "Transaction was successfull"
                sendData["data"] = formatedData                         
                return sendData
         
    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong updating customer balance"
        print("")
        return sendData

            
    

