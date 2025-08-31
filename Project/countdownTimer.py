import time

choice = int(input("Enter choice : "))

match choice:
    case 1:
        my_time = int(input("Enter time in sec : "))
        for x in range(1,my_time+1):
            seconds = x%60
            minutes = int(x/60) % 60
            hour = int(x/3600)
            print(f"{hour:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
        print("Times Up!")
    
    case 2:
        my_time = int(input("Enter time in sec : "))
        for x in range(my_time , 0 , -1):
            seconds = x%60
            minutes = int(x/60) % 60
            hour = int(x/3600)
            print(f"{hour:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
        print("Times Up!")

