purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount > 100:
    discount = purchase_amount * 0.10
else:
    discount = purchase_amount * 0.05
print(f"Discount amount: ${discount:.2f}")
