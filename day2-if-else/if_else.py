# Small ATM machine code with the help of if-else.

total_amount=5000

wid=int(input("Enter amount: "))

if wid<=total_amount:
    
    remain=total_amount-wid
    print("Succesfully GIVEN:",wid,"Rupees")
    print("Remaining amount:",remain,"Rupees")
else:
    print(wid,"is Greater than account balance("+str(total_amount)+").")
    print("-------Enter more cash-------")

    add=int(input("Enter amount:"))
    total_amount=total_amount+add

    print(add,"Succesfully added in bank Account.")
    print("ACCOUNT BALANCE:",total_amount)