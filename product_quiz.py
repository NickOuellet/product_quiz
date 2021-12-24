import random
import time

total = 0
correct = 0
print("Type '0' to quit")
while True:
    x = random.randint(1,20)
    y = random.randint(1,20)
    user_input = int(input("What is %d * %d? " % (x,y)))
    time_st = time.time()
    if user_input == 0:
        break
    if (x * y) == user_input:
        total = total + 1
        correct = correct + 1
        print("Correct! %d * %d = %d | %d / %d |\nTime of round: %0.2f" % (x,y,x*y, correct,total, time.time() - time_st) )

    else:
        total = total + 1
        print("Sorry, thats incorrect. %d * %d = %d | %d / %d |\nTime of round: %0.2f" % (x,y,x*y, correct,total, time.time() - time_st) )
    print("New Round ... \n")
print("You have a success rate of %d percent and %d total rounds played" % (correct*100/total, total))