# 2. Flip Coin and print percentage of Heads and Tails
# a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
# b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
# heads
# c. O/P -> Percentage of Head vs Tails
import random
head=0
tail=0

for i in range(0,11):
    coin=random.random()
    if coin<0.5:
        tail+=1
    else:
        head+=1

heads_percentage = (head / 11) * 100
tails_percentage = (tail / 11) * 100

print('Tail Percentage : ', tails_percentage)
print('Head Percentage : ',heads_percentage)