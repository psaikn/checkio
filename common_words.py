def checkio(first, second):
    split_first_words = first.split(",")
    split_second_words = second.split(",")
    return ",".join(sorted(set(split_first_words).intersection(set(split_second_words))))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
