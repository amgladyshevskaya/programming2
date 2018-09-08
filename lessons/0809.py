#прописные буквы англ яз
import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alph = [ i for i in alphabet]
letter = random.choice(alph)
index = alph.index(letter)+1
while 1:
    guess = input('введите букву английского алфавита')
    if guess == letter:
        print('вы угадали!')
        break
    elif guess != letter:
        index_guess = alph.index(guess)+1
        if index_guess < index:
            print('загаданная буква правее')
            continue
        else:
            print('загаданная буква левее')
            continue
    else:
        print('Это не буква, попробуйте снова')
        continue
        
