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

Number = input('Write any negative or positive number:')

if (int(Number)) > 0:
    print("Number is positive")

if (int(Number)) < 0:
    print("Number is negative")

if (int(Number)) == 0:
    print("Number is equal to zero")


# 2: 10-is jeradi

Number = input('Write any number:')

Finalresult = (int(Number)) % 10

if Finalresult == 0:
    print("რიცხვი ბოლოვდება 0-ით")
else:
    print("რიცხვი არ ბოლოვდება 0-ით")

# 3: >10 or <10

Number = input('Write any number:')

Number2 = input('Write any number:')

if (int(Number)) > 10 and (int(Number2)) > 10:
    print(((int(Number)) + (int(Number2))) / 2, 'არის პირველი და მეორე რიცხვის საშუალო არითმეტიკული')
else:
    print((int(Number)) * (int(Number2)), 'არის პირველი და მეორე რიცხვის ნამრავლი')


# 4: 3 number programm

Number = input('Write any number:')

Number2 = input('Write any number:')

Number3 = input('Write any number:')

if (int(Number)) < (int(Number2)) and (int(Number)) < (int(Number3)):
    print('Number 1 is lowest number')

else:
    if (int(Number2)) < (int(Number)) and (int(Number2)) < (int(Number3)):
        print('Number 2 is lowest number')
    else:
        if (int(Number3)) < (int(Number)) and (int(Number3)) < (int(Number2)):
            print('Number 3 is lowest number')


# 5: Last digit of number

Number = int(input('Write any number:'))

print(Number % 10, "is last digit of number")

