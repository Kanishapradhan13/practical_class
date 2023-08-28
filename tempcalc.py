while True:
    print('C or F or E')
    user_input = input()

    if user_input == 'c':
        print('enter celcius value:')
        user_input_degree = input('degree celcius:')
        user_input_degree = int(user_input_degree)
        result = (user_input_degree * 9/5) + 32
        print('the temperature in farenheit is:',result)

    if user_input == 'f':
        print('enter farenheit value:')
        user_input_degree = input('degree farenheit')
        user_input_degree = int(user_input_degree)    
        result = (user_input_degree - 32) * 5/9
        print ('the temperature in celcius is:',result)

    if user_input == 'e':
        exit()

