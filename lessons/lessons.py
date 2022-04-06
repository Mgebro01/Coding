Number = int(input('შეიყვანე მებისმირეი რიცხვი 0-100 :'))

if Number > 100 or Number < 0:
    print()
elif Number > 0 or Number < 40:
    print('Failed')
elif Number > 41 or Number < 50:
    print('Fx')
elif Number > 51 or Number < 60:
    print('E')
elif Number > 61 or Number < 70:
    print('D')
elif Number > 71 or Number < 80:
    print('C')
elif Number > 81 or Number < 90:
    print('B')
elif Number > 91 or Number < 100:
    print('A')