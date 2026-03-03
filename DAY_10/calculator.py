from art import logo
print(logo)
import os

def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
}

fn=True
while(True):
    if(fn==True):
        first_number = float(input("Enter first number: "))
    operator = input("Enter operation to be performed (+,-,*,/): ")
    second_number = float(input("Enter second number: "))

    result = operations[operator](first_number,second_number)
    
    print(f"{first_number} {operator} {second_number} : {result}")
    repeat = input("Do you want to continue with previous result (y) or start new calculation (n) or exit (e): ")
    if(repeat=='y'):
        fn=False
        first_number=result
    elif repeat=='n':
        os.system('cls')
        fn=True
    elif repeat=='e':
        print("Good bye!\n")
        break
    
