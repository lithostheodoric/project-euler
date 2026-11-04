# Find the sum of all the multiples of 3 or 5 below 1000

sum = 0
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number
print(sum)

# For each iteration through a range of numbers including 1 until but excluding 1000, if the iteration number is divisible by 3 or 5 with a remainder of 0,
# the iteration will be added to the sum
