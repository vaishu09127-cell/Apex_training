amount = float(input("Enter purchase amount: "))

if amount < 1000:
    discount = amount * 5 / 100
elif amount < 5000:
    discount = amount * 10 / 100
else:
    discount = amount * 15 / 100

net_payable = amount - discount

print("Purchase amount:", amount)
print("Discount:", discount)
print("Net payable:", net_payable)
