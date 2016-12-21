def is_pangram(sentence):
    """ Check if sentence has all letters of the alphabet """
    alphabet = 'abcdefghijklmnopqrstvxyz'
    return all(letter in sentence.lower() for letter in alphabet)
