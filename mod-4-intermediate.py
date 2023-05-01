 '''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def shift_letter(letter, shift):
    if letter == ' ' and letter_shift == '_':
        return ' '
    
    result = ord(letter) + shift
    while result > ord('Z'):
        result -= 26
    while result < ord('A'):
        result += 26
    return chr(result)
        
        

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def caesar_cipher(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_msg = ''
    for char in message:
        char = char.lower()
        if char != ' ':
            index = alphabet.find(char)
            print(index)
            if index == -1:
                new_msg += char
            else:
                new_shift = index + shift
                if new_shift >= 26:
                    new_shift -= 26
                new_msg += alphabet[new_shift]
        else: 
            new_msg += ' '
    return new_msg

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def shift_by_letter(letter, letter_shift):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    letters_values = [*range(0,27)]
    
    dictionary = dict(zip(letters,letters_values))
    shift = dictionary.get(letter_shift)
    print(shift)
    
    if letter == ' ' and letter_shift =='_':
        
    result = ord(letter) + shift
    while result > ord('Z'):
        result -= 26
    while result < ord('A'):
        result += 26
    return chr(result)
    
    
def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def vigenere_cipher(message, key):
    
    key = (key * (len(message) // len(key) + 1))[:len(message)]
  
    shifted_message = ""
    for i in range(len(message)):
        if message[i] == " ":
            shifted_message += " "
        else:
            if key[i] == " ":
                shifted_message += message[i]
            else:
                shift = alphabet.index(key[i])
                shifted_letter = shift_letter(message[i], shift)
                shifted_message += shifted_letter
            
    return shifted_message
     print("Vigenere cipher of message: " + shifted_message)