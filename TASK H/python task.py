limit_available = 100000
due_amount = 0

while True:
    spending_amount = int(input("Enter how much you want to spend: "))

    if spending_amount <= limit_available:
        limit_available = limit_available - spending_amount
        due_amount = due_amount + spending_amount

        print("Take the amount:", spending_amount)
        print("You can still use:", limit_available)
        print("Your due amount is:", due_amount)

    else:
        if due_amount >= spending_amount:
            due_amount = due_amount - spending_amount
            limit_available = limit_available + spending_amount
            print("Due cleared.")
        else:
            print("Exceeded the card limit.")
