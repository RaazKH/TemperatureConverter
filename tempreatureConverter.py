print('Welcome to the temperature converter!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
repeat = True
loops = 0

while repeat:
    print('\n')
    code = input('Enter the code:')
    
    valid = False
    while valid != True:
        try:
            temp= float(input('Enter the temperature in \N{DEGREE SIGN}' + 'C' + ':'))
            valid = True
        except ValueError:
            print('\nPlease enter a valid temperature!\n')

    print ('Would you like to make another calculation?')
    repeat = 'Y' in input().upper()
    loops += 1

print('\nGoodbye')
