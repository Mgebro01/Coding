number = 1
# while True:
#     number += 1
#     if number % 4 == 0:
#      print(number)
#     if number > 300:
#      break
#
# number = 1
# while True:
#     number += 1
#
#     if number % 4 != 0:
#         continue
#     print(number)
#
#     if number > 300:
#      break

# while number < 10:
#     print(number)
#     number += 1

# for i in range(0, 10, 2):
#     print(i)

Number = int(input('input number:'))

answer = 0

for i in range(Number, 0, -1):

    if Number % i == 0:
        print(i)