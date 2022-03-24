import random
from datetime import datetime as date
import time
import os
import json
from globalVar import database as dbFile

# Find customer based on accountNumber

def findCustomer(acctNumber):
    sendData = {}
    rowCount = 0
    
    if acctNumber == None or acctNumber == "":
        sendData["error"] = True
        sendData["message"] = "failed to find customer, expecting 'acctNumber' but got none"
        return sendData

    # dbFile = os.path.join(currdir, "projects", "ATM", "db.json")
    
    # check if the path is valid
    
    if os.path.exists(dbFile) == False:
        sendData["error"] = True
        sendData["message"] = "database doesnt exist: "+ dbFile
        return sendData
    
    try:
        f = open(dbFile, "r")
        dbdata = f.read()
        result = json.loads(dbdata)
        customers = result["customers"]
       
        if len(customers) == 0 :
            sendData["error"] = True
            sendData["message"] = "No customer found"
            print("")

        # Valid account numbers
        acctnums = []
        # search for customers
        for index, users in enumerate(customers):
            acctnums.append(users["account_number"])
        
        if acctNumber in acctnums:
            rowCount = 1
            sendData["error"] = False
            sendData["rowCount"] = rowCount
            return sendData
        else: 
            rowCount = 0
            sendData["error"] = False
            sendData["rowCount"] = rowCount
            return sendData
         
    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong searching for customer"
        print("")
        return sendData
    
    
# print(findCustomer("544226559"))

# Find Customer with phone number

def findCustomerPhonenumber(phoneNumber):
    sendData = {}
    rowCount = 0
    
    if phoneNumber == None or phoneNumber == "":
        sendData["error"] = True
        sendData["message"] = "failed to find customer, expecting 'phoneNumber' but got none"
        return sendData

    # dbFile = os.path.join(currdir, "projects", "ATM", "db.json")
    
    # check if the path is valid
    
    if os.path.exists(dbFile) == False:
        sendData["error"] = True
        sendData["message"] = "database doesnt exist: "+ dbFile
        return sendData
    
    try:
        f = open(dbFile, "r")
        dbdata = f.read()
        result = json.loads(dbdata)
        customers = result["customers"]
       
        if len(customers) == 0 :
            sendData["error"] = True
            sendData["message"] = "No customer found"
            print("")

        # Valid account numbers
        phoneNums = []
        # search for customers
        for index, users in enumerate(customers):
            phoneNums.append(users["phone_number"])
        
        if phoneNumber in phoneNums:
            rowCount = 1
            sendData["error"] = False
            sendData["rowCount"] = rowCount
            return sendData
        else: 
            rowCount = 0
            sendData["error"] = False
            sendData["rowCount"] = rowCount
            return sendData
         
    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong searching for customer"
        print("")
        return sendData
    
# print(findCustomerPhonenumber("07070712296"))