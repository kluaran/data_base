
'''Модуль со всеми проверяющими функциями, которые используются в программе.'''

import string


def do_you_want(deistvie):
    ''' Декоратор запускающий функцию только при получении от пользователя от вета ДА.'''

    def decor(func):
        def wrapper(*args, **kwargs):
            while True:
                anser = chek_nal_bookv(input(deistvie), deistvie)
                if anser in ['da', 'yes', 'да']:
                    func(*args, **kwargs)
                elif anser in ['no', 'not', 'net', 'нет']:
                    break
                else:
                    print('Ваш ответ не понятен!')
        return wrapper
    return decor


def punctuation(text):
    '''Избавление от лишних символов пунктуации и пробелов, переводит в нижний регистр.'''

    for i in string.punctuation:
        text = text.replace(i, ' ')
    text = ' '.join(text.split())
    return text.lower()


def chek_isnum(text, deistvie):
    '''Проверка являются ли пользовательские данные числом.'''

    text = punctuation(text)
    try:
        text = int(text)
    except ValueError:
        text = input(f'Данные должны являться натуральным числом!\n{deistvie}')
        return chek_isnum(text, deistvie)
    else:
        return text


def chek_nal_bookv(text, deistvie):
    '''Проверка данных вверённых пользователем на наличие букв.'''

    text = punctuation(text)
    if any(filter(lambda x: x.isalpha(), text)):
        return perevod_to_eng(text)
    else:
        text = input(f'Данные должны содержать хотябы одну букву!\n{deistvie}')
        return chek_nal_bookv(text, deistvie)


def perevod_to_eng(text):
    '''Переводит русский на английский транслит.'''

    for k in alfovit:
        text = text.replace(k, alfovit[k])
    return text


def perevod_to_rus(text):
    '''Переводит анлийский транслит на русский.'''

    text = text.lower()
    for v in alfovit.values():
        text = text.replace(v, list(alfovit.keys())[list(alfovit.values()).index(v)])
    return text


alfovit = {'ч': 'jx',
           'щ': 'wx',
           'ё': 'yo',
           'ы': 'yi',
           'э': 'ye',
           'ю': 'yu',
           'я': 'ya',
           'а': 'a',
           'б': 'b',
           'в': 'v',
           'г': 'g',
           'д': 'd',
           'е': 'e',
           'ж': 'j',
           'з': 'z',
           'и': 'i',
           'й': 'q',
           'к': 'k',
           'л': 'l',
           'м': 'm',
           'н': 'n',
           'о': 'o',
           'п': 'p',
           'р': 'r',
           'с': 's',
           'т': 't',
           'у': 'u',
           'ф': 'f',
           'х': 'h',
           'ц': 'c',
           'ш': 'w',
           'ъ': 'xx',
           'ь': 'x',
           ' ': '_',
           }
