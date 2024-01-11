from random import *

word_list = ['time', 'year', 'people', 'way', 'day', 'man', 'thing', 'woman', 'life', 'child', 'world', 'school',
             'state', 'family', 'student', 'group', 'country', 'problem', 'hand', 'part', 'place', 'case', 'week',
             'company', 'system', 'program', 'question', 'work', 'government', 'number', 'night', 'point', 'home',
             'water', 'room', 'mother', 'area', 'money', 'story', 'fact', 'month', 'lot', 'right', 'study', 'book',
             'eye', 'job', 'word', 'business', 'issue', 'side', 'kind', 'head', 'house', 'service', 'friend', 'father',
             'power', 'hour', 'game', 'line', 'end', 'member', 'law', 'car', 'city', 'community', 'name', 'president',
             'team', 'minute', 'idea', 'kid', 'body', 'information', 'back', 'parent', 'face', 'others', 'level',
             'office', 'door', 'health', 'person', 'art', 'war', 'history', 'party', 'result', 'change', 'morning',
             'reason', 'research', 'girl', 'guy', 'moment', 'air', 'teacher', 'force', 'education']


def fool_check_yn(n):
    k = n.lower()
    while k != 'y' and k != 'n':
        print('Please, enter the valid letter (Y - yes, N - no)')
        k = input().lower()
    return k


def get_word(word):
    result = choice(word).upper()
    return result


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def fool_check_letter(n):
    k = n
    while not (k.isalpha() and len(k) == 1):
        print('Please, enter the letter that you think is in this word')
        k = input()
    return k


def fool_check_word(n):
    k = n
    while not (k.isalpha() and len(k) == len(your_word)):
        print('Please, enter the word that you think is hidden')
        k = input()
    return k.upper()


def fool_check_wl(n):
    k = n.lower()
    while k != 'w' and k != 'l':
        print('Please, choose what you want to enter: W for word, L for letter')
        k = input()
    return k


def check_written(option, lists):
    m = option
    while m in lists:
        print('You\'ve already tried this option! Try something new!')
        m = input()
    return m


def play(hidden):
    print('Let\'s play Hangman together! I make a word and you guess. You have 6 chances to make a mistake :)')
    tries = 6
    print(display_hangman(tries))
    word_completion = '_' * len(hidden)
    print(word_completion)
    guessed_letters = []
    guessed_words = []
    while word_completion != hidden and tries > 0:
        print('Do you want to enter the letter or the whole word? W / L')
        wl_enter = fool_check_wl(input())
        if wl_enter == 'w':
            print('Please enter the word that you think is hidden:')
            word = check_written(fool_check_word(input()).upper(), guessed_words)
            if word == hidden:
                print('Congratulations! You guessed the word!')
                print(hidden)
                print(display_hangman(tries))
                break
            else:
                print('Unfortunately, it\'s not the correct word')
                print(word_completion)
                tries -= 1
                print(display_hangman(tries))
                guessed_words.append(word)
        else:
            print('Please enter the letter that you think is in this word:')
            letter = check_written(fool_check_letter(input()).upper(), guessed_letters)
            save = []
            for g in range(len(hidden)):
                if letter == hidden[g]:
                    save.append(g)
            if save != []:
                print('Congratulations! You guessed the letter!')                     # TO FIX IF MORE THAN ONE LETTER IN WORD
                guessed_letters.append(letter)
                for d in save:
                    word_completion = word_completion[:d]+letter+word_completion[d+1:]
                print(word_completion)
                print(display_hangman(tries))
            else:
                print('Unfortunately, it\'s not the correct letter')
                print(word_completion)
                tries -= 1
                print(display_hangman(tries))
                guessed_letters.append(letter)


    else:
        if word_completion != hidden:
            print('Congratulations! You guessed the word!')
            print(hidden)
            print(display_hangman(tries))
        elif tries == 0:
            print(display_hangman(tries))
            print('Sorry, you lost! Try again later!', '\n', 'The hidden word was', hidden)


your_word = get_word(word_list)
play(your_word)

print('Do you want to play again? Y / N')
answer = fool_check_yn(input())
while answer == 'y':
    your_word = get_word(word_list)
    print(your_word)
    play(your_word)

print('Thanks for playing with me today! Come back any time to play again :)')
