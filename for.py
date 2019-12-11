'''
Оценки
Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''
def main():
    listp = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '5b', 'scores': [3,3,5,4,5]},
        {'school_class': '5c', 'scores': [2,2,3,3,3]}]
    
    score_cnt = 0
    score_sum = 0
    for score in listp:
        class_ = score['school_class']
        score1_cnt = len(score['scores'])#длина списка
        score_cnt += score1_cnt
        score1_sum = sum(score['scores'])#сумма элементов списка
        score_sum += score1_sum
        print('средний балл по классу {}: {}'.format(class_, score1_sum/score1_cnt))

    print("средний балл по всей школе: {}".format(score_sum/score_cnt))

if __name__ == "__main__":
    main()
