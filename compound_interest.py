principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (Years): "))

amount = principal * (1 + rate/100) ** time
ci = amount - principal

print("Compound Interest =", ci)
print("Total Amount =", amount)