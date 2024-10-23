def is_perfect(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        return True
    else:
        return False


def perfect_numbers(count):
    perfect_numbers = []
    num = 1

    while len(perfect_numbers) < count:
        if is_perfect(num):
            perfect_numbers.append(num)
        num += 1

    return perfect_numbers


result = perfect_numbers(4)
print(result)
