x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
a = x + y
s = x - y
m = x * y
d = x / y if y != 0 else "undefined (division by zero)"
print(f"Addition: {a}")
print(f"Subtraction: {s}")
print(f"Multiplication: {m}")
print(f"Division: {d}")