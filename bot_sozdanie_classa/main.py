import chek.fullchek as chek
import processes.pokazat_class as p_cl
import processes.delet_class as delit
import sys
import os

do=('Создать', 'Изменить', 'Удалить', 'Очистить', 'Посмотреть')
ob=('Класс', 'Объект')
def start():
    list_imp_fails=os.listdir('classes')
    if '__pycache__' in list_imp_fails:
        del list_imp_fails[list_imp_fails.index('__pycache__')]
    long=len(list_imp_fails)
    for mod in list_imp_fails:
        list_imp_fails[list_imp_fails.index(mod)]='bot_sozdanie_classa.classes.'+mod[:-3]
    list2=list_imp_fails[:]
    for mod in list_imp_fails:
        mod1=mod.replace('.classes.', '.objects.')
        list_imp_fails[list_imp_fails.index(mod)]=mod1
    list_imp_fails+=list2
    list_imp_fails.append('processes.pokaz_objecta')
    for modul in list_imp_fails:
        if modul in sys.modules:
            # print(modul)
            del sys.modules[modul]
    choice=input(f'\nВведите одно из дейстий {do} и один из объектов {ob}: \nДля завершения программы введите: Завершить Программу\n')
    choice=chek.fullcheck(choice)
    return choice, long

def doing(choice, long):
    if len(choice)!=2:
        print('Неверное количесто данных!\nКоманда должна содержать два слова!')
        choice, long=start()
        choice=doing(choice, long)

    elif choice==['Создать', 'Класс'] or choice==['Класс', 'Создать']:
        print('Создаём класс')
        if 'processes.criate_class' in sys.modules:
            del sys.modules['processes.criate_class']
        import processes.criate_class
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Создать', 'Объект'] or choice==['Объект', 'Создать']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Создаём объект')
            if 'processes.criate_object' in sys.modules:
                del sys.modules['processes.criate_object']
            import processes.criate_object
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Изменить', 'Класс'] or choice==['Класс', 'Изменить']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Изменяем класс')
            import processes.change_class as ch_cl
            ch_cl.start()
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Изменить', 'Объект'] or choice==['Объект', 'Изменить']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Изменяем объект')
            import processes.change_object as ch_ob
            ch_ob.start()
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Удалить', 'Класс'] or choice==['Класс', 'Удалить']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Удаляем класс')
            adres=delit.poisk_faila()
            delit.delit(adres)
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Удалить', 'Объект'] or choice==['Объект', 'Удалить']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Удаляем объект')
            import processes.delet_object as do
            do.delet_object()
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Очистить', 'Класс'] or choice==['Класс', 'Очистить']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Очищаем класс')
            import processes.clear_class as c_cl
            c_cl.start()
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Очистить', 'Объект'] or choice==['Объект', 'Очистить']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Очищаем объект')
            import processes.clear_object as cl_ob
            cl_ob.start()
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Посмотреть', 'Класс'] or choice==['Класс', 'Посмотреть']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Показываем класс')
            soderj_classa, adres=p_cl.vozvrat_soderj_classa()
            p_cl.pokaz_class(soderj_classa)
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Посмотреть', 'Объект'] or choice==['Объект', 'Посмотреть']:
        if long==0:
            print('Классов и объектов ещё не создано!')
        else:
            print('Показываем объект')
            import processes.pokazat_object as pob
            pob.start()
        choice, long = start()
        choice = doing(choice, long)
    elif choice==['Завершить', 'Программу']:
        print('Программа завершена!')
    else:
        print('Не корректно введены данные!')
        choice, long = start()
        choice = doing(choice, long)
    return choice

choice, long=start()
choice=doing(choice, long)