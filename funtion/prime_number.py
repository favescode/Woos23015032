 # Program to check if a number is prime or not

def check_prime():
    num = int(input(" Pls enter your number :  "))
    for x in range( 2 , num ):
        if num % x == 1:
            return True
        elif num % x == 0:
            return False


print(check_prime())