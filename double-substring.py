from collections import Counter
def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    hash_obj = {}
    for index, key in enumerate(line):
        line_substr = line[index:]
        i = 0
        while i < len(line_substr):
            cnt = line_substr.count(line_substr[:i+1])
            if (not len(line_substr[:i+1]) in hash_obj) or (hash_obj[len(line_substr[:i+1])] < cnt):
                hash_obj[len(line_substr[:i+1])] = cnt
            i = i + 1
    filtered_dict = dict(filter(lambda x: x[1] > 1, hash_obj.items()))
    return max(filtered_dict.keys()) if filtered_dict else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
