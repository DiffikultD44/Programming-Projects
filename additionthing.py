number = int(input("Enter a number: "))
sum = 0
while True:
    sum += number
    number = int(input("Enter another number (or 100 to stop): "))
    if number == 100:
        break
print("The sum is:", sum)