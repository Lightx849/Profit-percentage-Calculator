# Profit percentage calculator
def prof_per():

    profit = 0
    cost_price = 0

    while profit <=0:
        print("profits not less or equal to 0")
        profit = int(input("enter the profit money:"))

        if profit <= 0:
            print(" insufficent profit occured")
            continue

    while cost_price <=0:
        print("cost price not less or equal to 0")
        cost_price = int(input("enter the cost price money:"))

        if cost_price <= 0:
            print(" insufficent cost price occured")
            continue

    percentage = (profit / cost_price) * 100
    return percentage

total_prof = prof_per()

print(f"hence the total profit percentage  is:{total_prof}%")









