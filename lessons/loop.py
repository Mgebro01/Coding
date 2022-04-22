# # number = 1
# # while True:
# #     number += 1
# #     if number % 4 == 0:
# #      print(number)
# #     if number > 300:
# #      break
# #
# # number = 1
# # while True:
# #     number += 1
# #
# #     if number % 4 != 0:
# #         continue
# #     print(number)
# #
# #     if number > 300:
# #      break
#
# # while number < 10:
# #     print(number)
# #     number += 1
#
# # for i in range(0, 10, 2):
# #     print(i)
#
# # Number = int(input('input number:'))
# #
# # for i in range(Number, 0, -1):
# #
# #     if Number % i == 0:
# #         print(i)
#
# #
# # Number = int(input('input number:'))
# #
# # Number2 = int(input('input number:'))
# # Low = Number2
# #
# # if Number < Number2:
# #
# #     Low = Number
# #
# # for i in range(1, Low + 1):
# #
# #     if Number % i == 0 and Number2 % i == 0:
# #         print(i)
# #
#
#
# # # შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.
# #
# # print()
# # print('შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.')
# # print()
# #
# # Number = int(input('input number:'))
# #
# # Number2 = int(input('input number:'))
# #
# # i = 0
# #
# # while True:
# #     i += 1
# #
# #     if Number < 0 or Number2 < 0:
# #         print('ეს რიცხვი 0-ზე ნაკლებია')
# #         break
# #
# #     if i % Number == 0 and i % Number2 == 0:
# #         print(i)
# #         break
# #
# #
# # # ვარიანტი 2
# #
# #
# # n1 = int(input('input number:'))
# #
# # n2 = int(input('input number:'))
# #
# #
# # high = n1
# # if n2 > n1:
# #     high = n2
# #
# # for i in range(high, n1 * n2 + 1):
# #     if i % n1 == 0 and i % n2 == 0:
# #         print(i)
# #         break
#
# #
# # Number = int(input('input number:'))
# #
# # is_prine = True
# #
# # for i in range(2, Number):
# #
# #     if Number % i == 0:
# #         is_prine = False
# #         break
# #
# # if is_prine:
# #     print("რიცხვი მარტივია")
# #
# # else:
# #     print("რიცხვი შედგენილია")
#
# #ვარიანტი 2
#
# Number = int(input('input number:'))
#
# is_prine = "მარტივია"
#
# for i in range(2, Number):
#
#     if Number % i == 0:
#         is_prine = 'შედგენილია'
#         break
#
# print(is_prine)
#
#
#
# LESSON 7
#
#1
#
# a = 1
# b = 1
#
# while a < 6:
#     print(a)
#     temp = a + b
#     a = b
#     b = temp
#
# # 2
# #
# for n in range(2, 1001):
#     h = 0
#     for i in range(2, n):
#         if n % i == 0:
#             h = 1
#     if h == 0:
#         print(n)


# number = 253
#
# temp_number = number
# count = 0
# num_sum = 0
#
# while temp_number >= 1:
#     num_sum += int(temp_number) % 10
#     count += 1
#     temp_number /= 10
#
# print(count)
# print(num_sum)


#
#
# number = 256
#
# while number // 10 >= 1:
#     number //= 10
#
#
# print(number)


#  6. შეიყვანეთ ნებისმიერი რიცხვი. დაბეჭდეთ შეტანილი რიცხვი შებრუნებული სახით.
#  (მითითება: მაგ. თუ შეიტანთ 1254-ს, დაბეჭდოს 4521). შენიშვნა:
#  არ გააკეთოთ სტრიქონის ტიპის მონაცემისთვის

print()
print('6. შეიყვანეთ ნებისმიერი რიცხვი. დაბეჭდეთ შეტანილი რიცხვი შებრუნებული სახით. (მითითება: მაგ. თუ შეიტანთ 1254-ს, დაბეჭდოს 4521). შენიშვნა: არ გააკეთოთ სტრიქონის ტიპის მონაცემისთვის')
print()

number = 1234

temp_number = number
result = 0

while temp_number >= 1:
    # result = result * 10 + temp_number % 10
    result *= 10
    result += temp_number % 10

    temp_number //= 10

print(result)


