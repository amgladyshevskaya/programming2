import re
import random
hangman = ['''

  
     
      
      
      
      
=========''','''

  
    
      
      
      
      |
=========''','''

  
      
      
      |
      |
      |
=========''','''

      +
      |
      |
      |
      |
      |
=========''','''

  +---+
      |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def theme_choice():      #Функция просит игрока выбрать одну из трех тем
    print('Выберите тему: \n1. Фамилии известных футболистов\n2. Фамилии известных режиссеров\n3. Города Германии')
    choice = input('Укажите цифру выбранной темы: ')
    while choice != '1' and choice != '2' and choice != '3':
        print('Выбранная тема не существует')
        choice = input('Выберите одну из трех тем: ')
    return choice
def open_file(choice): #Функция читает файл с выбранной игроком темой и создает списки слов из файлов
    if choice == '1':
        with open('football.txt', encoding='utf-8') as f:
            words = f.read().split('\n')
            
    elif choice == '2':
        with open('film.txt', encoding='utf-8') as f:
            words = f.read().split('\n')
    elif choice == '3':
        with open('germany.txt', encoding='utf-8') as f:
            words = f.read().split('\n')
    return words

def random_word(words): #Функция выбирает случайное слово из списка
    wordid = random.randint(0, len(words) - 1)
    rand_word = words[wordid]
    return rand_word

def game(hangman, rand_word):
    i = 0
    print(hangman[i])
    x = len(rand_word)
    n = 10
    print('У вас есть ',n,' попыток, чтобы угадать слово из ',x,' букв.' )
    blanks = '_ '*x
    print(blanks)
    already_tried = []
    while n >= 0:
        guess = input('Введите букву: ').lower()
        if guess in already_tried:
            print('Вы уже вводили эту букву. Попробуйте другую.')
        elif guess not in 'йцукенгшщзхъфывапролджэёячсмитьбю':
            print('Введите букву кириллицы.')
        elif guess not in rand_word:
            print('Такой буквы в слове нет.')
            n-=1
            i+=1
        else:
            k = 0
            for l in rand_word:
                if guess == l:
                    blanks[k] == guess
                    blanks = blanks[:1]+guess + blanks[i+1]
                else:
                    k+=1
        print(hangman[i])
        print(blanks)
        already_tried.append(guess)

                    
def main(blanks):
    print(rand_word)
    print(blanks)
    

if __name__ == '__main__':
    main(game(hangman,(random_word(open_file(theme_choice())))))
    
    
