n = 0
evens = 0
n1, n2 = 1, 2

while n2 < 4000000:
    if n1 % 2 == 0:
        evens += n1
    elif n2 % 2 == 0:
        evens += n2
    n = n1 + n2
    n1 = n
    if n2 < n1:
        n2 = n2 + n1
    else:
        n1 = n1 + n2

print(f"The sum of even values in the Fibonacci sequence is: {evens}")
