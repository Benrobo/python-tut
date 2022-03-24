import random
from datetime import datetime as date
import time
import os
import json
from helpers.findCustomer import findCustomer
from helpers.globalVar import database as dbFile

# Create file

def createFile(filename):
    sendData = {}
    
    if filename == None or filename == "":
        sendData["error"] = True
        sendData["message"] = "Failed to create file, filename isnt provided"
        return sendData
    
    # get current directory
    currdir = os.getcwd()
    baseDir = os.path.join(currdir, "projects", "ATM")
    filedir = os.path.join(currdir, "projects", "ATM", filename)
    
    # check if the pat5h is valid
    
    if os.path.exists(baseDir) == False:
        sendData["error"] = True
        sendData["message"] = "Failed to create file, path doest exist: "+ baseDir
        return sendData
    
    # create file
    try:
        f = open(filedir, "a")
        sendData["error"] = False
        sendData["message"] = f"{filename} has been created"
        return sendData
    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong creating file"
        print("")
        return sendData
    

def updateCustomerPin(acctNumber="", pin=""):
    sendData = {}
    
    if acctNumber == None or acctNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'acctNumber' but got none"
        return sendData
    
    if pin == None or pin == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'pin' but got none"
        return sendData
    
    # get current directory
    currdir = os.getcwd()
    dbFile = os.path.join(currdir, "projects", "ATM", "db.json")
    
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
        sendData["error"] = False
        sendData["message"] = "No customer found with this account number"
        return sendData
    

    try:
        f = open(dbFile, "r")
        dbdata = f.read()
        result = json.loads(dbdata)
        customer = result['customers']
        
        for index, users in enumerate(customer):
            if users["account_number"] == acctNumber:
                users["pin"] = pin
        
        # update file database
        overideData = {
            "name": result["bank_name"],
            "customers": customer
        }
        fo = open(dbFile, "w")
        fo.write(json.dumps(overideData))
        fo.close()
        
        sendData["error"] = False
        sendData["message"] = "Customer Pin updated successfullt"
        return sendData

    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong updating customer data"
        print("")
        return sendData
  

print(updateCustomerPin("2265567117", "2222"))