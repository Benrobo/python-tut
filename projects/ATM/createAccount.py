import sys
import os
import random
from datetime import datetime as date
import time
import json
from findCustomer import findCustomer
from findCustomer import findCustomerPhonenumber as findCusNumber
from genId import genId
from genAcctNumber import generateAccountNumber as genAcctNum
from formatDate import formatDate
from genPin import generatePin

# Dbfile 
currdir = os.getcwd()
dbFile = os.path.join(currdir, "db.json")

# print(dbFile)

def createAccount(payload):
    sendData = {}
    
    # verify payload
    payloadLength = len(list(payload))
    if payloadLength == 0:
        sendData["error"] = True
        sendData["message"] = "expected a valid payload but got none"
        return sendData
    
    if payloadLength > 0:
        # customer data
        phonenumber = payload["phonenumber"]
        dob = payload["dob"]
        fullname = payload["fullname"]
        
        # check if customer with that phonenumber exist
        check = findCusNumber(phonenumber)
        
        if check["error"] == True:
            sendData["error"] = False
            sendData["message"] = check["message"]
            return sendData
        
        elif check["error"] == False and check["rowCount"] == 1:
            sendData["error"] = True
            sendData["message"] = "Customer with that phone number already exist"
            return sendData
        
        try:
            f = open(dbFile, "r")
            dbdata = f.read()
            result = json.loads(dbdata)
            customer = result['customers']
            
            newcustomer = {
                "id": genId(),
                "name": fullname,
                "phone_number": phonenumber,
                "DOB": dob,
                "account_number": genAcctNum(),
                "pin": generatePin(),
                "cash": "0",
                "joined": formatDate()
            }
            
            customer.append(newcustomer)
                
            # update file database
            fo = open(dbFile, "w")
            fo.write(json.dumps(result))
            fo.close()
            
            sendData["error"] = False
            sendData["message"] = "Account created"
            sendData["data"] = newcustomer
            return sendData

        except:
            sendData["error"] = True
            sendData["message"] = "Something went wrong creating account."
            print("")
            return sendData
            

payload = {
    "fullname": "Mark Brad",
    "dob": "11/03/2002",
    "phonenumber": "07034209681"
}

# print(createAccount(payload))
        
    
    

