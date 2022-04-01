# Homework 1

# print(9-3, 8*2.5, 9/2, 9/-2, 9%2, 9**2)
# print(4-2**3+5*2-3/2)
# print((3+245)*4-3**4)
# print((42+3*3)/(2+4))



# Homework 2

# 1-What's up, Tim

message = "What's up, Tim?"
print(message)

# 2-A and B reverse

a = 1
b = 4
a, b = b, a
print('a', a, 'b', b)

# 3- Name and last name

Name = input("What's your name?:")
lastname = input("What's your last name?:")

print('you are', Name, lastname)

# 4- Salary per month

Salaryperhour = input('How much do you earn per hour?:')
Workingtime = input('How long do you work a month?:')
Answer = int(Salaryperhour) * int(Workingtime)

print('You earn', Answer, '$ per month')


# 5- საშუალო არითმეტიკული

a = input("write any number:")
b = input("write any number:")
c = input("write any number:")

Answer = ((int(a)+int(b)+int(c))/3)
print(Answer)

# 6- How many years to 100 years

Name, Age = (input("What's your name?:")), (input("How old are you?:"))
Year = (100 - int(Age))

print("You will be 100 years old in", Year, "years")

# C to F

C = (input("Write any C degrees")),
F = (int(C)*9/5)+32

print('Your input in Celsius degrees Fahrenheit', F)