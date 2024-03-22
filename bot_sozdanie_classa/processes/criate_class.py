import os
import bot_sozdanie_classa.chek.translitor as tr


def naz():
    name = input('\nВведите имя класса: ')
    name = tr.perevod(name)
    if len(name) == 0 or name.count('_') == len(name):
        print('Имя должно содержать хотя бы одну букву!')
        name = naz()
    return name


def create(name):
    x = f'classes/{name}.py'
    if not os.path.exists(x):
        file = open(f'classes/{name}.py', 'w', encoding='utf-8')
        file.write(f'class {name.capitalize()}:\n')
        file.close()
    else:
        print('Такой класс уже существует!')
        name = naz()
        name = create(name)
    return name


def soderj(name):
    try:
        kol_har = int(input(f'\nУкажите количество характеристик для класса {name.capitalize()}: '))
    except ValueError:
        print('Число указано не верно!')
        name_har, name_def_har = soderj(name)
        return name_har, name_def_har
    else:
        stroka = ''
        stroka_def_arg = ''
        spisok = []
        nomer = 0
        file = open(f'classes/{name}.py', 'a', encoding='utf-8')
        while nomer < kol_har:
            har = input(f'\nВведите характеристику №{nomer + 1}: ')
            har = tr.perevod(har)

            if len(har) == 0 or (har.count('_') == len(har) and har != '___'):
                print('Характеристика должна содержать хотя бы одну букву!')
                print('Для пропуска характеристики введите: ___')
            elif har == '___':
                nomer += 1
            else:

                if spisok.count(har) != 0 or har=='self':
                    print('Такая характеристика уже существует')
                else:
                    nomer += 1
                    file.write(f'\t{har} = None\n')
                    stroka = stroka + ', ' + har
                    stroka_def_arg = stroka_def_arg + ', ' + har + '=None'
                    spisok.append(har)
        stroka = stroka[2:]
        stroka_def_arg = stroka_def_arg[2:]

        if spisok==[]:
            print("Класс должен содержать хотя бы одну характеристику!")
            name_har, name_def_har = soderj(name)
            return name_har, name_def_har
        else:
            file.write(f'\n\tdef set_data(self, {stroka_def_arg}):\n')
            for obj in spisok:
                file.write(f'\t\tself.{obj} = {obj}\n')

            stroka_get = ''
            file.write('\n\tdef get_data(self):\n')
            for kol in spisok:
                stroka_get = stroka_get + 'f"' + f'{kol}' + ': {self.' + f'{kol}' + '}", '
            file.write(f'\t\tprint({stroka_get}sep="\\n")\n')

            file.write(f'\n\tdef __init__(self, {stroka_def_arg}):\n')
            file.write(f'\t\tself.set_data({stroka})\n')
            file.write('\t\tself.get_data()\n')

            file.close()
            return stroka, stroka_def_arg


def pod_class(name, name_har, name_def_har, name_file, name_vseh_classov):
    x = input(f'\nХотиде создать класс наследник для класса {name}? ')
    x = tr.perevod(x)
    if x == 'net' or x == 'false' or x == '0' or x == 'no':
        return name_vseh_classov
    elif x == 'da' or x == 'true' or x == '1' or x == 'yes':

        n1 = True
        while n1==True:
            name_sub= input(f'\nВведите имя класса наследника для класса {name}: ')
            name_sub = tr.perevod(name_sub)

            if len(name_sub) == 0 or name_sub.count('_') == len(name_sub):
                print('Имя должно содержать хотя бы одну букву!')
            elif name_vseh_classov.count(name_sub)>0:
                print(f'Подкласс с именем {name_sub} уже существует!')
            else:
                file = open(f'classes/{name_file}.py', 'a', encoding='utf-8')
                file.write(f'\nclass {name_sub.capitalize()}({name.capitalize()}):\n')
                file.close()

                n2=True
                while n2==True:
                    try:
                        kol_har = int(input(f'\nУкажите количество характеристик для класса {name_sub.capitalize()}: '))
                    except ValueError:
                        print('Число указано не верно!')

                    else:
                        stroka = ''
                        stroka_def_arg = ''
                        spisok = []
                        nomer = 0
                        file = open(f'classes/{name_file}.py', 'a', encoding='utf-8')
                        while nomer < kol_har:
                            har = input(f'\nВведите характеристику №{nomer + 1}: ')
                            har = tr.perevod(har)

                            if len(har) == 0 or (har.count('_') == len(har) and har != '___'):
                                print('Характеристика должна содержать хотя бы одну букву!')
                                print('Для пропуска характеристики введите: ___')
                            elif har == '___':
                                nomer += 1
                            else:

                                if spisok.count(har) != 0 or str(name_har).split(', ').count(har)!=0 or har=='self':
                                    print('Такая характеристика уже существует!')
                                else:
                                    nomer += 1
                                    file.write(f'\t{har} = None\n')
                                    stroka = stroka + ', ' + har
                                    stroka_def_arg = stroka_def_arg + ', ' + har + '=None'
                                    spisok.append(har)
                        stroka = stroka[2:]
                        stroka_def_arg = stroka_def_arg[2:]

                        if spisok==[]:
                            print('Класс наследник должен содержать хотябы одну характеристику!')
                        else:
                            file.write(f'\n\tdef set_data(self, {stroka_def_arg}, {name_def_har}):\n')
                            file.write(f'\t\tsuper({name_sub.capitalize()}, self).set_data({name_har})\n')
                            for obj in spisok:
                                file.write(f'\t\tself.{obj} = {obj}\n')

                            stroka_get = ''
                            file.write('\n\tdef get_data(self):\n')
                            file.write('\t\tsuper().get_data()\n')
                            for kol in spisok:
                                stroka_get = stroka_get + 'f"' + f'{kol}' + ': {self.' + f'{kol}' + '}", '
                            file.write(f'\t\tprint({stroka_get}sep="\\n")\n')

                            file.write(f'\n\tdef __init__(self, {stroka_def_arg}, {name_def_har}):\n')
                            file.write(f'\t\tself.set_data({stroka}, {name_har})\n')
                            file.write('\t\tself.get_data()\n')

                            file.close()
                            n2=False

                name_last_rod=name_sub
                name_har_vseh_rod=stroka+', '+name_har
                name_def_har_vseh_rod=stroka_def_arg+', '+name_def_har
                name_vseh_classov.append(name_sub)
                name_vseh_classov=pod_class(name_last_rod, name_har_vseh_rod, name_def_har_vseh_rod, name_file, name_vseh_classov)
                name_vseh_classov=pod_class(name, name_har, name_def_har, name_file, name_vseh_classov)
                n1=False
                return name_vseh_classov

    else:
        print('Ваш ответ не понятен')
        name_vseh_classov=pod_class(name, name_har, name_def_har, name_file, name_vseh_classov)
        return name_vseh_classov

name = naz()
name = create(name)
name_file=name
name_vseh_classov=[name]
name_har, name_def_har = soderj(name)
name_vseh_classov=pod_class(name, name_har, name_def_har, name_file, name_vseh_classov)
print(f'Класс {name} создан!')

for imena in name_vseh_classov:
    nomer_imeni=name_vseh_classov.index(imena)
    name_vseh_classov[nomer_imeni]=imena.capitalize()
v_object=', '.join(name_vseh_classov)

file=open(f'objects/{name_file}.py', 'w', encoding='utf-8')
file.write(f'from bot_sozdanie_classa.classes.{name_file} import {v_object}\n' )
file.close()