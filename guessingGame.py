print('welcome to the guessing game ')

user_name = input('What is you name: ')
secret_number = '13'

print('hello',user_name)
print('guess the secret number from 1 to 15: ')

user_guess=input()

if user_guess == secret_number:
  print('Correct, you win!')
else:
  print('you loser, guess again')  

user_guess=input()
  
if user_guess == secret_number:
  print('Correct, you win!')
else:
  print('you loser, guess again') 
  
user_guess=input()    
  
if user_guess == secret_number:
  print('Correct, you win!')
else:
  print('you loser, guess again')  

print('game over,you lose')    

