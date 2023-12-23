import random

num = random.randint(100,1000)

while True:
    a=int(input('enter a number:-'))
    if a == num:
        print('congrats! you successfully gussed the number',num)
        break
    elif a < num:
        print('enter greater number')
    elif a > num:
        print('enter lesser number')
