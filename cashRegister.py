 #step 1: INPUT (Ask for things)
words = ["first", "second", "third", "fourth", "fifth"]
objects = []
costs = []

total = 0
bought = ""
while bought != "Q":
    bought = input(f"what did you buy? > ")
    if bought != "Q":
        objects.append(bought)
        costs.append(float(input("how much does it cost? > ")))
        total += costs[-1]


# buy2 = (input("what is the second thing your buying? > "))
# cost2 = float(input("how much does it cost? > "))

# buy3 = (input("what is the third thing your buying? > "))
# cost3 = float(input("how much does it cost? > "))


# buy4 = (input("what is the fourth thing your buying? > "))
# cost4 = float(input("how much does it cost? > "))


# buy5 = (input("what is the fifth thing your buying? > "))
# cost5 = float(input("how much does it cost? > "))



#step 2: PROCESSING (calculate one or more things)

# total = cost1 + cost2 + cost3 + cost4 + cost5
tax = total / 13
gtotal = total + tax


#step 3: OUTPUT (Print the answer or answers)

print("++++++++++++++")
print("RECEIPT")
print("++++++++++++++")
for i in range(len(objects)):
    print("%s -------- %.2f" %(objects[i], costs[i]))
# print("%s -------- %.2f" %(buy1, cost1))
# print("%s -------- %.2f" %(buy2, cost2))
# print("%s -------- %.2f" %(buy3, cost3))
# print("%s -------- %.2f" %(buy4, cost4))
# print("%s -------- %.2f" %(buy5, cost5))
print("++++++++++++++")
print("Subtotal: %.2f" %(total))
print("Tax: %.2f" %(tax))
print("Grand Total: %.2f" %(gtotal))