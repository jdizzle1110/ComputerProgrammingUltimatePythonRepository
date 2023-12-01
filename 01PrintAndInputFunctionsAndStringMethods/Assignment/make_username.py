print("Enter info") 
name = input("enter your full name: ").title().replace("", "")
number = input ("Enter favorite number between 1 and 99: ")
print(name + number.zfill(2))
