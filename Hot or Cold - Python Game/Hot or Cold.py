import random

# initial value is set to zero(0)
pre_value = 0


# ENGLISH VERSION/영어 버전
def guess_game_eng(limit):
    global pre_value                                                        # take pre_value

    num = random.randint(1, 99)
    try:
        while limit > 0:
            print('-------------------------------')
            guess = int(input('What is your guess? '))                      # asks for user input 
            limit -= 1
            if num == guess:                                                # if guessed correctly, exit guess_game_eng(); go to try_again_eng()   
                print('☆★☆Congratulations, you won!☆★☆')
                break
            elif guess > 99 or guess < 1:
                print('Guess is out of range')
                guess_game_eng(limit)
            elif limit < 14 and ((num < guess <= num + 5) or (num > guess >= num - 5)):
                print('Getting VERY HOT!')
                print(f'You have {limit} guess(es) left')
            elif limit < 14 and (guess > (num + 25) or guess < (num - 25)):
                print("That's TOO COLD!")
                print(f'You have {limit} guess(es) left')
            elif limit < 14 and ((pre_value < guess < num) or (num < guess < pre_value)):
                print('Getting Hotter!')
                print(f'You have {limit} guess(es) left')
            elif limit < 14 and ((guess < pre_value < num) or (num < pre_value < guess)):
                print('Getting Colder...')
                print(f'You have {limit} guess(es) left')
            elif (num < guess < num + 10) or (num > guess > num - 10):
                print('HOT')
                print(f'You have {limit} guess(es) left')
            elif guess > (num + 20) or guess < (num - 20):
                print('COLD')
                print(f'You have {limit} guess(es) left')
            elif (num + 10 <= guess <= num + 20) or (num - 5 >= guess >= num - 20):
                print('Warm')
                print(f'You have {limit} guess(es) left')
            pre_value = guess
        else:
            print('Game Over!')
            print(f'The random number was {num}.')
    except ValueError:                                      # if input is not integer
        print('Only integers are allowed')
        guess_game_eng(limit)                               # after error message, ask again


def intro_eng():
    print('==================================================')
    print('Welcome to "Hot or Cold", a number guessing game!')
    print('==================================================')
    print('If you are close to the number, you get "HOT"!')
    print('If you are too far from the number, you get "COLD".')
    print("If you're somewhere in between, you get 'Warm'.")
    print('----------------------------------------------------------------')
    print('We will pick a number between 1 and 99, and you have 15 guesses!')
    guess_game_eng(15)


def try_again_eng():                                        # last function (regardless of winning/losing)
    print('===================================')
    again = input('Do you want to play again? (y/n) ')      # asks for user input if they want to play again
    if again.lower() == 'y':                                
        welcome()                                           # if y, replay game from welcome()
    elif again.lower() == 'n':
        print('Thanks for playing! Goodbye!')               # if n, end game after message
    else:
        print('Wrong input')                                # if other input, print error message and ask again
        try_again_eng()


# KOREAN VERSION/한국어 버전

def guess_game_kor(limit):
    global pre_value                                        # 외부에 있는 pre_value 값을 가져온다

    num = random.randint(1, 99)
    try:
        while limit > 0:
            print('-------------------------------')
            guess = int(input('숫자를 입력하세요: '))
            limit -= 1
            if num == guess:
                print('☆★☆축하합니다, 게임에서 이겼습니다!☆★☆')
                break
            elif guess > 99 or guess < 1:
                print('Guess is out of range')
                guess_game_kor(limit)
            elif limit < 14 and ((num < guess <= num + 5) or (num > guess >= num - 5)):
                print('Getting VERY HOT!')
                print('많이 가까워졌어요!!')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
            elif limit < 14 and (guess > (num + 25) or guess < (num - 25)):
                print("That's TOO COLD!")
                print("너무 멀어졌어요!!")
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
            elif limit < 14 and ((pre_value < guess < num) or (num < guess < pre_value)):
                print('Getting Hotter!')
                print('더 가까워졌어요!')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
            elif limit < 14 and ((guess < pre_value < num) or (num < pre_value < guess)):
                print('Getting Colder...')
                print('더 멀어졌어요...')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
            elif (num < guess < num + 10) or (num > guess > num - 10):
                print('HOT')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
            elif guess > (num + 20) or guess < (num - 20):
                print('COLD')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
            elif (num + 10 <= guess <= num + 20) or (num - 5 >= guess >= num - 20):
                print('Warm')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
            pre_value = guess
        else:
            print('기회가 더이상 없습니다...ㅠ_ㅠ')
            print(f'정답은 {num}였습니다.')
    except ValueError:
        print('숫자만 입력해주세요')
        guess_game_kor(limit)


def intro_kor():
    print('==================================================')
    print('숫자 맟히는 게임, "Hot or Cold"!')
    print('==================================================')
    print('숫자에 가까워지면 "HOT", 또는 "Hotter"가 나와요!')
    print('숫자에 멀어지면 "COLD", 또는 "Colder"가 나와요.')
    print('멀지 않고 가깝지 않으면 "Warm"이 출력됩니다.')
    print('-------------------------------------------------------------')
    print('1과 99사이 숫자를 랜덤으로 선택하고, 15 번의 숫자 맞힐 기회가 있습니다')
    guess_game_kor(15)


def try_again_kor():
    print('=====================================')
    again = input('게임 다시 하시겠습니까? (y/n) ')
    if again.lower() == 'y':
        welcome()
    elif again.lower() == 'n':
        print('Thanks for playing! Goodbye!')
    else:
        print('입력을 잘못하셨습니다.')
        try_again_kor()


# WELCOME SCREEN/MESSAGE
def welcome():
    print('==================================================')
    print('Welcome!')
    language = input('Select language/언어를 선택하세요(eng/kor): ')
    if language.upper() == "ENG":
        intro_eng()
        try_again_eng()
    elif language.upper() == "KOR":
        intro_kor()
        try_again_kor()
    else:
        print('Wrong input')
        welcome()


# start game
welcome()
