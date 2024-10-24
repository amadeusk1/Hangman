import random

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(HANGMAN[2])

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
#65 words
chosenword = words[random.randrange(0,64)]
print(chosenword)
i = 0
g = 0
wordguessed = False
wordsalreadyguessed = []
print(len(chosenword))


while not wordguessed and i < 7 and g <=len(chosenword):
    print(HANGMAN[i])
    userguess = "6"
    print()
    print("letters that you've already used:",wordsalreadyguessed)

    while not userguess.isalpha():
        print("Please enter a letter")
        userguess = input("Choose a letter: ")

    while userguess in wordsalreadyguessed:
        print("You've already chosen this letter")
        userguess = input("Choose a letter: ")

    if userguess in chosenword:
        print("CORRECT GUESS")
        g += 1
    else:
        print("INCCORECT GUESS")
        i += 1
    wordsalreadyguessed.append(userguess)

print("GAME OVER")