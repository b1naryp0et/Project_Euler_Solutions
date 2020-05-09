#!/usr/bin/python3

# Program which sums all multiples of 3 and 5 below 1000

j = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        j += i
        
print(j)
