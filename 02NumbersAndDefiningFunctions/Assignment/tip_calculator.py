print("Enter Info")
price = float(input("Enter meal price: "))
percent = int(input("Enter tip percentage: ")) / 100
print(round(float(price * percent), 2))