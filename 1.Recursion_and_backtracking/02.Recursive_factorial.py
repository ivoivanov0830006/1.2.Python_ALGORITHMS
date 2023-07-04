def calc_fact(n):
    if n == 0:   # base case
        return 1
    return n * calc_fact(n - 1)


number = int(input())

print(calc_fact(number))
