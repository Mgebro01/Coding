# Homework 1

# print(9-3, 8*2.5, 9/2, 9/-2, 9%2, 9**2)
# print(4-2**3+5*2-3/2)
# print((3+245)*4-3**4)
# print((42+3*3)/(2+4))



# # Homework 2
#
# # 1-What's up, Tim
#
# message = "What's up, Tim?"
# print(message)
#
# # 2-A and B reverse
#
# a = 1
# b = 4
# a, b = b, a
# print('a', a, 'b', b)
#
# # 3- Name and last name
#
# Name = input("What's your name?:")
# lastname = input("What's your last name?:")
#
# print('you are', Name, lastname)
#
# # 4- Salary per month
#
# Salaryperhour = input('How much do you earn per hour?:')
# Workingtime = input('How long do you work a month?:')
# Answer = int(Salaryperhour) * int(Workingtime)
#
# print('You earn', Answer, '$ per month')
#
#
# # 5- საშუალო არითმეტიკული
#
# a = input("write any number:")
# b = input("write any number:")
# c = input("write any number:")
#
# Answer = ((int(a)+int(b)+int(c))/3)
# print(Answer)
#
# # 6- How many years to 100 years
#
# Name, Age = (input("What's your name?:")), (input("How old are you?:"))
# Year = (100 - int(Age))
#
# print("You will be 100 years old in", Year, "years")
#
# # C to F
#
# C = (input("Write any C degrees:"))
# F = (int(C)*9/5)+32
#
# print('Your input in Celsius degrees Fahrenheit', F)


# homework-3

# 1: Positive and Negative numbers

# Number = input('Write any negative or positive number:')
#
# if (int(Number)) > 0:
#     print("Number is positive")
#
# if (int(Number)) < 0:
#     print("Number is negative")
#
# if (int(Number)) == 0:
#     print("Number is equal to zero")
#
#
# # 2: 10-is jeradi
#
# Number = input('Write any number:')
#
# Finalresult = (int(Number)) % 10
#
# if Finalresult == 0:
#     print("რიცხვი ბოლოვდება 0-ით")
# else:
#     print("რიცხვი არ ბოლოვდება 0-ით")
#
# # 3: >10 or <10
#
# Number = input('Write any number:')
#
# Number2 = input('Write any number:')
#
# if (int(Number)) > 10 and (int(Number2)) > 10:
#     print(((int(Number)) + (int(Number2))) / 2, 'არის პირველი და მეორე რიცხვის საშუალო არითმეტიკული')
# else:
#     print((int(Number)) * (int(Number2)), 'არის პირველი და მეორე რიცხვის ნამრავლი')
#
#
# # 4: 3 number programm
#
# Number = input('Write any number:')
#
# Number2 = input('Write any number:')
#
# Number3 = input('Write any number:')
#
# if (int(Number)) < (int(Number2)) and (int(Number)) < (int(Number3)):
#     print('Number 1 is lowest number')
#
# else:
#     if (int(Number2)) < (int(Number)) and (int(Number2)) < (int(Number3)):
#         print('Number 2 is lowest number')
#     else:
#         if (int(Number3)) < (int(Number)) and (int(Number3)) < (int(Number2)):
#             print('Number 3 is lowest number')
#
#
# # 5: Last digit of number
#
# Number = int(input('Write any number:'))
#
# print(Number % 10, "is last digit of number")

# Homework 4

#  ნაკიანი წლები
#
# Year = int(input('write any year:'))
#
# if not Year % 4 == 0 and not Year % 400 == 0 and not Year % 100 == 0:
#     print(Year, 'არ არის, ნაკიანი წელი')
# elif Year % 4 == 0 and not Year % 100 == 0 and not Year % 400 == 0:
#     print(Year, 'არის, ნაკიანი წელი')
# elif Year % 100 == 0 and Year % 4 == 0 and not Year % 400 == 0:
#     print(Year, 'არ არის, ნაკიანი წელი')
# elif Year % 100 == 0 and Year % 4 == 0 and Year % 400 == 0:
#     print(Year, 'არის, ნაკიანი წელი')


# Homework 5

# 1) 5 ის ჯერადები 20 - 125

print('5 ის ჯერადები 20 - 125')
print()
Number = 20

while Number <= 125:

    if Number % 5 == 0:
        print(Number)

    Number += 1

# 2) 8 ის ჯერადები 200 - 25

print()
print('8 ის ჯერადები 200 - 25')
print()

for i in range(200, 25, -1):

     if i % 8 == 0:
        print(i)


# 3) 1500 - 2100 5 ის და 7 ის ჯერადები

print()
print('1500 - 2100 5 ის და 7 ის ჯერადები')
print()

for i in range(1500, 2100, 1):

     if i % 7 == 0 and i % 5 == 0:
        print(i)

# 4) 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.

print()
print('1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.')
print()

Number = 0

for i in range(1500, 2100, 1):

     if i % 7 == 0 and i % 5 == 0:
        print(i)
        Number += i
print('ამ რიცხვების ჯამი არის', Number)


# 5) 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული ჯამი ეკრანზე.

print()
print('1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული ჯამი ეკრანზე.')
print()

Number = 0

for i in range(1500, 2100, 1):

     if i % 7 == 0 and i % 5 == 0:
        print(i)
        Number += i

     if Number > 20000:
        break

print('ამ რიცხვების ჯამი არის', Number)

# 6) დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.

print()
print('დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.')
print()

Number = 0

for i in range(1500, 2100, 1):

     if i % 5 == 0:
        print(i)
        Number += i

print('ამ რიცხვების ჯამი არის', Number)

# 7) შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.

print()
print('შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.')
print()

Number = 0

for i in range(0, 10):
    Number += int(input('input number:'))
print(Number/10)

# 8) დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.

print()
print('დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.')
print()

Number = 0

for i in range(1, 101):
    if i % 2 != 0:
        print(i)
    Number += i
print(Number)


# 9) დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue ოპერატორი.

print()
print('დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue ოპერატორი.')
print()

for i in range(14, 151, 1):

      if i % 5 == 0 and i == 50 or i == 75 or i == 80:
        continue
      elif i % 5 == 0:
          print(i)

# 10) შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ. მაგალითად 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5

print()
print('შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ. მაგალითად 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5')
print()

end = int(input('input number:'))
N = 1
Number = 1

for i in range(0, end):

    Number *= N
    N += 1

print(Number)



