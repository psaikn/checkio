import re
def checkio(data):
    if len(data) < 10:
       return False
    
    exp = ['([a-z]+).*$', '([A-Z]+).*$', '([0-9]+).*$']
    return all([re.compile(e).search(data) for e in exp])    

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
