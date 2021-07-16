import random


class Student:
    def __init__(self, name, x):
        self.name = name
        self.x = x

    def equation(self):
        question1 = input(self.name + ', please solve question 1:\n 2x + 10 = 22: ')
        if question1 == '6':
            print('Correct')
            self.equation_second()
        elif question1 == 'calc':
            calc()
            self.equation()
        else:
            print('wrong')
            calculator = input('Would you like to use a calculator: ')
            if calculator == 'Yes':
                calc()
                self.equation()
            else:
                self.equation()

    def equation_second(self):
        question2 = input(self.name + ', please solve question 2:\n 3x - 47 = 7: ')
        if question2 == '18':
            print('Correct')
            self.equation_three()
        elif question2 == 'calc':
            calc()
            self.equation_second()
        else:
            print('wrong')
            calculator = input('Would you like to use a calculator: ')
            if calculator == 'Yes':
                calc()
                self.equation_second()
            else:
                self.equation_second()

    def equation_three(self):
        for _ in range(5):
            value = random.randint(1, 900)
        if value % 2 == 0:
            print(value)
            answer = input(': Is this number even or odd?: ')
            if answer == 'even':
                print('Yes! This number is even!')
            elif answer != 'even':
                print('No! This number is even!')
        else:
            print(value)
            answer = input(': Is this number even or odd?: ')
            if answer == 'odd':
                print('Yes! This number is odd')
            elif answer != 'odd':
                print('No, this number is odd!')

        option = input('Would you like to answer a bonus question? (It is guaranteed points!): ')
        if option == 'Yes':
            self.bonus_question()
        elif option == 'No':
            quit()

    def bonus_question(self):
        random_num = random.randint(1, 10)
        num_input = 0
        while num_input != random_num:
            num_input = int(input(self.name + ' Guess a number: '))
            print(num_input)
            if num_input != random_num:
                print('not quite... ' + self.name)
            else:
                print('You guessed the number! ' + self.name)
                print('The test is now over.')
                quit()


andrew = Student('Andrew', '')
jess = Student('Jess', '')
marc = Student('Marc', '')
alexandria = Student('Alexandria', '')


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


def user():

    username = input('Enter username: ')
    password = input('Enter password: ')

    if username == 'andrew' and password == 'password':
        submit = input('Hello Andrew! Are you ready to take your test!: ')
        if submit == 'Yes':
            andrew.equation()
        else:
            print(submit)
    elif username == 'jess' and password == 'password':
        submit = input('Hello Jess! Are you ready to take your test!: ')
        if submit == 'Yes':
            jess.equation()
        else:
            print(submit)
    elif username == 'marc' and password == 'password':
        submit = input('Hello Marc! Are you ready to take your test!: ')
        if submit == 'Yes':
            marc.equation()
        else:
            print(submit)
    elif username == 'alexandria' and password == 'password':
        submit = input('Hello Alexandria! Are you ready to take your test!: ')
        if submit == 'Yes':
            alexandria.equation()
        else:
            print(submit)
    else:
        print('Please enter a valid username and password')
        user()


user()