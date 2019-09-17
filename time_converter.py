def time_converter(time):
    #replace this for solution
    benchmark = 12
    hour, minute = time.split(":")
    if int(hour) < benchmark:
        if hour != '00' and hour[0] == '0':
            hour = hour[1:]
        elif hour == '00':
            hour = benchmark
        zone = 'a.m.'
    else:
        if int(hour) > benchmark:
            hour = int(hour) - benchmark
        zone = 'p.m.'
    time = "{}:{} {}".format(hour, minute, zone)
    return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
