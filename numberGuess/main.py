import random

class Game:
    def guess():
        num = random.randint(1, 10)
        triesLeft = 10
        while triesLeft != 0:
            guess = int(input("Guess the number between 1 and 10 (inlusive): "))
            if guess != num:
                triesLeft -= 1
                print(f"You have {triesLeft} tries left!\n")
            else:
                print(f"You got it right!\n")
                print(f"The number was {guess}")

                #Ask to play again
                print("--------------------------------------\n")
                finalAsk = input("Would you like to play again?: ").lower()
                if finalAsk == 'yes':
                    Game.guess()
                else:
                    exit()

#Driver Files
if __name__ == "__main__":
    print("Number guess game using python")
    Game.guess()
