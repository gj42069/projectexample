import sqlite3
con = sqlite3.connect("accounting.db")
name = input("What is you last and first name?")
companyname = input("What is the name of your company?")
date = input("What is the date?")
choice = input("Welcome to the balancing sheeter and incoming stater. Would you like to make a balance sheet or income statement?")
picking = True
while picking == True:
    if choice == "balance sheet":
        picking = False
    elif choice == "income statement":
        picking = False
    else:
        picking = True
        choice = input("Please choose between balance sheet or income statement")
if choice == "balance sheet":
    cash = float(input("How much cash do you have?"))
    ars = int(input("How much accounts recivables are there?"))
    arname = []
    arvalue = []
    print("Give the name of the each account receivable and how much you are owed one at a time")
    for i in range(1, ars+1):
        arname[i] = input("Name of the account recivable?")
        arvalue[i] = float(input("How much you are receiving?"))
    supplies = float(input("How much are your supplies worth? Put zero if you have none"))
    land = float(input("How much is your land worth?"))
    building = float(input("How much is your building worth?"))
    furniture = float(input("How much is your furniture and equipment worth?"))
    automobiles = float(input("How much is your automobiles worth? Put 0 if you own none"))
    aps = int(input("How much accounts payables do you have?"))
    apname = []
    apowed = []
    print("Give the name of the account payable and how much is owed one at a time")
    for i in range(1, aps+1):
        apname[i] = input("Name of the account payable?")
        apowed[i] = float(input("How much do you owe?"))
    bankloan = float(input("How much did the bank loan you?"))
    mortgagepayable = float(input("How much is the mortgage payable"))
    combinedar = 0
    for i in range(1, ars+1):
        combinedar = arvalue[i] + combinedar
    totalassets = combinedar + cash + supplies + land + building + furniture + automobiles
    combinedaps = 0
    for i in range(1 + aps):
        combinedaps = combinedaps + apowed[i]
    totalliabilities = combinedaps + bankloan + mortgagepayable
    capital = totalassets - totalliabilities
    totalliabilitiesandequity = capital + totalliabilities
elif choice == "income statement":
    feesearned = float(input("How much is your fees earned?"))
    sales = float(input("how much did you make from sales?"))
    costofgoodssold = float(input("What is the cost of goods sold?"))
    profits = sales + feesearned - costofgoodssold
    advertising = float(input("What is your advertising expense? Put zero if none"))
    bankinterestandcharges = float(input("What is your bank interest and charge expense?"))
    buildingmaintenance = float(input("How much does building maintenance cose"))
    carexpense = float(input("How much does car expense cost?"))
    deprecation = float(input("How much is the deprecation expense?"))
    insurance = float(input("How much is the insurance expence?"))
    miscellaneous = float(input("How much was the miscellaneous expense?"))
    supplyexp = float(input("How much is the supply expense?"))
    sundry = float(input("What is the sundry expense?"))
    licenses = float(input("How much is the license expense?"))
    lightheatwater = float(input("How much does light, heat and water cost?"))
    rent = float(input("How much was rent?"))
    repairs = float(input("How much was the repair and maintenance expense?"))
    telephone = float(input("What is the telephone expense?"))
    utilities = float(input("How much do the other utilities cost?"))
    wages = float(input("How much do you pay your workers?"))
    totalexpenses = advertising + bankinterestandcharges + buildingmaintenance + carexpense +deprecation + insurance + miscellaneous + supplyexp + sundry + licenses + lightheatwater + rent + repairs + telephone + utilities + wages
    netincome = profits - totalexpenses