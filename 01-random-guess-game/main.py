import random
import time

print('Welcome to Random Guess Game. I \'ll pick a number between 1-50, then you guess ')

time.sleep(2)
print('picking a number for you ...')
time.sleep(2)

guess = int(input('Enter your guess number: '))
correct_num = random.randint(1,50)
guess_count= 1

while guess !=correct_num :
    time.sleep(2)
    guess_count += 1  
    if guess < correct_num:
       guess = int(input('Wrong, You need to guess higher, Enter new guess: ')) 
    else:
        guess = int(input('Wrong, You need to guess lower, Enter new guess: ')) 

print(f"Congrats! You entered {correct_num} which is correct. It took you {guess_count} guesses. ")
