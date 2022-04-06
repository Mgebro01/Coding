Number = int(input('შეიყვანე მებისმირეი რიცხვი 0-100 :'))

if Number > 100 and Number < 0:
    print()
elif Number >= 0 and Number <= 40:
    print('Failed')
elif Number >= 41 and Number <= 50:
    print('Fx')
elif Number >= 51 and Number <= 60:
    print('E')
elif Number >= 61 and Number <= 70:
    print('D')
elif Number >=71 and Number <= 80:
    print('C')
elif Number >= 81 and Number <= 90:
    print('B')
elif Number >= 91 and Number <= 100:
    print('A')