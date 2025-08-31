import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
print(answer)
guesses = 0
is_running = True

print("------PYTHON NUMBER GUESSING GAME------")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess = int(input("Enter your guess : "))
    guesses+=1
    
    if guess<lowest_num or guess>highest_num:
        print("Number out of range")
        print(f"Please select between {lowest_num} & {highest_num}")
        
        
    elif guess < answer:
        print("Too Low !! , Try again")
        print("----------------------------")
        
    elif guess > answer:
        print("Too High!! , Try again")
        print("----------------------------")
                
    else:
        if guess == answer:
            print()
            print(f"CORRECT!!, The answer was {answer}")
            print(f"No of Guesses : {guesses}")
            break
    
    