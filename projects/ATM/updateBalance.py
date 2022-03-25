import random
from datetime import datetime as date
import time
import os
import json
from helpers.findCustomer import findCustomer
from helpers.globalVar import database as dbFile
# Utility File

# Update customer cash

def updateCustomerBalance(acctNumber="", cash=""):
    sendData = {}
    
    if acctNumber == None or acctNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'acctNumber' but got none"
        return sendData
    
    if cash == None or cash == "":
        sendData["error"] = True
        sendData["message"] = "expecting current 'cash' balance but got none"
        return sendData
    
    # check if the pat5h is valid
    
    if os.path.exists(dbFile) == False:
        sendData["error"] = True
        sendData["message"] = "database database file doesnt exist: "+ dbFile
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
                users["cash"] = cash

        # update file database
        overideData = {
            "name": result["name"],
            "customers": customer
        }
        print(overideData)
        fo = open(dbFile, "w")
        fo.write(json.dumps(overideData))
        fo.close()
        
        sendData["error"] = False
        sendData["message"] = "Cash updated"
        sendData["data"] = customer
        return sendData

    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong updating customer balance"
        print("")
        return sendData
  
print(updateCustomerBalance("544226559", "45000"))