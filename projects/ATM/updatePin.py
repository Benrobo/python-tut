import random
from datetime import datetime as date
import time
import os
import json
from findCustomer import findCustomer
# from globalVar import database as dbFile

currdir = os.getcwd()
dbFile = os.path.join(currdir,"db.json")

# for test purpose below 
#####################################
# dbFile = os.path.join(currdir, "projects", "ATM","db.json")
#####################################

def updateCustomerPin(acctNumber="", pin="", newpin=""):
    sendData = {}
    
    if acctNumber == None or acctNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'acctNumber' but got none"
        return sendData
    
    if pin == None or pin == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'pin' but got none"
        return sendData
    
    if newpin == None or newpin == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'newpin' but got none"
        return sendData

    # check if the pat5h is valid
    
    if os.path.exists(dbFile) == False:
        sendData["error"] = True
        sendData["message"] = "database datbe file doesnt exist: "+ dbFile
        return sendData
    
    # Check if customer exist in db with that id
    check = findCustomer(acctNumber)
    
    if check["error"] == True:
        return check["message"]
    
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
            if users["account_number"] == acctNumber:
                # validate pin
                if users["pin"] != pin:
                    sendData["error"] = True
                    sendData["message"] = "You entered wrong old pin: {}".format(pin) 
                    return sendData
                
                users["pin"] = newpin
                
        # update file database
        overideData = {
            "name": result["name"],
            "customers": customer
        }
        fo = open(dbFile, "w")
        fo.write(json.dumps(overideData))
        fo.close()
        
        sendData["error"] = False
        sendData["message"] = "Pin updated successfullt"
        return sendData

    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong updating customer data"
        print("")
        return sendData
  

# print(updateCustomerPin("2265567117", "2222", "3344"))