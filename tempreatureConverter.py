def parseRep(userIN):
    userIN = userIN.upper()
    if 'Y' in userIN:
        return True
    return False

print('Welcome to the temperature converter!')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
repeat = True
loops = 0
while repeat:
    print ('\n')
    print ('enter the temp code')
    #if loops == 0:

    print ('Would you like to make another calculation?')
    repeat = parseRep(input())
    loops += 1

print('Goodbye')
