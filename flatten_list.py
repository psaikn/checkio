def flat_list(li):
    li_ = []
    return do_flat_list(li, li_)

def do_flat_list(li, li_):
    for item in li:
        if isinstance(item, list):
            do_flat_list(item, li_)
        else:
            li_.append(item)
    return li_
    

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
