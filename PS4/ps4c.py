# Problem Set 4C
# Name: llewellyndm
# Collaborators:
# Time Spent: x:xx

# =============================================================================
# Implementing a substitution cypher using vowels i.e. each vowel in the original
# message is replaced with another e.g. all the a's become o's.
# =============================================================================

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
wordList = load_words(WORDLIST_FILENAME)

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = wordList
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict = {}
        vowel_index = 0
        for vowel in VOWELS_LOWER:
            transpose_dict[vowel] = vowels_permutation[vowel_index]
            vowel_index += 1
        cap_vowel_index = 0
        for cap_vowel in VOWELS_UPPER:
            transpose_dict[cap_vowel] = vowels_permutation[cap_vowel_index].upper()
            cap_vowel_index += 1
        for cons in (CONSONANTS_LOWER+CONSONANTS_UPPER):
            transpose_dict[cons] = cons
        return transpose_dict

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message = []
        for char in self.message_text:
            if char in string.ascii_letters:
                encrypted_message.append(transpose_dict[char])
            else:
                encrypted_message.append(char)
        return ''.join(encrypted_message)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        vowels_permutation = get_permutations(VOWELS_LOWER)
        list_valid_word_count = []
        final_decryption = self.message_text
        for perm in vowels_permutation:           
            number_of_valid_words = 0
            decrypted_message_as_list = []
            transpose_dict = self.build_transpose_dict(perm)
            # here the message is decrypted according to each permutation, and then
            # this list of words is checked for any valid ones.
            for char in self.message_text:
                if char in string.ascii_letters:
                    decrypted_message_as_list.append(transpose_dict[char])
                else:
                    decrypted_message_as_list.append(char)
            decrypted_string = ''.join(decrypted_message_as_list)
            decrypted_words = decrypted_string.split() #creates a list of the decrypted words
            for word in decrypted_words:
                if is_word(wordList, word):
                    number_of_valid_words += 1
            list_valid_word_count.append(number_of_valid_words)
            if number_of_valid_words == max(list_valid_word_count): #this means each decrypted word is a real one
                final_decryption = decrypted_string
        return final_decryption
    

if __name__ == '__main__':

    # Example test case
    print('\nTEST 1 ---------------------')
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    print('\nTEST 2 ---------------------')
    m = SubMessage('Pineapple')
    p = 'iaoue'
    e = m.build_transpose_dict(p)
    print("Original message:", m.get_message_text(), "Permutation:", p)
    print("Expected encryption:", "Ponaippla")
    print("Actual encryption:", m.apply_transpose(e))
    e_m = EncryptedSubMessage(m.apply_transpose(e))
    print("Decrypted message:", e_m.decrypt_message())
    
    print('\nTEST 3 ---------------------')
    m2 = SubMessage('FaCeTiOuS')
    p2 = 'oiuea'
    e2 = m2.build_transpose_dict(p2)
    print("Original message:", m2.get_message_text(), "Permutation:", p2)
    print("Expected encryption:", "FoCiTuEaS")
    print("Actual encryption:", m2.apply_transpose(e2))
    e_m2 = EncryptedSubMessage(m2.apply_transpose(e2))
    print("Decrypted message:", e_m2.decrypt_message())
