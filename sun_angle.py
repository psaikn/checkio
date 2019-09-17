def sun_angle(time):
    #replace this for solution
    hr, min_ = map(int, time.split(":"))
    if hr <= 5 or (hr >= 18 and min_ > 0):
        return "I don't see the sun!"
    else:
        base_hr = 6
        cur_hr = round((hr - base_hr) * 15 + (min_ * 0.25), 2)
        return cur_hr

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
