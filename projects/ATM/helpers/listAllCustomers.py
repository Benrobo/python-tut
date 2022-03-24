import random
from datetime import datetime as date
import time
import os
import json
from helpers.globalVar import database as dbFile

def listAllCustomers():
    sendData = {}
     
    try:
        f = open(dbFile, "r")
        dbdata = f.read()
        result = json.loads(dbdata)
        customer = result['customers']

        sendData["error"] = False
        sendData["message"] = "Successfully"
        sendData["customers"] = customer                         
        return sendData
    except:
        sendData["error"] = True
        sendData["message"] = "Something went wrong updating customer balance"
        print("")
        return sendData

            

print(json.dumps(listAllCustomers(), indent=4))
        
    
    

