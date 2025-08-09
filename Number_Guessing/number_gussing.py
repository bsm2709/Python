import random
import time
print('Hello Player! Welcome to the game')
print('Rules:')
print('1. You have to guess the number between 1 and 10')
print('2. You have 4 chances to guess the number')
print('3. If you guess the number in 4 chances, you win the game')
print('4. If you don\'t guess the number in 4 chances, you lose the game')


time.sleep(2)
n = random.randint(1, 10)
count = 4
print('Number has been generated!')


while count!=0:
    a = int(input('Guess the number: '))

    if a == n:
        print("Yay! That's right. You won!")
        break
    elif a > n:
        print('The number is less than ', a)
    else:
        print('The number is greater than ', a)
    count=-1


print (count)