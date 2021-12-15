name = input('Please type your name ')
print('welcome ', name, ' this adventure')

answer = input('choose your way, Left or Right ').lower()

if answer == 'left':
    answer = input('River. walk or swim ? ').lower()
    if answer == 'swim':
        print('You swam and got eaten by crocodile and lost')
    elif answer == 'walk':
        print('You walked many miles and ran out of water and lost ')
    else:
        print('Not valid, you loose')
elif answer == 'right':
    answer = input('Bridge.Cross or walk back? ').lower()
    if answer == 'cross':
        print('bridge broke, you fell and lost ')
    elif answer == 'back':
        print('You are saved ')
    else:
        print('Not valid, you loose ')
else:
    print('Not a valid option')
