
# ---------- Calculator --------


print('Welcome, this is a simple calculator.')

while True:
    print("Enter + , - , * , / or ** for calculating.")
    print("Press e for exit.")
    users_input = input(">> ")

    if users_input == "e":
        break
    elif users_input == "+":
        print("Please enter two numbers for subtraction:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a+b
    elif users_input == "-":
        print("Please enter two numbers for subtraction:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a-b
    elif users_input == "*":
        print("Please enter two numbers for mutliplicate:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a*b 
    elif users_input == "/":
        print("Please enter two numbers for divide:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a/b
    elif users_input == "**":
        print("Please enter two numbers for power:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a**b
    else:
        print("please enter one of this signs: + , - , * , / , **")
        print()
        print("now continue.....")
        continue
    print()
    print(f'The answer is >> {c}')
    print()

print("Thanks for using our calculator :)")

