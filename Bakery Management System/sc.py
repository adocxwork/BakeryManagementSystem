from datetime import datetime


def check_for_stock():
    with open("stock.txt") as f:
        stock = eval(f.read())
        print("Items , Quantity , Price")
        for i in stock:
            print(i,",",stock[i][0],",",stock[i][1])
    print()

def explore_exciting_food():
    with open("stock.txt") as f:
        stock = eval(f.read())
        print("Items , Price")
        for i in stock:
            print(i,",",stock[i][1])
    print()

def order_something_exciting():
    print("Loading Items...")
    explore_exciting_food()
    ite = input("Enter the item : ")
    amtt = int(input("Enter the quantity : "))
    with open("stock.txt") as f:
        stock = eval(f.read())
    if ite in stock:
        if amtt > stock[ite][0]:
            print("Sorry\nGiven quantity is Not availble...")
        else:
            nn = input("Enter your Name : ")
            stock[ite][0] = stock[ite][0] - amtt
            with open("stock.txt","w") as f:
                f.write(str(stock))
            price = stock[ite][1]*amtt
            with open("money.txt") as f:
                mypocket = float(f.read())
            mypocket = mypocket + price
            with open("money.txt", "w") as f:
                f.write(str(mypocket))
            print(f"Hey {nn},\nHere is your bill....\n")
            print("------Royal Bakery------")
            print("------------------------")
            print("----------Bill----------")
            print(datetime.now())
            print(nn)
            print("Item , Quantity , Total Price")
            print(ite,amtt,price)
            print()
            print("---------------Eat Fresh, Stay Fresh")
            print()
            print()
    else:
        print("The given item doesn't exist...")
    print()

def add_items_to_stock():
    with open("stock.txt") as f:
        stock = eval(f.read())
        print("Items , Quantity , Price")
        for i in stock:
            print(i,",",stock[i][0],",",stock[i][1])
    inp = input("Enter the item to be added : ")
    qua = int(input("Enter the amount of quantity to be added : "))
    found = False
    for i in stock:
        if i == inp:
            stock[i][0] = stock[i][0] + qua
            with open("stock.txt","w") as f:
                f.write(str(stock))
            found = True
            price = (stock[i][1]*qua)/2
            with open("money.txt") as f:
                mypocket = float(f.read())
            mypocket = mypocket - price
            with open("money.txt","w") as f:
                f.write(str(mypocket))
                print(f"Payment done..!\nRs. {price}")
                print("Your current balance is : ", mypocket)
    if found == False:
        print("The Entered item doesn't exists...")
    else:
        print("The Stock updated successfully...")
    print()

def remove_items_from_stock():
    with open("stock.txt") as f:
        stock = eval(f.read())
        print("Items , Quantity , Price")
        for i in stock:
            print(i,",",stock[i][0],",",stock[i][1])
    rite = input("Enter the item : ")
    qa = int(input("Enter quantity : "))
    if rite in stock:
        if qa>stock[rite][0]:
            print("Stock doesn't meets the requirements..")
        else:
            stock[rite][0] = stock[rite][0] - qa
            with open("stock.txt","w") as f:
                f.write(str(stock))
            price = stock[rite][1]*qa
            with open("money.txt") as f:
                mypocket = float(f.read())
            mypocket = mypocket + price
            print("Payment Received.., Rs.", price)
            with open("money.txt", "w") as f:
                f.write(str(mypocket))
    else:
        print("The item doesn't exists...")
    print()

def change_in_price():
    with open("stock.txt") as f:
        stock = eval(f.read())
        print("Items , Quantity , Price")
        for i in stock:
            print(i,",",stock[i][0],",",stock[i][1])
    ite = input("Enter the item, whose price you wanna change : ")
    p = int(input("Enter the price, which you want to have : "))
    if ite in stock:
        stock[ite][1] = p
        with open("stock.txt","w") as f:
            f.write(str(stock))
            print("Price updated..")
    else:
        print("The item doesn't exist...")
    print()

def pay_to_working_staff():
    amt = int(input("Enter the amount to be paid : "))
    with open("money.txt") as f:
        mypocket = float(f.read())
    if mypocket >= amt:
        mypocket = mypocket - amt
        print("Payment done..")
    else:
        print("There is not enough balance in your account.")
    with open("money.txt","w") as f:
        f.write(str(mypocket))
    print()

def checkBalance():
    with open("money.txt") as f:
        print("Your balance is :-")
        print("Rs. ",float(f.read()))
        print()

def password_for_admin():
    with open("pass.txt") as f:
        ad_pass = f.read()
        return ad_pass

def change_admin_password():
    ad_neww = input("Enter your Current Password : ")
    if ad_neww == password_for_admin():
        np = input("Enter your new Password : ")
        cnp = input("Re-enter your new Password : ")
        if np == cnp:
            with open("pass.txt","w") as f:
                f.write(cnp)
            print("---Password Updated---")
        else:
            print("Password did not matched..!!")
    else:
        print("---Wrong Password---")
    print()

# __main__

while True:
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    ii = input("Enter Input : ")

    # Admin
    if ii == "1":
        # I'm Admin bro.., here i'm..!!
        adnew = input("Enter Password : ")
        if adnew == password_for_admin():
            # Admin Login Successful..!!
            print("---Logged In Successfully---")

            while True:
                print("1. Check the Remaining Stock")
                print("2. Add items")
                print("3. Remove items")
                print("4. Change price")
                print("5. Pay to Working Staff")
                print("6. Change Admin Password")
                print("7. Check Money balance")
                print("8. Log out")

                fn = input("Enter Input : ")
                print()
                if fn == "1":
                    check_for_stock()
                elif fn == "2":
                    add_items_to_stock()
                elif fn == "3":
                    remove_items_from_stock()
                elif fn == "4":
                    change_in_price()
                elif fn == "5":
                    pay_to_working_staff()
                elif fn == "6":
                    change_admin_password()
                elif fn == "7":
                    checkBalance()
                elif fn == "8":
                    print("---Logging Out---")
                    break
                else:
                    print("---Invalid Input---")

        else:
            # Admin password is wrong...!!
            print("---Wrong Password---")

    # Customer
    elif ii == "2":
        print("---Welcome To Royal Bakery---")
        while True:
            print("1. Explore Delicious Food Items")
            print("2. Order Something Exciting")
            print("3. Return back to Main Menu")

            fnn = input("Enter Input : ")
            print()
            if fnn == "1":
                explore_exciting_food()
            elif fnn == "2":
                order_something_exciting()
            elif fnn == "3":
                break
            else:
                print("---Invalid Input---")

    # Exit
    elif ii == "3":
        print("---Shutting Down---")
        print("---Shutting Down---")
        print("---Shutting Down---")
        print()
        break

    # Invalid Input
    else:
        print("---Invalid Input---")
print("---Thank You---")