import random


RandomNumber = random.randint(1 ,100)

print("The number has been chosen. ")

Counter = 0

while(True):
    Counter += 1

    if(Counter > 5):
        print("Unfortunately could not guess in time and you LOST.")
        
        restart = input("Do you want to play again? 1.Yes  2.No:  ")

        if restart.isdigit():

            restart = int(restart)
            if(restart == 1):
                RandomNumber = random.randint(1 ,100)
                print("The number has been chosen. ")
                Counter = 0
            else:
                print("Bye. ")
                break

        else:
            print("Invalid input. Please enter integer. ")
            continue
        


    InputNumber = input("guess: ")

    if InputNumber.isdigit():
        Number = int(InputNumber)
    else:
        print("Invalid input. Please enter integer. ")
        continue

    if(Number < 0):
        print("Error!!!Your number must be between 1 and 100.")
        continue

    if(Number > 100):
        print("Error!!!Your number must be between 1 and 100.")
        continue
    

    if(Number > RandomNumber):
        print("Too high!!!")
        continue
        
    elif(RandomNumber > Number):
        print("Too low!!!")
        continue
        
    else:
        print("Congratulations! You guessed it!")
        print(f"It took you {Counter} guesses to win." )
        break
    