import random
from datetime import datetime as date
import time
import os
import json
from helpers.globalVar import database as dbFile
from helpers.findCustomer import findCustomer
from helpers.findCustomer import findCustomerPhonenumber as findCusNumber

def deleteBankAccount(acctNumber, pin=""):
    sendData = {}
    newCustomerData = {}
    newcustomersStore = []
                    
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
                
                for index, customers in enumerate(customer):
                    # return customers whose account isnt equal to the one provided
                    if acctNumber != customers["account_number"]:
                        newcustomersStore.append(customers)
                
                newCustomerData["name"] = result["name"]
                newCustomerData["customers"] = newcustomersStore
                
                fo = open(dbFile, "w")
                fo.write(json.dumps(newCustomerData))
                fo.close()
            
                sendData["error"] = False
                sendData["message"] = "Account Deleted Successfully"
                return sendData
    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong updating customer balance"
        print("")
        return sendData

            

print(deleteBankAccount("544226559", "1234"))
        
    
    

