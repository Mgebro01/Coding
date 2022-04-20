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

# print('5 ის ჯერადები 20 - 125')
# print()
# Number = 20
#
# while Number <= 125:
#
#     if Number % 5 == 0:
#         print(Number)
#
#     Number += 1
#
# input()
#
# # 2) 8 ის ჯერადები 200 - 25
#
# print()
# print('8 ის ჯერადები 200 - 25')
# print()
#
# for i in range(200, 25, -1):
#
#     if i % 8 == 0:
#         print(i)
#
# input()
#
# # 3) 1500 - 2100 5 ის და 7 ის ჯერადები
#
# print()
# print('1500 - 2100 5 ის და 7 ის ჯერადები')
# print()
#
# for i in range(1500, 2101, 1):
#
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#
# input()
#
# # 4) 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.
#
# print()
# print('1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.')
# print()
#
# Number = 0
#
# for i in range(1500, 2101, 1):
#
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#         Number += i
#
# print('ამ რიცხვების ჯამი არის', Number)
#
# input()
#
# # 5) 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული ჯამი ეკრანზე.
#
# print()
# print('1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული ჯამი ეკრანზე.')
# print()
#
# Number = 0
#
# for i in range(1500, 2101, 1):
#
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#         Number += i
#
#     if Number > 20000:
#         break
#
# print('ამ რიცხვების ჯამი არის', Number)
#
# input()
#
# # 6) დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.
#
# print()
# print('დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.')
# print()
#
# Number = 0
#
# for i in range(1500, 2101, 1):
#
#     if i % 5 == 0:
#         print(i)
#         Number += 1
#
# print('ამ რიცხვების რაოდენობა არის', Number)
#
# input()
#
# # 7) შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.
#
# print()
# print('შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.')
# print()
#
# Number = 0
#
# for i in range(0, 10):
#     Number += int(input('input number:'))
# print(Number/10)
#
# input()
#
# # 8) დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.
#
# print()
# print('დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.')
# print()
#
# Number = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)
#         Number += i
#
# print(Number)
#
# input()
#
# # 9) დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue ოპერატორი.
#
# print()
# print('დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue ოპერატორი.')
# print()
#
# for i in range(14, 150, 1):
#
#     if i % 5 == 0 and i == 50 or i == 75 or i == 80:
#         continue
#     elif i % 5 == 0:
#         print(i)
#
# input()
#
# 10) შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ. მაგალითად 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5
#
# print()
# print('შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ. მაგალითად 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5')
# print()
#
# # ვარიანტი 1
#
# end = int(input('input number:'))
# N = 1
# Number = 1
#
# for i in range(0, end):
#
#     Number *= N
#     N += 1
#
# print(Number)
#
# # ვარიანტი 2
#
# for i in range(0, end):
#
#     Number *= i
#
# print(Number)
#

# homework 6

# 1.შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.
#
# print()
# print("1.შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.")
# print()
#
# Number = int(input('input number:'))
#
# Number2 = int(input('input number:'))
# Low = Number2
#
#
# if Number < Number2:
#
#     Low = Number
#
# for i in range(Low, 0, -1):
#
#     if Number < 0 or Number2 < 0:
#         print('ეს რიცხვი 0-ზე ნაკლებია')
#         break
#
#     elif Number % i == 0 and Number2 % i == 0:
#         print(i)
#         break
#
#
# # შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.
#
# print()
# print('შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.')
# print()
#
# Number = int(input('input number:'))
#
# Number2 = int(input('input number:'))
#
# i = 0
#
# while True:
#     i += 1
#
#     if Number < 0 or Number2 < 0:
#         print('ეს რიცხვი 0-ზე ნაკლებია')
#         break
#
#     if i % Number == 0 and i % Number2 == 0:
#         print(i)
#         break
#
#
# # 3. შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით.
# # იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი და დაბეჭდეთ.
# # თუ კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.
#
# print()
# print('3. შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით. იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი და დაბეჭდეთ.თუ კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.')
# print()
#
# Number = 0
#
# N = 0
#
# for i in range(0, 10):
#
#     Number = int(input('input number:'))
#
#     if Number % 2 != 0 and Number > N:
#         N = Number
#
#
# if N == 0:
#     print('ამ რიცხვებში არ არის კენტი რიცხვი')
# else:
#     print(i)
#
#

#  1. დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.
print()
print('1. დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.')
print()

Number = 2

# N = 2

for i in range(2, 1001):
    if i % Number == 0:
        Number += 1
        continue
    else:
        print(i)
# ვერმივხვდი მას


# 2. დაბეჭდეთ 0-დან 100-მდე არსებული
# ფიბონაჩის რიცხვები (ფიბონაჩის რიცხვებია 1, 1, 2, 3, 5, 8, 13, ...).

print()
print('2. დაბეჭდეთ 0-დან 100-მდე არსებული ფიბონაჩის რიცხვები (ფიბონაჩის რიცხვებია 1, 1, 2, 3, 5, 8, 13, ...).')
print()

a = 0
b = 1


while a < 100:
    print(a)
    a = a + b
    print(b)
    b = a + b


#3. შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და ჯამი და დაბეჭდეთ.
print()
print('3. შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და ჯამი და დაბეჭდეთ.')
print()

Number = int(input('input number:'))
D = 0
i = 1
D1 = 0
D2 = 0
D3 = 0
O = 1

while i < Number:

    i *= 10
    D = Number % i - D1
    D1 = Number % i

    if D >= 10:
        O *= 10
        D = round(D / O)

    D3 += D
    D2 += 1

print("რაოდენობა არის", D2)
print("ჯამი არის", D3)

#მაას მთელი ღამე ვწვალობდი და მაინც რაათაც ბაგები აქვს
#
#
#
#5. შეიყვანეთ ნებისმიერი რიცხვი და დაბეჭდეთ ამ რიცხვის პირველი ციფრი.
print()
print('5. შეიყვანეთ ნებისმიერი რიცხვი და დაბეჭდეთ ამ რიცხვის პირველი ციფრი.')
print()

Number = int(input('input number:'))
D = 0
i = 1
D1 = 0
D3 = 0
O = 1

while i < Number:

    i *= 10
    D = Number % i - D1
    D1 = Number % i

    if D >= 10:
        O *= 10
        D = round(D / O)

    D3 = D

print(D3)


# მეექვსე ვერავიგე მას








