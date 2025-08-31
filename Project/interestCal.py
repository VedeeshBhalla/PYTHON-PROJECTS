principle = int(input("Enter Principle : "))
rate = float(input("Enter rate : "))
time = int(input("Enter time : "))

total = principle * pow((1 + rate/100), time)

print(f"Balance after {time} year/s : {total:.2f}")