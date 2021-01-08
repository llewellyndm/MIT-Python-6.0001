# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    correct = 0
    for letter in secret_word:
        if letter in letters_guessed:
            correct += 1
    if correct == len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    list1 = []
    for letter in secret_word:
        if letter in letters_guessed:
            list1.append(letter + ' ')
        else:
            list1.append('_ ')
    return ''.join(list1)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    list2 = []
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            list2.append(letter)
    return ''.join(list2)        
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    '''
    print('---------------')
    print('Welcome to Hangman!')
    
    # the following if/elif statement is only to ensure correct grammar (using 'a' or 'an')
    if len(secret_word) == 8:
        print('I am thinking of an', len(secret_word), 'letter word:', '_ '*8)
    else:
        print('I am thinking of a', len(secret_word), 'letter word:',
              '_ '*len(secret_word))
    print('You have 6 lives. Each time you guess an incorrect letter, you lose a life.')
    print('If you lose all 6 lives, the game is over.')
    print('---------------')
    letters_guessed = []
    warnings = 3
    lives_remaining = 6
    
    while not is_word_guessed(secret_word, letters_guessed):
        print('You have', lives_remaining, 'lives remaining.')
        print('Letters available:', get_available_letters(letters_guessed))
        print('---------------')
        guess = str.lower(input('Guess a letter: '))
        
        while (len(guess) != 1 or guess not in string.ascii_lowercase or 
               guess in letters_guessed): #invalid guess made by user
            warnings -= 1
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print('Your guess needs to be a letter!')
            elif guess in letters_guessed:
                print('That letter has already been guessed.')
            if warnings == 0:
                warnings = 3
                lives_remaining -= 1
                print('You have entered 3 invalid guesses. You lose a life.')
                if lives_remaining == 0:
                    print('You have no lives left. You lose.')
                    return None
                print('You now have', lives_remaining, 'lives.')
            print('You have', warnings, 'warnings remaining until you lose a life.')
            print('---------------')
            guess = str.lower(input('Guess a letter: '))
            
        letters_guessed.append(guess)
        if guess not in secret_word:
            lives_remaining -= 1
            print('Unlucky... That letter is not in my word:', 
                  get_guessed_word(secret_word, letters_guessed))
            if lives_remaining == 0:
                print('Oh no! You\'ve run out of guesses...')
                print('My word was', secret_word)
                return None
        elif guess in secret_word:
            print('Good guess! That letter is in my word:', 
                  get_guessed_word(secret_word, letters_guessed))
            
    print('Well done, you\'ve guessed my word! It was', secret_word)
    unique_letters = []
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    score = lives_remaining*len(unique_letters)
    print('Score:', score)
        
            
    ...



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] in string.ascii_lowercase and my_word[i] != other_word[i]:
                return False
        elif my_word[i] == '_' and other_word[i] in my_word:
                return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)
    if len(matches) == 0:
        print('No matches found')
    else:
        print(' '.join(matches))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('---------------')
    print('Welcome to Hangman with Hints!')
    if len(secret_word) == 8:
        print('I am thinking of an', len(secret_word), 'letter word:', '_ '*8)
    else:
        print('I am thinking of a', len(secret_word), 'letter word:',
              '_ '*len(secret_word))
    print('You have 6 lives. Each time you guess an incorrect letter, you lose a life.')
    print('If you lose all 6 lives, the game is over.')
    print('Enter the special character * to see words that match the letters',\
          'that you have already guessed.')
    print('---------------')
    
    letters_guessed = []
    warnings = 3
    lives_remaining = 6
    
    while not is_word_guessed(secret_word, letters_guessed):
        print('You have', lives_remaining, 'lives remaining.')
        print('Letters available:', get_available_letters(letters_guessed))
        print('---------------')
        guess = str.lower(input('Guess a letter: '))
        
        while (len(guess) != 1 or guess not in string.ascii_lowercase or 
               guess in letters_guessed):
            if guess == '*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                guess = str.lower(input('Guess a letter: '))
                continue
            warnings -= 1
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print('Your guess needs to be a letter!')
            elif guess in letters_guessed:
                print('That letter has already been guessed.')
            if warnings == 0:
                warnings = 3
                lives_remaining -= 1
                print('You have entered 3 invalid guesses. You lose a life.')
                if lives_remaining == 0:
                    print('You have no lives left. You lose.')
                    return None
                print('You now have', lives_remaining, 'lives.')
            print('You have', warnings, 'warnings remaining until you lose a life.')
            print('---------------')
            guess = str.lower(input('Guess a letter: '))
            
        letters_guessed.append(guess)
        if guess not in secret_word:
            lives_remaining -= 1
            print('Unlucky... That letter is not in my word:', 
                  get_guessed_word(secret_word, letters_guessed))
            if lives_remaining == 0:
                print('Oh no! You\'ve run out of guesses...')
                print('My word was', secret_word)
                return None
        elif guess in secret_word:
            print('Good guess! That letter is in my word:', 
                  get_guessed_word(secret_word, letters_guessed))
            
    print('Well done, you\'ve guessed my word! It was', secret_word)
    unique_letters = []
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    score = lives_remaining*len(unique_letters)
    print('Score:', score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
