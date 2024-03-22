import chek.translitor as tr
import processes.pokazat_class as p_cl
import sys


# Выбор класса
def vibor_classa():
    soder_classa, adres = p_cl.vozvrat_soderj_classa()
    kluchi = list(soder_classa.keys())
    class_name_list = []
    for k in kluchi:
        if k.count('(') != 0:
            k = k[0:k.index('(')]
        class_name_list.append(k)
    return soder_classa, adres, kluchi, class_name_list


# Выбор подкласса
def vibor_podclassa(soder_classa, kluchi, class_name_list):
    t = True
    while t == True:
        print('\nВыберите подкласс:')
        for i in soder_classa:
            print(kluchi.index(i) + 1, '. class ', i, ':', sep='')
            for j in soder_classa[i]:
                print(j)
            print('')
        print(len(soder_classa) + 1, '. Все подклассы', sep='')
        vibor = input('\nВведите номер или имя подкласса: ')
        try:
            vibor = int(vibor)
        except ValueError:
            vibor = tr.perevod(vibor)
            vibor = vibor.capitalize()
            if class_name_list.count(vibor) == 0 and vibor != 'Vse_podklassyi':
                print('Такого подкласса не существует!')
            else:
                t = False
        else:
            if vibor < 1 or vibor > len(class_name_list) + 1:
                print('Такого класса не существует!')
            else:
                if vibor == len(class_name_list) + 1:
                    vibor = 'Vse_podklassyi'
                else:
                    vibor = class_name_list[vibor - 1]
                t = False
    return vibor


# Проверка на уверенность в выборе
def proverka_na_uver(soder_classa, adres, kluchi, class_name_list, vibor):
    t1 = True
    while t1 == True:
        if vibor != 'Vse_podklassyi':
            print(f'\nВы уверенны что хотите очистить подкласс {kluchi[class_name_list.index(vibor)]}:')
            for i in soder_classa[kluchi[class_name_list.index(vibor)]]:
                print(i)
        else:
            print('\nВы уверенный что хотите очистить ВСЕ подклассы?')
        sogl = input('\nВведите ответ: ')
        sogl = tr.perevod(sogl)
        if sogl == 'no' or sogl == 'net' or sogl == 'False' or sogl == '0':
            t2 = True
            while t2 == True:
                contr_sogl = input(
                    '\nДля выбора другого подкласса нажмите Enter, для возвращения в главное меню введите: ___\n')
                if contr_sogl == '':
                    soder_classa, adres, kluchi, class_name_list = vibor_classa()
                    vibor = vibor_podclassa(soder_classa, kluchi, class_name_list)
                    soder_classa, adres, kluchi, class_name_list, vibor = proverka_na_uver(soder_classa, adres, kluchi,
                                                                                           class_name_list, vibor)
                    t2 = False
                    t1 = False
                elif contr_sogl == '___':
                    return 0, 0, 0, 0, 0
                else:
                    print('Некорректный ввод данных!')
        elif sogl == 'yes' or sogl == 'da' or sogl == 'True' or sogl == '1':
            t1 = False
        else:
            print('Некорректный ответ!')
    return soder_classa, adres, kluchi, class_name_list, vibor


# Извлечение списка всех родительских классов выбранного подкласса
def spisok_rod_classov(kluchi, class_name_list, vibor):
    spisok_rod_classov = []
    t = True
    while t == True:
        spisok_rod_classov.append(vibor)
        if kluchi[class_name_list.index(vibor)][-1] == ')':
            x = kluchi[class_name_list.index(vibor)][::-1].find('(')
            vibor = kluchi[class_name_list.index(vibor)][-x:-1]
        else:
            t = False
    return spisok_rod_classov


# Функция удаления характеристики
def del_har(soder_classa, name_faila, kluchi, class_name_list, vibor):
    # Создание списка удаляемых характеристик
    if vibor != 'Vse_podklassyi':
        spisok_del_har = [soder_classa[kluchi[class_name_list.index(vibor)]]]
    else:
        spisok_del_har = []
        for val in soder_classa.values():
            spisok_del_har.append(val)
    # Извлечение содержимого в фаил класса
    file = open(f'classes/{name_faila}', 'r', encoding='utf-8')
    sodrjanie_faila = file.readlines()
    file.close()
    # Извлечение содержания объектов данного класса
    fail = open(f'objects/{name_faila}', 'r', encoding='utf-8')
    soder_faila_objectov = fail.readlines()
    fail.close()
    # Копирование содержания класса
    soder_classa1 = {}
    for k in soder_classa:
        soder_classa1.setdefault(k[:], soder_classa[k][:])

    for har_classa in spisok_del_har:
        dlina = len(har_classa)
        for har in har_classa:
            # Поиск всех подклассов для которых выбранный подкласс является родительским
            del_class = class_name_list[list(soder_classa.values()).index(har_classa)]
            spisok_docher_class = []
            for kajdiy_class in class_name_list:
                roditeli = spisok_rod_classov(kluchi, class_name_list, kajdiy_class)
                if roditeli.count(del_class) > 0:
                    spisok_docher_class.append(kluchi[class_name_list.index(kajdiy_class)])
            i = class_name_list.index(del_class) + 1
            # Вид новой характеристики
            if dlina == 1:
                new_har = [f'\tnone{i} = None\n', f', none{i}=None', f'\t\tself.none{i} = none{i}\n',
                           f'f"none{i}: ' + '{self.none' + f'{i}' + '}", ', f', none{i}, ', 'None']
            else:
                new_har = ['', '', '', '', '', '']

            # Внесение изменений в фаил класса
            for podclass in spisok_docher_class:
                if kluchi.index(podclass) != len(kluchi) - 1:
                    chast1 = sodrjanie_faila[:sodrjanie_faila.index(f'class {podclass}:\n')]
                    chast2 = sodrjanie_faila[sodrjanie_faila.index(f'class {podclass}:\n'):sodrjanie_faila.index(
                        f'class {kluchi[kluchi.index(podclass) + 1]}:\n')]
                    chast3 = sodrjanie_faila[sodrjanie_faila.index(f'class {kluchi[kluchi.index(podclass) + 1]}:\n'):]
                else:
                    chast1 = sodrjanie_faila[:sodrjanie_faila.index(f'class {podclass}:\n')]
                    chast2 = sodrjanie_faila[sodrjanie_faila.index(f'class {podclass}:\n'):]
                    chast3 = ['']
                for stroki in chast2:
                    if stroki.count(f'\t{har} = None\n') > 0:
                        stroki1 = stroki.replace(f'\t{har} = None\n', f'{new_har[0]}')
                    elif stroki.count(f', {har}=None') > 0:
                        stroki1 = stroki.replace(f', {har}=None', f'{new_har[1]}')
                    elif stroki.count(f'\t\tself.{har} = {har}\n') > 0:
                        stroki1 = stroki.replace(f'\t\tself.{har} = {har}\n', f'{new_har[2]}')
                    elif stroki.count(f'f"{har}: ' + '{self.' + f'{har}' + '}", ') > 0:
                        stroki1 = stroki.replace(f'f"{har}: ' + '{self.' + f'{har}' + '}", ', f'{new_har[3]}')
                    elif stroki.count(f'({har},') > 0:
                        stroki1 = stroki.replace(f'({har}, ', f'({new_har[4][2:]}')
                    elif stroki.count(f', {har},') > 0:
                        stroki1 = stroki.replace(f', {har}', f'{new_har[4][:-2]}')
                    elif stroki.count(f', {har})') > 0:
                        stroki1 = stroki.replace(f', {har})', f'{new_har[4][:-2]})')
                    elif stroki.count(f'({har})') > 0:
                        stroki1 = stroki.replace(f'({har})', f'({new_har[4][2:-2]})')
                    else:
                        stroki1 = stroki
                    chast2[chast2.index(stroki)] = stroki1
                sodrjanie_faila = chast1 + chast2 + chast3

            # Поиск выбранного и дочерних классов в содержании объекта
            for el in spisok_docher_class:
                spisok_docher_class[spisok_docher_class.index(el)] = class_name_list[kluchi.index(el)]
            for punkt in soder_faila_objectov:
                for podclass in spisok_docher_class:
                    if punkt.count(f'={podclass}(') > 0:
                        # Поиск порядкового номера удаляемой характеристики
                        rod_for_podclass_do_vibor = spisok_rod_classov(kluchi, class_name_list, podclass)
                        rod_for_podclass_do_vibor = rod_for_podclass_do_vibor[
                                                    :rod_for_podclass_do_vibor.index(del_class) + 1]
                        kol_har = 0
                        for rod in rod_for_podclass_do_vibor:
                            kol_har = kol_har + len(soder_classa1[kluchi[class_name_list.index(rod)]])
                        kol_har = kol_har - (len(soder_classa1[kluchi[class_name_list.index(del_class)]]) - (
                                    soder_classa1[kluchi[class_name_list.index(del_class)]].index(har) + 1))
                        # Вставка значения None для новой характеристики в объект
                        if punkt.count('", "') + 1 >= kol_har and punkt.count('()\n') == 0:
                            x, y, z = punkt[:punkt.find('("') + 2], punkt[
                                                                    punkt.find('("') + 2:punkt.find('")\n')], punkt[
                                                                                                              punkt.find(
                                                                                                                  '")\n'):]
                            y = y.split('", "')
                            if new_har[5] == 'None':
                                y[kol_har - 1] = 'None'
                            elif new_har[5] == '':
                                y.remove(y[kol_har - 1])
                            y = '", "'.join(y)
                            punkt_new = x + y + z
                            soder_faila_objectov[soder_faila_objectov.index(punkt)] = punkt_new
            dlina -= 1
            soder_classa1[kluchi[class_name_list.index(del_class)]].remove(har)

    new_class_soder = ''.join(sodrjanie_faila)
    new_obj_soder = ''.join(soder_faila_objectov)

    fail = open(f'classes/{name_faila}', 'w', encoding='utf-8')
    fail.write(f'{new_class_soder}')
    fail.close()

    fail = open(f'objects/{name_faila}', 'w', encoding='utf-8')
    fail.write(f'{new_obj_soder}')
    fail.close()
    return


# Запуск программы
def start():
    soder_classa, adres, kluchi, class_name_list = vibor_classa()
    vibor = vibor_podclassa(soder_classa, kluchi, class_name_list)
    soder_classa, adres, kluchi, class_name_list, vibor = proverka_na_uver(soder_classa, adres, kluchi, class_name_list,
                                                                           vibor)
    if soder_classa == 0 and adres == 0 and kluchi == 0 and class_name_list == 0 and vibor == 0:
        return
    name_faila = adres[8:]
    del_har(soder_classa, name_faila, kluchi, class_name_list, vibor)
    return