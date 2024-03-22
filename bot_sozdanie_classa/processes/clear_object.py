import chek.translitor as tr
import processes.pokazat_object as pob
import sys
# Выбор объекта
def vibor_objecta():
    t = True
    while t == True:
        name_faila = pob.name_faila()
        spisok_objectov = pob.name_objects(name_faila)
        if len(spisok_objectov) == 0:
            print('В выбранном классе нет объектов!')
            return 0, 0, 0
        name_object, nomer_objecta = pob.name_object(spisok_objectov)

        t1 = True
        while t1 == True:
            print(f'\nВы уверенны что хотите очистить объект {name_object}?')
            pob.pokaz_dannih(name_faila, nomer_objecta)
            file = open(f'processes/pokaz_objecta.py', 'a', encoding='utf-8')
            file.write(f'\nx={name_object}\n')
            file.close()
            if 'processes.pokaz_objecta' in sys.modules:
                del sys.modules['processes.pokaz_objecta']
            import processes.pokaz_objecta
            sogl = input('\nВведите ответ: ')
            sogl = tr.perevod(sogl)
            if sogl == 'no' or sogl == 'net' or sogl == 'False' or sogl == '0':
                t2 = True
                while t2 == True:
                    contr_sogl = input(
                        '\nДля выбора другого объекта нажмите Enter, для возвращения в главное меню введите: ___\n')
                    if contr_sogl == '':
                        t2 = False
                        t1 = False
                    elif contr_sogl == '___':
                        return 0, 0, 0
                    else:
                        print('Некорректный ввод данных!')
            elif sogl == 'yes' or sogl == 'da' or sogl == 'True' or sogl == '1':
                t1 = False
                t = False
            else:
                print('Некорректный ответ!')
    return name_faila, name_object, nomer_objecta
# Очистка объекта
def clear(name_faila, nomer_objecta):
    file = open(f'objects/{name_faila}', 'r', encoding='utf-8')
    soderjanie_faila = file.readlines()
    file.close()
    change_stroka = soderjanie_faila[2 * nomer_objecta]
    change_stroka = change_stroka.replace(change_stroka[change_stroka.find('(') + 1:change_stroka.find(')\n')],
                                          '')
    soderjanie_faila[2 * nomer_objecta] = change_stroka
    file = open(f'objects/{name_faila}', 'w', encoding='utf-8')
    file.write(f'{''.join(soderjanie_faila)}')
    file.close()
    return soderjanie_faila
# Показ пустого объекта
def pokaz(name_object, nomer_objecta, soderjanie_faila):
    print(f'\nОбъект очищен:\n\n{name_object}')
    file = open('processes/pokaz_objecta.py', 'w', encoding='utf-8')
    file.write(f'{soderjanie_faila[0]}\n\n{soderjanie_faila[2 * nomer_objecta]}')
    file.close()
    if 'processes.pokaz_objecta' in sys.modules:
        del sys.modules['processes.pokaz_objecta']
    import processes.pokaz_objecta
    return
# Запуск
def start():
    name_faila, name_object, nomer_objecta=vibor_objecta()
    if name_faila==0 and name_object==0 and nomer_objecta==0:
        return
    soderjanie_faila=clear(name_faila, nomer_objecta)
    pokaz(name_object, nomer_objecta, soderjanie_faila)
    return