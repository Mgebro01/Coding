# Number = int(input('შეიყვანე მებისმირეი რიცხვი 0-100 :'))
#
# if Number > 100 and Number < 0:
#     print('wrong number')
# elif Number >= 0 and Number <= 40:
#     print('Failed')
# elif Number >= 41 and Number <= 50:
#     print('Fx')
# elif Number >= 51 and Number <= 60:
#     print('E')
# elif Number >= 61 and Number <= 70:
#     print('D')
# elif Number >=71 and Number <= 80:
#     print('C')
# elif Number >= 81 and Number <= 90:
#     print('B')
# elif Number >= 91 and Number <= 100:
#     print('A')
#
#

# #  ნაკიანი წლები
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

#
#
# string = input('input string:')
#
# print(len(string))
# #
# #
# #
# string = input('input string:')
#
# string2 = input('input string:')
#
# string3 = string + string2
#
# print(string3)
# #
# #
# string = input('input string:')
#
# count = 0
#
# for i in range(0, len(string)):
#     if "a" == string[i]:
#         count += 1
#
# print(count)
#
# #
#
#
#
string = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
string2 = ''
count = 0
for i in range(0, 20):
    if "ს" == string[i]:
        count += 1
    string2 += string[i]

print(count)
print(string2)
#
#
#
#
text = 'Hello, this is example of string. Please, write this text and do some exercises'
count = 0
for i in range(len(text)):
    if " " in text[i]:
        count += 1
count += 1
print(count)
#
#
#
#
#
#
text = 'Have a nice day.'
i = len(text)

while i > 0:
    i -= 1
    print(text[i])
#
#
#
#
text = input('input string')
count = 0
for i in range(0, len(text)):
    if text[i] in 'AaEeIiOoUu':
        count += 1

print(count)
#
#
#
#
#
#
n = str(input('input number:'))
print(len(n))
#
#
#
#
#
name = input('input name:')
surename = input('input surename:')
email = name + surename + '@gmail.com'
print(email)
#
#
#
#
#
#
#
text = input('input text')







