# Instructions
# Add your code to the fizzbuzz function.
# The function takes a number as an argument.
# If the number is evenly divisble by 3, the function returns "fizz"
# If the number is evenly divisble by 5, the function returns "buzz"
# If the number is evenly divisble by 3 and 5, the function returns "fizzbuzz"
def fizzbuzz(number):
    # add your code here
    if(number % 3 == 0 and number % 5 == 0):
        return "fizzbuzz"
    elif(number % 3 == 0):
        return "fizz"
    elif(number % 5 == 0):
        return "buzz"
    else:
        return number

def main():
    for number in range(1,101):
        print(fizzbuzz(number))

if __name__ == "__main__":
    main()