# # file = open('cursor.txt', 'r+')
# #
# # print(file.read())
# #
# # file.close()
#
# with open('cursor.txt', 'r') as file:
#     print(file.read())
#
# # file = open('cursor.txt', 'r')
# # print(file.read())
# # file.close()
#
#
# file = open('cursor.txt', 'r')
# #
# # text = file.read()
# #
# # print(text)
# # text += '\n' + input()
# # file.close()
# #
# # file = open('cursor.txt', 'w')
# # file.write(text)
# # file.close()
#
#
# file = open('cursor.txt', 'r')
#
# print(file.read())
# file.close()
#
# file = open('cursor.txt', 'a')
# file.write('\n' + input())
# file.close()

with open('cursor.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f'line {i}\n')
with open('cursor.txt', 'r') as f:
    # for i in range(1, 101):
    #     print(f.readline())
    for line in f:
        print(line[:-1])

print('gamarjoba seni asakia {}'.format(123))
