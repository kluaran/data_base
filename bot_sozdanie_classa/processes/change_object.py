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
            return
        name_object, nomer_objecta = pob.name_object(spisok_objectov)

        t1 = True
        while t1 == True:
            print(f'\nВы уверенны что хотите изменить объект {name_object}?')
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
                        return
                    else:
                        print('Некорректный ввод данных!')
            elif sogl == 'yes' or sogl == 'da' or sogl == 'True' or sogl == '1':
                t1 = False
                t = False
            else:
                print('Некорректный ответ!')
    # Установка характеристик в правильном порядке
    vse_har=processes.pokaz_objecta.x.__dict__
    vse_har_kluch=list(vse_har.keys())
    vse_har_value=list(vse_har.values())
    n=[]
    for nomer in range(len(vse_har)):
        n.append(nomer+1)
    n=tuple(n)
    processes.pokaz_objecta.x.set_data(*n)
    nom_har=processes.pokaz_objecta.x.__dict__
    nom_value=list(nom_har.values())
    nom_value.sort()
    slovar={}
    for k in nom_value:
        slovar[list(nom_har.keys())[list(nom_har.values()).index(k)]]=vse_har_value[vse_har_kluch.index(list(nom_har.keys())[list(nom_har.values()).index(k)])]
    # Вывод изменяемых характеристик
    t=True
    while t==True:
        slovar_keys=list(slovar.keys())
        slovar_elements=list(slovar.values())
        print('\nЧто вы хотите изменить?')
        for l in range(len(slovar)+1):
            if l==len(slovar):
                print(f'{l+1}. Всё')
            else:
                print(f'{l+1}. {slovar_keys[l]}: {slovar_elements[l]}')
        # Выбор меняемой характеристики
        har=input('\nВведите номер или имя изменяемой характеристики: ')
        try:
            har = int(har)
        except ValueError:
            har = tr.perevod(har)
            if har!=tr.perevod('всё'):
                if slovar_keys.count(har) == 0:
                    print('Такой характеристики не существует!')
                else:
                    t = False
            else:
                t=False
        else:
            if har <= 0 or har > len(slovar)+1:
                print('Такой характеристики не существует!')
            elif har==len(slovar)+1:
                har=tr.perevod('всё')
                t=False
            else:
                har = slovar_keys[har - 1]
                t = False
    # Замена характеристики
    if har==tr.perevod('всё'):
        for kluch in slovar:
            new=input(f'\nЕсли все следующие характеристики начиная с этой вы хотите оставить без изменений введите: ___\nЕсли все следующие характеристи начиная с этой вы хотите сделать пустыми введите: _____\nВведите новое значение для {kluch}: ')
            if (new.count(' ')+new.count('_')==len(new) or new=='') and new!='___' and new!='_____':
                slovar[kluch]=None
            elif new=='___':
                break
            elif new=='_____':
                for a in range(len(slovar)):
                    if a < list(slovar.keys()).index(kluch):
                        continue
                    else:
                        slovar[list(slovar_keys)[a]]=None
                break
            else:
                slovar[kluch]=new
    else:
        new = input(f'\nВведите новое значение для {har}: ')
        if new.count(' ') + new.count('_') == len(new) or new == '':
            new = None
        slovar[har] = new
    # Удаление лишних None в конце списка значений словаря
    znach_slovar=list(slovar.values())
    t=True
    while t==True:
        if znach_slovar[-1]==None:
            znach_slovar.pop()
            if len(znach_slovar)==0:
                t=False
        else:
            t=False
    # Перевод словаря в строку
    znach_stroka=[]
    for elem in znach_slovar:
        znach_stroka.append('"'+str(elem)+'"')
    znach_stroka=', '.join(znach_stroka)
    znach_stroka='('+znach_stroka+')'
    # Изменение данных объекта в файле объекта
    file=open(f'objects/{name_faila}', 'r', encoding='utf-8')
    soderjanie_faila=file.readlines()
    file.close()
    change_stroka=soderjanie_faila[2*nomer_objecta]
    change_stroka=change_stroka.replace(change_stroka[change_stroka.find('('):change_stroka.find(')\n')+1], znach_stroka)
    soderjanie_faila[2*nomer_objecta]=change_stroka
    file = open(f'objects/{name_faila}', 'w', encoding='utf-8')
    file.write(f'{''.join(soderjanie_faila)}')
    file.close()
    # Показать изменённый объект
    print(f'\nОбъект изменён:\n\n{name_object}')
    file=open('processes/pokaz_objecta.py', 'w', encoding='utf-8')
    file.write(f'{soderjanie_faila[0]}\n\n{soderjanie_faila[2*nomer_objecta]}')
    file.close()
    if 'processes.pokaz_objecta' in sys.modules:
        del sys.modules['processes.pokaz_objecta']
    import processes.pokaz_objecta
    return
def start():
    vibor_objecta()
    return