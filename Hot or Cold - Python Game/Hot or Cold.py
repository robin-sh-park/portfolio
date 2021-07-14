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
            elif guess > 99 or guess < 1:                                   # if out of range, print error message
                print('Guess is out of range')
                guess_game_eng(limit)
                
                # if guess is too far from num
            elif limit < 14 and ((num < guess <= num + 5) or (num > guess >= num - 5)):
                print('Getting VERY HOT!')
                print(f'You have {limit} guess(es) left')
            elif limit < 14 and (guess > (num + 25) or guess < (num - 25)):
                print("That's TOO COLD!")
                print(f'You have {limit} guess(es) left')
                
                # if guess is getting closer/further compared to pre_value (previous guess)
            elif limit < 14 and ((pre_value < guess < num) or (num < guess < pre_value)):
                print('Getting Hotter!')
                print(f'You have {limit} guess(es) left')
            elif limit < 14 and ((guess < pre_value < num) or (num < pre_value < guess)):
                print('Getting Colder...')
                print(f'You have {limit} guess(es) left')
                
                # first hint after first input
            elif (num < guess < num + 10) or (num > guess > num - 10):
                print('HOT')
                print(f'You have {limit} guess(es) left')
            elif guess > (num + 20) or guess < (num - 20):
                print('COLD')
                print(f'You have {limit} guess(es) left')
            elif (num + 10 <= guess <= num + 20) or (num - 5 >= guess >= num - 20):
                print('Warm')
                print(f'You have {limit} guess(es) left')
                
            # after guess, put guess value into pre_value variable
            pre_value = guess
        else:                                               # if run out of tries, print 'Game Over' and the set random number
            print('Game Over!')
            print(f'The random number was {num}.')
    except ValueError:                                      # if input is not integer
        print('Only integers are allowed')
        guess_game_eng(limit)                               # after error message, ask again


def intro_eng():                                            # prints rules of game
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
            guess = int(input('숫자를 입력하세요: '))                  # 입력값을 가져온다
            limit -= 1                                               # 값을 입력할 때 마다 기회가 1씩 줄어든다
            if num == guess:
                print('☆★☆축하합니다, 게임에서 이겼습니다!☆★☆')       # 맞혔을 경우 문장 print 후 빠져나오기; try_again_kor()로 이동
                break
            elif guess > 99 or guess < 1:                               # 입력값이 1 ~ 99 범위를 벗어난 경우 다시 물어보기
                print('Guess is out of range')
                guess_game_kor(limit)
                
                # guess가 num과 많이 가까워진 경우 
            elif limit < 14 and ((num < guess <= num + 5) or (num > guess >= num - 5)):
                print('Getting VERY HOT!')
                print('많이 가까워졌어요!!')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
                
                # guess가 num과 너무 멀어진 경우 
            elif limit < 14 and (guess > (num + 25) or guess < (num - 25)):
                print("That's TOO COLD!")
                print("너무 멀어졌어요!!")
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
                
                # guess가 이전 값(pre_value) 보다 num에 더 가까워진 경우 
            elif limit < 14 and ((pre_value < guess < num) or (num < guess < pre_value)):
                print('Getting Hotter!')
                print('더 가까워졌어요!')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
                
                # guess가 이전 값(pre_value) 보다 num에 더 멀어진 경우 
            elif limit < 14 and ((guess < pre_value < num) or (num < pre_value < guess)):
                print('Getting Colder...')
                print('더 멀어졌어요...')
                print(" ")
                print(f'{limit}번의 기회가 있습니다.')
                
                # 첫 입력값 후 표시되는 값들 
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


def intro_kor():                                                    # 본 게임 시작 전 출력되는 문장; 게임 설명
    print('==================================================')
    print('숫자 맟히는 게임, "Hot or Cold"!')
    print('==================================================')
    print('숫자에 가까워지면 "HOT", 또는 "Hotter"가 나와요!')
    print('숫자에 멀어지면 "COLD", 또는 "Colder"가 나와요.')
    print('멀지 않고 가깝지 않으면 "Warm"이 출력됩니다.')
    print('-------------------------------------------------------------')
    print('1과 99사이 숫자를 랜덤으로 선택하고, 15 번의 숫자 맞힐 기회가 있습니다')
    guess_game_kor(15)                                              # 본 게임 function (guess_game_kor(기회 수))


def try_again_kor():                                                # 본 게임이 끝난 후, 이겼는지 졌는지 결과와 상관없이 출력되는 문장
    print('=====================================')
    again = input('게임 다시 하시겠습니까? (y/n) ')                    # 게임을 다시 하겠냐고 물어본다
    if again.lower() == 'y':                      
        welcome()                                                   # y 일 경우 welcome() 부터 다시 시작
    elif again.lower() == 'n':
        print('Thanks for playing! Goodbye!')                       # n 일 경우 문장 출력 후 종료
    else:
        print('입력을 잘못하셨습니다.')                                # 그 외 값이 입력되면 오류 메세지 표시 후 다시 질문
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
