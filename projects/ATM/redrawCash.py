import random
from datetime import datetime as date
import time
import os
import json
from globalVar import database as dbFile
from findCustomer import findCustomer
from findCustomer import findCustomerPhonenumber as findCusNumber

def redrawCash(acctNumber, pin="", amount=""):
    sendData = {}
    
    if acctNumber == None or acctNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'acctNumber' but got none"
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
    check = findCustomer(acctNumber)
    
    if check["error"] == True:
        sendData["error"] = False
        sendData["message"] = check["message"]
        return sendData
    
    elif check["error"] == False and check["rowCount"] == 0:
        sendData["error"] = True
        sendData["message"] = "No customer found with this account number"
        return sendData
    
    try:
        f = open(dbFile, "r")
        dbdata = f.read()
        result = json.loads(dbdata)
        customer = result['customers']
        
        
        for index, users in enumerate(customer):
            if acctNumber == users["account_number"]:
                if users["pin"] != pin:
                    sendData["error"] = True
                    sendData["message"] = "Pin isnt correct: {}".format(pin)
                    return sendData
                
                currentBal = int(users["cash"])
                mainAmount = int(amount)
                
                
                if mainAmount > currentBal:
                    
                    sendData["error"] = True
                    sendData["message"] = "Insufficient Balance: {}".format(currentBal)
                    return sendData

                newCurrentBalance = (currentBal-mainAmount)
                users["cash"] = newCurrentBalance
                
                # update file database
                fo = open(dbFile, "w")
                fo.write(json.dumps(result))
                fo.close()
                
                formatedData = {
                    "acct_name": users["name"],
                    "acct_number": users["account_number"],
                    "amount_withdrawn": mainAmount,
                    "current_balance": newCurrentBalance
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

            

print(redrawCash("544226559", "17300"))
        
    
    

