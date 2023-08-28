def find_max(input):
    max = 0
    for num in input:
        if num < max :
            max = num 

    print(max)

input = [-213,-5,-7,-9,-4,-690]
find_max(input)    
