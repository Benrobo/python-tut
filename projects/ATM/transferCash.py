import random
from datetime import datetime as date
import time
import os
import json
from globalVar import database as dbFile
from findCustomer import findCustomer
from findCustomer import findCustomerPhonenumber as findCusNumber

def transferCash(senderAcctNumber, recieverAcctNumber, amount=""):
    sendData = {}
    
    if senderAcctNumber == None or senderAcctNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'senderAcctNumber' but got none"
        return sendData
    
    if recieverAcctNumber == None or recieverAcctNumber == "":
        sendData["error"] = True
        sendData["message"] = "expecting 'recieverAcctNumber' but got none"
        return sendData
    
    if amount == None or amount == "":
        sendData["error"] = True
        sendData["message"] = "expecting current 'amount' balance but got none"
        return sendData
    
    if os.path.exists(dbFile) == False:
        sendData["error"] = True
        sendData["message"] = "database file doesnt exist: "+ dbFile
        return sendData
    
    # Check if both customer exist in db with that account number
    sender = findCustomer(senderAcctNumber)
    reciever = findCustomer(recieverAcctNumber)
    
    # check if sender account exist
    if sender["error"] == True:
        sendData["error"] = False
        sendData["message"] = f"""{sender["message"]}: invalid account number from sender"""
        return sendData
    
    # check if reciever account exists
    if reciever["error"] == True:
        sendData["error"] = False
        sendData["message"] = f"""{reciever["message"]}: invalid account number from reciever"""
        return sendData
    # check if sender exists
    elif sender["error"] == False and sender["rowCount"] == 0:
        sendData["error"] = True
        sendData["message"] = "No customer found with this account number: {}".format(senderAcctNumber)
        return sendData
    
    # check if reciever exists
    elif reciever["error"] == False and reciever["rowCount"] == 0:
        sendData["error"] = True
        sendData["message"] = "No customer found with this account number {}".format(recieverAcctNumber)
        return sendData
    
    try:
        f = open(dbFile, "r")
        dbdata = f.read()
        result = json.loads(dbdata)
        customer = result['customers']
        
        
        for index, users in enumerate(customer):
            if senderAcctNumber == users["account_number"]:
                senderAcct = users
                senderCurrentBal = int(senderAcct["cash"])
                mainAmount = int(amount)
                
                if mainAmount > senderCurrentBal:
                    
                    sendData["error"] = True
                    sendData["message"] = "Insufficient Fund to transfer: current balance {}".format(senderCurrentBal)
                    return sendData

            if recieverAcctNumber == users["account_number"]:
                recieverAcct = users
                # subtract amount from senders account
                senderAcct["cash"] = int(senderAcct["cash"]) - int(mainAmount)
                # add amount to reciever account
                recieverCurrBal = int(recieverAcct["cash"])
                newCurrentBalance = (int(mainAmount) + int(recieverCurrBal))
                recieverAcct["cash"] = newCurrentBalance
                
                
                # update file database
                fo = open(dbFile, "w")
                fo.write(json.dumps(result))
                fo.close()
                
                formatedData = {
                    "acct_name_from": senderAcct["name"],
                    "acct_name_to": recieverAcct["name"],
                    "acct_number_from": senderAcct["account_number"],
                    "acct_number_to": recieverAcct["account_number"],
                    "amount_transfer": mainAmount,
                    "current_balance": senderAcct['cash']
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

            

# print(transferCash("544226559", "0023453509911", "16797300"))
        
    
    

