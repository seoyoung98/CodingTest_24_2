import sys

while True:
    input_str = sys.stdin.readline().rstrip('\n')

    if not input_str:
        break

    small = 0
    big = 0
    num = 0
    blank = 0

    for i in input_str:
        if i.isdecimal():
            num +=1
        elif i.isalpha():
            if i.isupper():
                big += 1
            else:
                small += 1
        else:
            blank += 1

    print(small, big, num, blank)