def calc():
    var1 = int(input('Enter a number: '))
    op = input('Enter an operator: ')
    var2 = int(input('Enter a number: '))

    if op == '+':
        print(var1 + var2)
        var3 = input('Would you like to perform another calculation: ')
        if var3 == "No":
            print('Goodbye!')
        elif var3 == "Yes":
            calc()

    elif op == '-':
        print(var1 - var2)
        var3 = input('Would you like to perform another calculation: ')
        if var3 == "No":
            print('Goodbye!')
        elif var3 == "Yes":
            calc()

    elif op == '*':
        print(var1 * var2)
        var3 = input('Would you like to perform another calculation: ')
        if var3 == "No":
            print('Goodbye!')
        elif var3 == "Yes":
            calc()

    elif op == '/':
        print(var1 / var2)
        var3 = input('Would you like to perform another calculation: ')
        if var3 == "No":
            print('Goodbye!')
        elif var3 == "Yes":
            calc()

    elif op == '%':
        print(var1 % var2)
        var3 = input('Would you like to perform another calculation: ')
        if var3 == "No":
            print('Goodbye!')
        elif var3 == "Yes":
            calc()

    else:
        print('Invalid operator or number. Please Try Again')
        calc()