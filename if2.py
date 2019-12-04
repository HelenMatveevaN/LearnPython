get_val1 = 'aaaa'
get_val2 = 'learn'

def get_two_strings(get_val1, get_val2):

    is_return = -1

    if (type(get_val1) == str and type(get_val2) == str):
        print('Да, это строки')

        if (get_val1 == get_val2):
            is_return = 1
        else:
            if (len(get_val1) > len(get_val2)):
                is_return = 2
            elif (get_val2 == 'learn'):
                is_return = 3

    else:
        print('Нет, это не строки')
        is_return = 0

    return is_return

result = get_two_strings(get_val1, get_val2)
print(result)