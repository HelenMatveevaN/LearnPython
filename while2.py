'''
* Создайте словарь типа "вопрос": "ответ", 
например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее

* Доработайте ask_user() так, чтобы когда пользователь вводил вопрос, 
который есть в словаре, программа давала ему соответствующий ответ. 

Например:
Пользователь: Что делаешь?
Программа: Программирую

'''

def ask_user():
    quest_answer = [
        {'вопрос': 'Что делаешь?', 'ответ': 'Программирую.'},
        {'вопрос': 'Как дела?', 'ответ': 'Хорошо!'},
        {'вопрос': 'Когда освободишься?', 'ответ': 'Не раньше завтрашнего утра.'},
        {'вопрос': 'Ну пока?', 'ответ': 'Пока!'}
        ]
    while True:
        user_say = input('Вопрос ')
        
        for x in quest_answer:
            if (user_say == x['вопрос']):
                print(quest_answer['ответ'])
            
            if (user_say == 'Ну пока?')
                break

if __name__ == "__main__":
    ask_user()
