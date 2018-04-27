def product(*numbs):
    a = 1
    for x in numbs:
        a = a * x
    return a

print(product(2))
