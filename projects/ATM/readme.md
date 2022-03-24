
# Benrobo Automated CLI Machine

This is a fully automated bank ATM machine built using python. A cli base application which has most of the functionalities an ATM / Bank would have.

1. [x] Create Customer account.
2. [x] Generate customer Pin code
3. [x] Generate bank account number.
4. [x] Redraw Cash
5. [x] Check account balance
6. [x] Change Pin.
7. [x] Transfer money from your account to other account.
8. [x] Delete bank account
9. [x] Displays all customer account 


## Basic Customers Info Schema

```json

    {
        "name": "Benrobo-CLI",
        "customers": [
            {
                "id": "wedfwe34523",
                "name": "Benrobo",
                "phone_number": "07070712296",
                "DOB": "12/02/2002",
                "pin": "2222",
                "account_number": "2265567117",
                "cash": "39000",
                "joined": "Feb 02, 2022"
            },
            {
                "id": "dsfgfert6w45et",
                "name": "John Doe",
                "phone_number": "08080815951",
                "DOB": "12/02/2002",
                "pin": "1234",
                "account_number": "544226559",
                "cash": 65400,
                "joined": "Feb 02, 2022"
            },
            {
                "id": "#2@)1hb!(4^",
                "name": "Mark Brad",
                "phone_number": "08034209681",
                "DOB": "11/03/2002",
                "account_number": "0023453509911",
                "pin": "3533",
                "cash": 17300,
                "joined": "March 24, 2022 06:08 AM"
            }
        ]
    }

```