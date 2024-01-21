def getguess():
    guess=int(input("What did you guess? "))
    return guess

def main():
    guess=getguess()
    if guess == 27:
        print("Thats correct")
    else:
        print("You guessed the wrong number")

main()