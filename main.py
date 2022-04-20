import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel", "alcameno", "the dark knight"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

word = []
flag = True
lives = 6

for i in range(len(chosen_word)):
    if chosen_word[i] == " ":
        word.append(' ')
    else:
        word.append('_')
print(word)
print(stages[6])
while flag == True:
    inList = False
    guess = input("Guess a letter: ").lower()
    print("")

    for z in range(len(chosen_word)):
        if guess == chosen_word[z]:
            word[z] = guess
            inList = True

    if inList == False:
        lives -= 1
        print("Wrong letter :(")
        print(stages[lives])

    print(word)

    if '_' not in word:
        print("Whoaao Whoaao Whoaaoooo, You Won ")
        flag = False
        break

    if lives == 0:
        print("You Lost :(")
        flag = False
        break











