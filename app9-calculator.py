no1 = float(input("Enter first number : "))
op = input("Enter operator : ")
no2 = float(input("Enter second number :"))

if op == "+":
    print(no1 + no2)

elif op == "-":
    print(no1 - no2)

elif op == "*":
    print(no1 * no2)

elif op == "/":
    print(no1 / no2)

elif op == "%":
    print(no1 % no2)

else:
    print("Invalid Operator")