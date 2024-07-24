import repetition

user_input = "Y"

while user_input != "3":
    user_input = input("Select an operation: \n1-Factorial\n2-Sum odd numbers\n3-Exit ")
    if user_input == "1":
        num = int(input("Enter a number greater than 0 and less than 100: "))
        while num <=0 or num >= 100:
            print("That number is invalid.") 
            num = int(input("Enter a number greater than 0 and less than 100: "))
        print("The factorial of "+ str(num) +" is "+ str(repetition.get_factorial(num)))
       
    if user_input == "2":
        num = int(input("Enter a number greater than 0 and less than 100: "))
        while num <=0 or num >= 100:
            print("That number is invalid.") 
            num = int(input("Enter a number greater than 0 and less than 100: "))
        print("The the sum of the odd numbers that comprise "+ str(num) +" is "+ str(repetition.sum_odd_numbers(num)))
 
