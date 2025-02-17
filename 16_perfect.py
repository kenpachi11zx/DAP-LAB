def is_perfect(number):
    if number < 2:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number