def verify_anagrams(first_word, second_word):
    first_word = first_word.replace(" ", "")
    second_word = second_word.replace(" ", "")
    return (sorted(list(first_word.lower())) == sorted(list(second_word.lower())))
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

