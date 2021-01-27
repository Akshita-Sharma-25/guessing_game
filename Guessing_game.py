from random import randint
#getting a random number
num=randint(1,100)
#Rules
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
# list to store the guesses
guesses=[]
# to check whether the guess is correct or not
while True:
    guess=int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    if guess in range(1,101):
        guesses.append(guess)
        break
    else:
        print('OUT OF BOUNDS! Please try again: ')
# To compare the number with the guess and find if the user has guessed it or not correctly
while True:
    if len(guesses)==1:
        if guesses[0]==num:
            print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
            break
        elif abs(num-guesses[0])<=10:
            print('WARM!')
        elif abs(num-guesses[0])>10:
            print('COLD!')
    else:
        if guesses[-1]==num:
            print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
            break
        elif abs(num-guesses[-1])<abs(num-guesses[-2]):
            print('WARMER!')
        elif abs(num-guesses[-1])>abs(num-guesses[-2]):
            print('COLDER!')
    guess=int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    guesses.append(guess)