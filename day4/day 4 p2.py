percentage = float(input("Enter percentage: "))
income = int(input("Enter family income: "))

percentage_ok = percentage >= 75
income_ok = income <= 30000

print("percentage_ok:", percentage_ok)
print("income_ok:", income_ok)
print("Scholarship eligible:", percentage_ok and income_ok)
print("At least one condition:", percentage_ok or income_ok)
print("Not percentage_ok:", not percentage_ok)
