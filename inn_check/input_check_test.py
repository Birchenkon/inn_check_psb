import re


# функция возвращает два списка: с инн тип int и с ошибочными значениями
def is_inn(input_data):
    lst_clc, lst_err = [], []
    # убираем лишние знаки табуляции, пробелы и тд. Оставляем только 1 пробел между
    # переводим сразу в list
    input_data = re.sub(r'\s+', ' ', input_data.strip()).split()

    # проверяем, является ли инн : длина = 10, только цифры
    for inn in input_data:
        if len(inn) == 10 and inn.isdigit():
            lst_clc.append(inn)
        else:
            lst_err.append(inn)

    return lst_clc, lst_err


if __name__ == '__main__':
    text = '77235171211\n7721503733\n7723092091'
    list_for_culc, list_error = is_inn(text)

    print(' Для дальнейших расчетов : ', list_for_culc, '\n',  'Ошибки : ', list_error)
