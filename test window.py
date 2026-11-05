
import random

f = 0.5
t = 0.75
s = 0.95

bf = int(input("how many frodo"))
bt = int(input("how many twux"))
bs = int(input("how many snookers"))
for x in range(bf):
    r = random.random()
    if r < f:
        break
    elif r < t:
        break
    elif r < s:
        break
    else:
        break

total = (bf * f) + (bt * t) + (bs * s)
print ("The total is: ", total)