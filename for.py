'''

Оценки

Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.

'''
def main:
    listp = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '5b', 'scores': [3,3,5,4,5]},
        {'school_class': '5c', 'scores': [2,2,3,3,3]}]
    
    score_cnt = 0
    score_sum = 0
    for score in listp:
        score_cnt = score_cnt + score['scores'].len
        score_sum = score_sum + score['scores'].sum
        print("средний балл по классу {score['school_class']}: {score['scores'].sum/score['scores'].len}")
    
    print("средний балл по всей школе: { score_sum/score_cnt }")

if __name__ == "__main__":
    main()
