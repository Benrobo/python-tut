import random
from datetime import datetime as date
import time
import os
import json
from globalVar import database as dbFile
from findCustomer import findCustomer
from findCustomer import findCustomerPhonenumber as findCusNumber

def checkAccountBalance(acctNumber, pin=""):
    sendData = {}
    
    if acctNumber == None or acctNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'acctNumber' but got none"
        return sendData
    
    if pin == None or pin == "":
        sendData["error"] = True
        sendData["message"] = "expecting current 'pin' balance but got none"
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
                # compare pin
                if pin != users["pin"]:
                    sendData["error"] = True
                    sendData["message"] = "Invalid Pin entered"
                    return sendData
                
                formatedData = {
                    "acct_name": users["name"],
                    "acct_number": users["account_number"],
                    "current_balance": users["cash"]
                }
                
                sendData["error"] = False
                sendData["message"] = "Successfully"
                sendData["data"] = formatedData                         
                return sendData
    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong updating customer balance"
        print("")
        return sendData

            

print(checkAccountBalance("544226559", "1234"))
        
    
    

