import os
import pwinput
import random

from components.Style import Style
from error.Error import Error
from model.User import User
from datetime import date, datetime

# CURRENT DATE
today = date.today()
currentDate = today.strftime("%B %d, %Y")

# CURRENT DATE AND TIME
now = datetime.now()
currentDateTime = now.strftime("%d/%m/%Y %H:%M:%S")

# MOCK DATABASE
listOfUser = [
    User("John Doe", "123456", 123.56),  # index: 101
    User("Jane Doe", "456789", 123.1234),  # index: 102
    User("Juan Dela Cruz", "987654", 123.45),  # index: 103
    User("Diego Silang", "654321", 123.978),  # index: 104
    User("Jose Bonifacio", "147258", 123.00),  # index: 105
    User("Mary Knorr", "258369", 123.12),  # index: 106
    User("Willie Da Pooh", "159357", 123.94),  # index: 107
    User("Bing Chilling", "123987", 123.6543),  # index: 108
    User("Apolinario Arroyo", "123987", 123.65),  # index: 109
    User("Andres Rizal", "307982", 123.1234)  # index: 110
]

# PAGES
def main() :
    os.system('cls')
    Style.header()
    getCardId = input("     Please enter your card number : ")
    try :
        isInteger = isinstance(int(getCardId), int)
        if isInteger :
            hasRecord = False
            index = 0
            for i in range(0, len(listOfUser)) :
                if int(getCardId) == listOfUser[i].cardId :
                    index = i
                    hasRecord = True
                    break
                elif int(getCardId) != listOfUser[i].cardId :
                    continue
            if hasRecord :
                secondStep(index)
            else :
                Error.cardNotFound()
                isTransactionContinue()
    except :
        Error.dataTypeChecker()
        isTransactionContinue()

def secondStep(index) :
    os.system('cls')
    Style.header()
    getPin = pwinput.pwinput(prompt="     Please enter six (6) digit pin : ", mask='*')
    try :
        isInteger = isinstance(int(getPin), int)
        if isInteger :
            if len(str(getPin)) == 6 :
                if str(listOfUser[index].pin) == str(getPin) :
                    welcomePage(index)
                else:
                    Error.cardIdAndPinNotMatch()
                    isTransactionContinue2(index)
            else :
                Error.invalidNumberOfPin()
                isTransactionContinue2(index)
    except :
        Error.dataTypeChecker()
        isTransactionContinue2(index)

def welcomePage(index) :
    os.system('cls')
    Style.menu()

    print(f"     Hello {listOfUser[index].name}, ")
    option = input("\n     Enter [1, 2, 3, 4 or 5]: ")
    try :
        isInteger = isinstance(int(option), int)
        if isInteger :
            if int(option) == 1 :
                accountDetails(index)
            if int(option) == 2 :
                checkBalance(index)
            if int(option) == 3 :
                deposit(index)
            if int(option) == 4 :
                withdraw(index)
            if int(option) == 5 :
                resetProgram()
            if int(option) > 5 :
                Error.optionVerifier()
                isTransactionContinue3(index)
    except :
        Error.dataTypeChecker()
        isTransactionContinue3(index)


# ATM MAIN FUNCTIONALITY
def accountDetails(index) :
    os.system('cls')
    Style.accountDetailsHeader()

    print(f"\n     NAME: {listOfUser[index].name}, ")
    print(f"\n     CARD NUMBER: {listOfUser[index].cardId}, ")
    print(f"\n     CURRENT BALANCE: Php {listOfUser[index].currentBalance:.2f}")

    goBackToWelcomePage(index)

def checkBalance(index) :
    os.system('cls')
    Style.checkBalanceHeader()

    print(f"     As of {currentDate} your current balance is : Php {listOfUser[index].currentBalance: .2f}")
    goBackToWelcomePage(index)

def deposit(index):
    os.system('cls')
    Style.depositHeader()
    currentBalance = listOfUser[index].currentBalance
    transactionNumber = random.randint(10000, 1000000)
    getDeposit = float(input("\n     Amount you want to deposit: Php "))
    try :
        isFloat = isinstance(getDeposit, (float, int))
        if isFloat :
            if float(getDeposit) > 0 :
                newBalance = float(currentBalance) + float(getDeposit)
                listOfUser[index].currentBalance = float(newBalance)
                print(f"\n     You successfully deposit Php {getDeposit}")
                print(f"\n     Your current balance is : Php {listOfUser[index].currentBalance: .2f}")
                receiptDeposit(transactionNumber, getDeposit, currentBalance, newBalance, index)
            else :
                Error.negativeNumberNotAllowed()
                goBackToDepositPage(index)
    except :
        Error.dataTypeChecker()
        goBackToDepositPage(index)

def withdraw(index):
    os.system('cls')
    Style.depositHeader()
    currentBalance = listOfUser[index].currentBalance
    transactionNumber = random.randint(10000, 1000000)
    print(f"     As of {currentDate} your current balance is : Php {listOfUser[index].currentBalance: .2f}")
    getWithdraw = float(input("\n     Amount you want to withdraw: Php "))
    try :
        isFloat = isinstance(getWithdraw, (float, int))
        if isFloat :
            if float(getWithdraw) > 0 :
                if float(currentBalance) > float(getWithdraw):
                    newBalance = float(currentBalance) - float(getWithdraw)
                    listOfUser[index].currentBalance = float(newBalance)
                    print(f"\n     You successfully withdraw Php {getWithdraw}")
                    print(f"\n     Your current balance is : Php {listOfUser[index].currentBalance: .2f}")
                    receiptWithdraw(transactionNumber, getWithdraw, currentBalance, newBalance, index)
                else :
                    Error.notEnoughBalance()
                    goBackToWithdrawPage(index)
            else :
                Error.negativeNumberNotAllowed()
                goBackToWithdrawPage(index)
    except :
        Error.dataTypeChecker()
        goBackToWithdrawPage(index)


# CONDITIONAL TRANSACTION
def isTransactionContinue() :
    transaction = input("\n     Do you want to retry the transaction? [1] Yes, [2] No : ")
    if transaction == '1' :
        os.system('cls')
        main()
    elif transaction == '2' :
        Style.endProgram()
    else :
        Error.yesNoVerifier()
        isTransactionContinue()

def isTransactionContinue2(index) :
    transaction = input("\n     Do you want retry the transaction? [1] Yes, [2] No : ")
    if transaction == '1' :
        os.system('cls')
        secondStep(index)
    elif transaction == '2' :
        resetProgram()
    else :
        Error.yesNoVerifier()
        isTransactionContinue()

def isTransactionContinue3(index) :
    transaction = input("\n     Do you want retry the transaction? [1] Yes, [2] No : ")
    if transaction == '1' :
        os.system('cls')
        welcomePage(index)
    elif transaction == '2' :
        resetProgram()
    else :
        Error.yesNoVerifier()
        isTransactionContinue()

def goBackToWelcomePage(index) :
    transaction = input("\n     Do you want to go back? [1] Yes, [2] No : ")
    if transaction == '1' :
        os.system('cls')
        welcomePage(index)
    elif transaction == '2' :
        resetProgram()
    else :
        Error.yesNoVerifier()
        isTransactionContinue()

def goBackToDepositPage(index) :
    transaction = input("\n     Do you want to go back? [1] Yes, [2] No : ")
    if transaction == '1' :
        os.system('cls')
        welcomePage(index)
    elif transaction == '2' :
        deposit(index)
    else :
        Error.yesNoVerifier()
        isTransactionContinue()

def goBackToWithdrawPage(index) :
    transaction = input("\n     Do you want to go back? [1] Yes, [2] No : ")
    if transaction == '1' :
        os.system('cls')
        welcomePage(index)
    elif transaction == '2' :
        withdraw(index)
    else :
        Error.yesNoVerifier()
        isTransactionContinue()

def userSummary(index) :
    os.system('cls')
    transaction = random.randint(10000, 1000000)
    print(f"""
        +----------------------------------------------------------+
           Transaction is now complete.                         
           Transaction number: {transaction} 
           Transaction date: {currentDate}
           
           Account holder: {listOfUser[index].name}                   
           Account number: {listOfUser[index].cardId}            
           Available balance: Php.{listOfUser[index].currentBalance: .2f}                                  
        +----------------------------------------------------------+
    """)
    print("""
        +----------------------------------------------------------+
        +             THANK YOU FOR USING OLFU PYBANK              +
        +             SEE YOU ON YOUR NEXT TRANSACTION             +
        +                        GOOD BYE                          +
        +----------------------------------------------------------+ 
        """)
    try :
        stopProgram = input("\n     Press any [enter] to exit...")
        if stopProgram :
            main()
        else :
            main()
    except :
        main()

def resetProgram() :
    os.system('cls')
    print("""
    +----------------------------------------------------------+
    +             THANK YOU FOR USING OLFU PYBANK              +
    +             SEE YOU ON YOUR NEXT TRANSACTION             +
    +                        GOOD BYE                          +
    +----------------------------------------------------------+ 
    """)
    try :
        stopProgram = input("\n     Press any [enter] to exit...")
        if stopProgram :
            main()
        else :
            main()
    except:
        main()

# FILE HANDLING
def printReceiptDeposit(transactionNumber, amountDeposit, oldBalance, newBalance, index) :
    path= f'./receipts/'
    filename = f"OLFU_PYBANK_LOGS_CARD-{listOfUser[index].cardId}_{currentDate}"
    completeName = os.path.join(path, filename + ".txt")
    receipt = open(completeName, 'a')
    receipt.write(f"""
    \n    Transaction number: {transactionNumber}
        +----------------------------------------------------------+
        +                                                          +
        +                    OLFU PYBANK RECEIPT                   +
        +                                                          +
        +----------------------------------------------------------+
           Transaction is now complete.                         
           Transaction date: {currentDateTime}
           
           Transaction made: DEPOSIT
           Deposited amount : {amountDeposit}
           
           Old Balance: {oldBalance}
           new Balance: {newBalance}
           
           Account holder: {listOfUser[index].name}                   
           Account number: {listOfUser[index].cardId}            
           Available balance: Php.{listOfUser[index].currentBalance: .2f}                              
        +----------------------------------------------------------+
        +        THANK YOU, SEE YOU ON YOUR NEXT TRANSACTION       +
        +----------------------------------------------------------+
    """)
    receipt.close()

def receiptDeposit(transactionNumber, amountDeposit, oldBalance, newBalance, index) :
    os.system('cls')
    print(f"""
            Transaction number: {transactionNumber}
            +----------------------------------------------------------+
            +                                                          +
            +                    OLFU PYBANK RECEIPT                   +
            +                                                          +
            +----------------------------------------------------------+
               Transaction is now complete.                         
               Transaction date: {currentDateTime}

               Transaction made: DEPOSIT
               Deposited amount : {amountDeposit}

               Old Balance: {oldBalance}
               new Balance: {newBalance}

               Account holder: {listOfUser[index].name}                   
               Account number: {listOfUser[index].cardId}            
               Available balance: Php.{listOfUser[index].currentBalance: .2f}                              
            +----------------------------------------------------------+
            +        THANK YOU, SEE YOU ON YOUR NEXT TRANSACTION       +
            +----------------------------------------------------------+
        """)
    printReceiptDeposit(transactionNumber, amountDeposit, oldBalance, newBalance, index)
    try :
        stopProgram = input("\n     Press any [enter] to exit...")
        if stopProgram :
            main()
        else :
            main()
    except :
        main()

def printReceiptWithdraw(transactionNumber, amountWithdraw, oldBalance, newBalance, index) :
    path = f'./receipts/'
    filename = f"OLFU_PYBANK_LOGS_CARD-{listOfUser[index].cardId}_{currentDate}"
    completeName = os.path.join(path, filename + ".txt")
    receipt = open(completeName, 'a')
    receipt.write(f"""
    \n    Transaction number: {transactionNumber}
        +----------------------------------------------------------+
        +                                                          +
        +                    OLFU PYBANK RECEIPT                   +
        +                                                          +
        +----------------------------------------------------------+
           Transaction is now complete.                         
           Transaction date: {currentDateTime}

           Transaction made: WITHDRAW
           Withdraw amount : {amountWithdraw}

           Old Balance: {oldBalance}
           new Balance: {newBalance}

           Account holder: {listOfUser[index].name}                   
           Account number: {listOfUser[index].cardId}            
           Available balance: Php.{listOfUser[index].currentBalance: .2f}                              
        +----------------------------------------------------------+
        +        THANK YOU, SEE YOU ON YOUR NEXT TRANSACTION       +
        +----------------------------------------------------------+
    """)
    receipt.close()

def receiptWithdraw(transactionNumber, amountWithdraw, oldBalance, newBalance, index) :
    os.system('cls')
    print(f"""
            Transaction number: {transactionNumber}
            +----------------------------------------------------------+
            +                                                          +
            +                    OLFU PYBANK RECEIPT                   +
            +                                                          +
            +----------------------------------------------------------+
               Transaction is now complete.                         
               Transaction date: {currentDateTime}

               Transaction made: WITHDRAW
               Withdraw amount : {amountWithdraw}

               Old Balance: {oldBalance}
               new Balance: {newBalance}

               Account holder: {listOfUser[index].name}                   
               Account number: {listOfUser[index].cardId}            
               Available balance: Php.{listOfUser[index].currentBalance: .2f}                              
            +----------------------------------------------------------+
            +        THANK YOU, SEE YOU ON YOUR NEXT TRANSACTION       +
            +----------------------------------------------------------+
        """)
    printReceiptWithdraw(transactionNumber, amountWithdraw, oldBalance, newBalance, index)
    try :
        stopProgram = input("\n     Press any [enter] to exit...")
        if stopProgram :
            main()
        else :
            main()
    except :
        main()

# MAIN PROGRAM
while True :
    main()
    break
