has_good_credit = True
price_of_house = 1000000
if has_good_credit:
    down_payment = price_of_house * 0.1
else:
    down_payment = price_of_house * 0.2

print(f"Price is ${down_payment}")
