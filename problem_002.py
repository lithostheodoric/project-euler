def fibonacci():
    """ Sum all of the even integers in a Fibonacci sequence under 4,000,000 """
    even_sum = 0
    n1, n2 = 1, 2

    while n2 < 4_000_000:
        if n2 % 2 == 0:
            even_sum += n2

        n1, n2 = n2, n1 + n2

    print(f"The sum of even values in the Fibonacci sequence is: {even_sum}")

if __name__ == '__main__':
    fibonacci()
        