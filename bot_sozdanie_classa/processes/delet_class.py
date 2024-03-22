import bot_sozdanie_classa.chek.translitor as tr
import os

def poisk_faila():
    i=True
    while i==True:
        print('\nВыберете класс:')
        spisok_failov=os.listdir('classes')
        if '__pycache__' in spisok_failov:
            del spisok_failov[spisok_failov.index('__pycache__')]
        for j in spisok_failov:
            print(spisok_failov.index(j)+1, '. ', j, sep='')
        name = input('\nВведите номер или имя класса: ')
        try:
            nomer=int(name)
        except ValueError:
            name = tr.perevod(name)
            adres=f'classes/{name}.py'
            if not os.path.exists(adres):
                print('Такого класса не существует!')
            else:
                i=False
        else:
            if nomer>len(spisok_failov) or nomer<1:
                print('Такого класса  не существоует!')
            else:
                adres= f'classes/{spisok_failov[nomer - 1]}'
                i=False
    return adres

def delit(adres):
    podtverjdenie=input(f'\nВы уверены что хотите удалить класс: {adres[8:]}? ')
    podtverjdenie=tr.perevod(podtverjdenie)
    if podtverjdenie=='da' or podtverjdenie=='yes':
        adres_object=adres.replace('classes', 'objects')
        os.remove(adres_object)
        os.remove(adres)
        print('Класс удалён!')
    elif podtverjdenie=='net' or podtverjdenie=='no':
        t=True
        while t==True:
            sogl=input('\nДля выбора другого класса нажмите Enter\nДля возвращения в главное меню введите: ___\n')
            if sogl=='':
                adres=poisk_faila()
                delit(adres)
                t=False
            elif sogl=='___':
                return
            else:
                print('Не корректные данные!')
    else:
        print('Ответ не понятен!')
        delit(adres)
