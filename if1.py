get_val = input('Укажите Ваш возраст: ')
age = int(get_val)

def get_age_status(age):
    
    v_status = 'учится в '
    
    if   3 <= age < 7:
        v_status = v_status + 'детском саду'
    elif 7 <= age < 17:
        v_status = v_status + 'школе'
    elif 17 <= age < 22:  
        v_status = v_status + 'ВУЗе'
    elif 22 <= age < 60: 
        v_status = 'работает'
    else:
        v_status = 'не определен'
    
    return v_status

status = get_age_status(age)
print(status)