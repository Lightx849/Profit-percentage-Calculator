# Profit-percentage-Calculator

def prof_per():

    profit = 0
    cost_price = 0
    sell_price = 0

    while sell_price <= 0:
        print("sell price not less or equal to 0")
        sell_price = int(input("enter the sell price money:"))

        if sell_price <= 0:
            print(" insufficent sell price occured")
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

