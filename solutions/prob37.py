# Problem 37
# Trucatable primes

# Key Idea: Left trunctable prime can
# only be generated by adding a digit
# to another left truncatable prime.
# Same for right.

from itertools import permutations
from functools import reduce
from tools.prime import is_prime

digits = ['1', '2', '3', '5', '7', '9']

left_primes = ['2', '3', '5', '7']
right_primes = ['2', '3', '5', '7']

running_sum = 0

digit_cnt = 0

while True:
    digit_cnt += 1
    if digit_cnt > 9:
        break
    new_left_primes = []
    for num in left_primes:
        for digit in digits:
            if is_prime(int(digit + num)):
                new_left_primes.append(digit + num)
    new_right_primes = []
    for num in right_primes:
        for digit in digits:
            if is_prime(int(num + digit)):
                new_right_primes.append(num + digit)
    same_nums = list(set(new_left_primes) & set(new_right_primes))
    print(same_nums)
    temp_sum = sum(int(val) for val in same_nums)
    running_sum += temp_sum
    left_primes = new_left_primes
    right_primes = new_right_primes

print(running_sum)