import random
def game():
    global x
    x = random.randint(1, 10)
    print("guess a number from 1 to 10.")
    guess()
def guess():
    global y
    y = input("your guess: ")
    list =  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if y in list:
        global z
        z = int(y)
        compare()
    else:
        print ("i said a number from 1 to 10, you idiot! try again.")
        guess()
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
