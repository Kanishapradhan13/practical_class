input_string = ")))"

# print('Program is here')

def findFloorAtEnd(input_string):
    floor_at_end = 0
    # print('Inside the function')
    for c in input_string:
        # print('Inside loop')
        if c== '(':
            floor_at_end += 1
            # print('Inside c true')

        elif c == ')':
            floor_at_end -= 1
            # print('Inside elif')

    print('At the end, you will be at floor number: ', floor_at_end)
    return floor_at_end


findFloorAtEnd(input_string)
