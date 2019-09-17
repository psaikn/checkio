VOWELS = "aeiouy"

def translate(phrase):
    items = []
    consecutive = 0
    for index, chr_ in enumerate(phrase):
        if chr_ not in VOWELS:
            if len(items):
                if phrase[index-1] == chr_:
                    continue;
            items.append(chr_)
        else:
            if len(items):
                if phrase[index] == items[-1]:
                    if consecutive >= 3:
                        items.append(chr_)
                        consecutive = 1
                        continue
                    else:
                        consecutive += 1
                        continue
                elif phrase[index] in VOWELS and phrase[index-1] not in VOWELS:
                    continue
            items.append(chr_)
            consecutive = 1
    return "".join(items)

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
