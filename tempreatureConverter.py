print('Welcome to the temperature converter!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('Conversion input example:
    \n\"cf\" = Celsius to Fahrenheit
    \n\"kf\" = Kelvin to Fahrenheit')

repeat = True
loops = 0

while repeat:
    print('\n')
    code = input('Conversion:').tolower()
    

    if   ('cf' in code):
        partA = '\N{DEGREE SIGN}C'
        partB = '\N{DEGREE SIGN}F'
    elif ('ck' in code):
        partA = '\N{DEGREE SIGN}C'
        partB = 'K'
    elif ('kf' in code):
        partA = 'K'
        partB = '\N{DEGREE SIGN}F'
    elif ('kc' in code):
        partA = 'K'
        partB = '\N{DEGREE SIGN}C'
    elif ('fc' in code):
        partA = 'K'
        partB = '\N{DEGREE SIGN}F'
    elif ('fk' in code):
        partA = 'K'
        partB = '\N{DEGREE SIGN}C'
        
    valid = False
    while valid != True:
        try:
            temp= float(input('Enter the temperature in ' + partA + ':'))
            valid = True
        except ValueError:
            print('\nInvalid temperature!!!\n')

    
    print ('Would you like to make another calculation?')
    repeat = 'Y' in input().upper()
    loops += 1

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('\nGoodbye')
