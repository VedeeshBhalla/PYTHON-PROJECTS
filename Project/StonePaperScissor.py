import random

options = ["stone" , "paper" , "scissors"]
running = True

while running:
        playerName = input("Enter player name : ")
        computer = random.choice(options)
        playerOptions = None

        while playerOptions not in options:
            playerOptions = input("Enter a choice(stone , paper , scissors) : ").lower()
            print("------------------------------------------------------")
            if   playerOptions== computer:
                print("ITS A TIE !!")  
            elif playerOptions == "stone" and computer == "scissors":
                print(f"{playerName} wins!!") 
            elif playerOptions == "stone" and computer == "paper":
                print(f"Computer wins!!")
            elif playerOptions == "s" and computer == "paper":
                print(f"{playerName} wins!!")
            elif playerOptions == "s" and computer == "stone":
                print(f"Computer wins!!")
            elif playerOptions == "paper" and computer == "stone":
                print(f"{playerName} wins!!")
            elif playerOptions == "paper" and computer == "s":
                print("Computer wins!!")
            else:
                break   
    
        print(f"{playerName} choice : {playerOptions}")
        print(f"Computer choice : {computer}")
        print("------------------------------------------------------")