import random

magic_number = [random.randint(0, 9),random.randint(0,9)]

def run_number_of_attempts(chances):
    
    for attempt in range(chances):
        print("your attempt {} ".format(attempt))
        user_check_number()
        

def user_check_number():
    user_input = int(input("Enter your number "))
    if user_input in magic_number:
        print("your number is right")
    if user_input not in magic_number:
        print("your number is quite wrong")


user_attempts = int(input("number of attempts? "))
run_number_of_attempts(user_attempts)








          
