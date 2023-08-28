input_string = "(((((((((())"

def findFloorAtEnd(input_string):
    floor_at_end = 0
    for c in input_string:
        if c== '(':
            floor_at_end += 1
        elif c == ')':
            floor_at_end-= 1
    return floor_at_end

    print('At the end, you will be at floor number: ', floor_at_end)

findFloorAtEnd(input_string)
