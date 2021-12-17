# Рекурсия

# def short_story():
#     print("hkahkjfdhas")
#     print("hkahkjfdhas")
#     print("hkahkjfdhas")
#     print("hkahkjfdhas")
#     short_story()

# short_story()


# Find factorial with for cycle
# def factorial(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     return res

# print(factorial(5))


# Find factorial with recursion function
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))


# Practise 1
# 1 - 9 by recursion

# def print_digits(n):
#     if n == 1:
#         return '1'
#     else:
#         return print_digits(n - 1) + ' ' + str(n)

# print(print_digits(10))

# Practise 2
# Sum of digits by recursion
# don't use lists, strings, cycles

# def sum_dig(n):
#     res = 0
#     for dig in str(n):
#         res += int(dig)
#     return res

# print(sum_dig(12344))

# print(156 // 10) #15
# print(156 % 10)  # 6
def sum_digit(number):
    if number > 0:
        return sum_digit(number // 10) + number % 10
    else:
        return 0

print(sum_digit(156)) # 12

# 15 + 6 = 21
# 2 + 1 = 3
# 0 + 


