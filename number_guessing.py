import random
# num = random.random()
random_num = random.choice(range(100))

# print(num)
while 1:
    num = int(input("Guess the number between 0 to 99(or enter -1 to stop the game):"))
    if num == -1:
        break
    elif num == random_num:
        print("you guessed it right.")
        break
    elif num > random_num:
        print("The number smaller than",num)
    elif num < random_num:
        print("The number is larger than",num)

print("The number is",random_num)


