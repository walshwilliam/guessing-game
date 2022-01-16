import random
def game():
    global x
    x = random.randint(1, 10)
    print("guess a number from 1 to 10.")
    guess()
def guess():
    global y
    y = input("your guess: ")
    global z
    z = int(y)
    compare()  
def compare():
    if x == z:
        print("good job!", x, "is the number!")
        print("play again?")
        a = input("y/n: ")
        if "y" in a:
            print(" ")
            game()
        else:
            print("fine. bye bye then!")
            print(" ")
    if x != z:
        print("wrong! guess again")
        guess()
game()
