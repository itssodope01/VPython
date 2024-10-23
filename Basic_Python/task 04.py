def the_number():
    c = 0
    while True:
        c += 1
        if all(c % i == 0 for i in range(1, 11)):
            return c

result = the_number()
print(result)
