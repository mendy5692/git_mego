
def fibonacci(n):
    if n <= 1:  # 2 base cases: if n is either 0 or 1, then just prt. it
            return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # 2x rec. call


# example usage:
n = 5
print(f"The {n}th element in the fibo. seq.: {fibonacci(n)}")
