"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt (Control+C), писала пользователю "Пока!" 
  и завершала работу при помощи оператора break

Виды исключений:
1. Базовые - Exception, BaseException
2. Исключения ОС - ConnectionError, TimeoutError и т.д.
3. Основные - ValueError, TypeError, IndexError, KeyError

Полный список исключений: https://docs.python.org/3.5/library/exceptions.html
"""

def ask_user():
    quest_answer = [
    {'вопрос': 'Как дела?', 'ответ': 'Хорошо!'}
    ,{'вопрос': 'Что делаешь?', 'ответ': 'Программирую.'}
    ,{'вопрос': 'Когда освободишься?', 'ответ': 'Не раньше завтрашнего утра.'}
    ,{'вопрос': 'Ну пока?', 'ответ': 'Пока!'}
    ]
    n = 1    
    while n == 1:
        try:
            user_say = input('Вопрос ')
        
            for x in quest_answer:
                if user_say == x['вопрос']:
                    print(x['ответ'])
                    if user_say == 'Ну пока?':
                        n = 0
                        break
        except KeyboardInterrupt:
            print("Пока!")
            break
    
if __name__ == "__main__":
    ask_user()
