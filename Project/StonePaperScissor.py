import random

options = ["stone" , "paper" , "scissors"]
running = True
playerName = input("Enter player name : ")
win = 0
total = 0
while running:
        computer = random.choice(options)
        playerOptions = None
        
        while playerOptions not in options:
            playerOptions = input("Enter a choice(stone , paper , scissors) : ").lower()
            print("------------------------------------------------------")
            if   playerOptions== computer:
                print("ITS A TIE !!") 
                total+=1 
            elif playerOptions == "stone" and computer == "scissors":
                print(f"{playerName} wins!!") 
                wins+=1
                total+=1 
            elif playerOptions == "stone" and computer == "paper":
                print(f"Computer wins!!")
                total+=1 
            elif playerOptions == "scissors" and computer == "paper":
                print(f"{playerName} wins!!")
                wins+=1
                total+=1 
            elif playerOptions == "scissors" and computer == "stone":
                print(f"Computer wins!!")
                total+=1 
            elif playerOptions == "paper" and computer == "stone":
                print(f"{playerName} wins!!")
                wins+=1
                total+=1 
            elif playerOptions == "paper" and computer == "s":
                print("Computer wins!!")
                total+=1 
            else:
                break   
    
        print(f"{playerName} choice : {playerOptions}")
        print(f"Computer choice : {computer}")
        print("------------------------------------------------------")
        
print(f"Score = {wins}/{total}")