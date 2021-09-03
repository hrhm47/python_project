import random
# print("\n\t\t****** Gussing Number ******* \n\n")
#
# def guess_number(rng):
#     random_number = random.randint(1,rng)
#     guess = 0
#     while guess != random_number:
#         guess = int(input('Guess the Number: '))
#         if guess > random_number:
#             print("Guess is to high")
#         else:
#             print("Guess is to low")
#     print("you guess the right number that is ",random_number)
#
# rng = int(input("\t\t Enter a range for Your self to Guess a Number: "))
# guess_number(rng)

print("\t\t\t Guess a number on Computer\n\n")

print("\t\t\t\t Thinks A number in Your Mind And guess it from Computer :)\n")

def guess_number(rng):
    low = 1
    high = rng
    guess = 0
    guess_string = ""
    while guess_string != 'c':
        if low != high :
            guess = random.randint(low,high)
        else:
            guess = low
        guess_string=input("\n\t\tIf guess number "+ str(guess) +" is too high (h), or too low (l) else write (c):")
        if guess_string == 'h':
            high = guess - 1
        elif guess_string == 'l':
            low = guess + 1
    print("\n\t\tyou guess the right number that is ",guess," \n\t\t\t Congratulations")

rng = int(input("\t\t Enter a range to Guess a Number from Computer: "))
guess_number(rng)