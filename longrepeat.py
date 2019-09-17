def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    # your code here
    max_len = 0
    prev_item = None
    freq_char = 0
    for item in line:
        if item == prev_item:
            freq_char += 1
        elif item != prev_item and freq_char > max_len:
            max_len = freq_char
            freq_char = 1
        else:
            freq_char = 1
        prev_item = item    
    return max(max_len, freq_char)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
