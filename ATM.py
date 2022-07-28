class Atm:
    def __init__(user,cardnumber,pin):
        user.cardnumber = cardnumber
        user.pin = pin


    def check_balance(user):
        balance = 0
        print("Your balance is : £", balance)


def main():
    print("Welcome to the ATM")
    user = input("Please enter your name: ")
    cardNumber = input("Insert your card number: ")
    pin  = input("Enter your pin: ")

    newUser =  Atm(Account,Card_number,pin_number)

    print("What do you want to do")
    print("Check balance OR Withdraw money)
    action = int(input("Enter what you want to do"))

    if (action == Check balance or check balance):
        newUser.check_balance()
    elif (activity == Withdraw money or withdraw money):
        moneyAdded = int(input("How much money do you want to withdraw: "))
        balance = moneyAdded + balance
        
    else:
        print("Enter a valid action")
