# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    
    # removing any whitespace character present in the word/string
    formatted_word = ''.join(word.split(' '))
    formatted_anagram = ''.join(anagram.split(' '))

    # comparing the word and second string to determine if they are anagrams
    if len(formatted_word) == len(formatted_anagram):
        if sorted(formatted_word) == sorted(formatted_anagram):
            return True
        else:
            return False
    else:
        return False
