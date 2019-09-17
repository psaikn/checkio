from typing import List

def checkio(game_result: List[str]) -> str:
    res = None
    
    for i in range(0,3):
        horizontal = []
        vertical = []
        for j in range(0,3):
            horizontal.append(game_result[i][j])
            vertical.append(game_result[j][i])

        if len(set(horizontal)) == 1:
            res = horizontal[0]
        elif len(set(vertical)) == 1:
            res = vertical[0]
        else:
            pass
            
    # To get Diagnoal        
    ldiagnoal = [game_result[0][0], game_result[1][1], game_result[2][2]]
    rdiagnoal = [game_result[2][0], game_result[1][1], game_result[0][2]]
    if len(set(ldiagnoal)) == 1:
        res = ldiagnoal[0]
    elif len(set(rdiagnoal)) == 1:
        res = rdiagnoal[0]

    if res in ["X", "O"]:
        return res
    else:
        return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio([
        "OOX",
        "XXO",
        "OXX"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
