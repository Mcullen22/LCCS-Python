import random

number =  random.randint(1,10)
print(number)

counter = 0

while  counter < 3:
    
    guess = int(input('Enter a number between 1 and 10: '))
    if guess == number:
        print('Correct')
        break
    elif guess < number :
        print('Incorrect, Too low')
    else:
        print('Incorrect, Too high')
        
    counter = counter + 1
    
print('Goodbye')