def fahrenheit(temp):
    print('%.2f\N{DEGREE SIGN}F' % temp)
    temp = (temp - 32) * (5.0 / 9.0)
    print('%.2f\N{DEGREE SIGN}C' % temp)
    print('%.2fK' % (temp + 273.15))
    return

def celsius(temp):
    print('%.2f\N{DEGREE SIGN}C' % temp)
    print('%.2f\N{DEGREE SIGN}F' % (temp * ((5.0 / 9.0)) + 32))
    print('%.2fK' % (temp + 273.15))
    return

def kelvin(temp):
    print('%.2fK' % temp)
    temp -= 273.15
    print('%.2f\N{DEGREE SIGN}C' % temp)
    print('%.2f\N{DEGREE SIGN}F' % (temp * ((5.0 / 9.0)) + 32))
    return

print('Welcome to the temperature converter!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

repeat = True
while repeat:    
    valid = False
    while valid != True:
        valid = True
        code = input('\nConvert from: ').lower()
        if   ('c' in code):
            code = '\N{DEGREE SIGN}C'
        elif ('k' in code):
            code = 'K'
        elif ('f' in code):
            code = '\N{DEGREE SIGN}F'
        else:
            print('\nInvalid input!\n')
            valid = False
        
    valid = False
    while valid != True:
        try:
            temp= float(input('Enter the temperature in ' + code + ': '))
            valid = True
        except ValueError:
            print('\nInvalid temperature!!!\n')
            
    print()
    if  ('C' in code):
        celsius(temp)
    elif('F' in code):
        fahrenheit(temp)
    else:
        kelvin(temp)
    
    repeat = 'Y' in input('\nWould you like to make another calculation?\n').upper()
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
print('               Goodbye')
