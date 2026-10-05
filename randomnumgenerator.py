import random as r


#intitialize 2 variables
tries = 0
rnumber = 0

#use a loop to generate a bunch of random numbers

while True:
    rnumber = r.randint(1, 100)
    tries += 1
    print("Try #%d --> %d" %(tries, rnumber))
    #every while true loop needs a break in order to stop
    if rnumber == 44:
        print("you got your lucky number!")
        break
       

print("it took %d tries to generate a 44" %tries)