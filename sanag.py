import random
options=['rock','paper','scissor']
scores={'user':0,'computer':0}

def game_result():
    if scores['user']>scores['computer']:
        print(" you win ")
    if scores['user']<scores['computer']:
        print("Computer win ")    
    if scores['user']==scores['computer']:
        print("Equal")


for i in range(10):
    computer_choice=random.choice(options)
    user_choice=input('Play the game=')
    if user_choice=='rock' and computer_choice=='paper':
        print('Computer is wins')
        scores['computer']+=1
    elif  user_choice=="paper" and computer_choice=="scissor":
         print('Computer is wins')
         scores['computer']+=1
    elif  user_choice=="scissor" and computer_choice=="rock":
         print('Computer is wins')
         scores['computer']+=1

    elif user_choice=='rock' and computer_choice=='sscissor':
        print('You win')
        scores['user']+=1
    elif user_choice=="paper" and computer_choice=="rock":
        print('You win')
        scores['user']+=1
   
    elif user_choice=="scissor" and computer_choice=="paper":
        print('You win')
        scores['user']+=1

        print('pc scores is=',scores['computer'],'user scores is=',scores['user'])

game_result()

 
