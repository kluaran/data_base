
'''Метакласс описывающий создание и функционал пользовательских классов.'''

import sys
import os
from importlib import import_module
from chek.fullchek import chek_nal_bookv, chek_isnum, perevod_to_rus, do_you_want



class Perent(type):
    name = None
    args = None

    def __new__(cls, name, base, args):
        if args:
            # Cоздание класса если он уже записан в файле.
            cls.name = name
            cls.args = args
            return type.__new__(cls, cls.name, base, cls.args)
        else:
            # Cоздание нового пользовательского класса.
            cls.cl_name(cls, base)
            cls.first_atr(cls, base)
            if not base:
                cls.clfile(cls, cls.name, base, cls.args)
                cls.obfile(cls)
                cls.create(cls, cls.name, base, cls.args)
            else:
                cls.create(cls, cls.name, base, cls.args)

    def cl_name(cls, base):
        '''Ввод имени для пользовательского класса и проверка на дублирование.'''

        # Лямбда функция для извлечения имен всех уже созданных подклассов в список.
        a = lambda x: [x.__name__] + [j for i in list((map(a, x.__subclasses__()))) for j in i]
        if base:
            allnames = a(base[0].__mro__[-2])
        else:
            allnames = []
        while True:
            name = chek_nal_bookv(input('Введите имя класса: '),
                                  'Введите имя класса: '
                                  ).capitalize()
            if ((allnames and (name not in allnames)) or
                    (not allnames and (name + '.py' not in os.listdir('classes')))):
                break
            else:
                print('Такой класс уже сущестует!')
        cls.name = name

    def first_atr(cls, base):
        '''Ввод первого атрибута и проверка на дублирование.'''

        if base:
            # Получение списка всех атрибутов родительских классов.
            allargs = [y for x in base[0].__mro__ if x is not object for y in list(x.attrs.keys())]
        else:
            allargs = []
        while True:
            atr = chek_nal_bookv(input('Введите атрибут класса: '), 'Введите атрибут класса: ')
            if atr not in allargs:
                break
            else:
                print('Такой атрибут уже существует!')
        cls.args = [atr]
        cls.atributs(cls, allargs)
        cls.args = dict.fromkeys(cls.args, None)

    @do_you_want('Хотите добавить атрибут класса? ')
    def atributs(cls, allargs):
        '''Ввод дополнительных атрибутов и проверка на их дублирование.'''

        while True:
            atr = chek_nal_bookv(input('Введите атрибут класса (для отмены введите "стоп" или "stop"): '),
                                 'Введите атрибут класса (для отмены введите "стоп" или "stop"): ')
            if atr not in allargs and atr not in cls.args and atr != 'stop':
                break
            elif atr == 'stop':
                return
            else:
                print('Такой атрибут уже существует!')
        cls.args.append(atr)

    def clfile(cls, name, base, attrs):
        '''Создание файла для класса и импорт в него мета-класса Perent.'''

        cls.file_name = cls.name
        with open(f'classes/{cls.file_name}.py', 'w', encoding='utf-8') as file:
            file.write('from classes.Perent import Perent\n\n')

    def obfile(cls):
        '''Создание файла для записи будущих объектов.'''

        with open(f'objects/{cls.file_name}.py', 'w', encoding='utf-8') as file:
            file.write(f'from classes.{cls.file_name} import *\n\n')

    def create(cls, name, base, attrs):
        '''Функция записывающая в созданный фаил код,

         генерирующий новый класс и его атрибуты.

         '''

        new_class = Perent(name, base, attrs)
        with open(f'classes/{cls.file_name}.py', 'a', encoding='utf-8') as file:
            file.write(f'{name} = Perent("{name}", '
                       f'({new_class.__base__.__name__},), '
                       f'{attrs})\n'
                       )

        @do_you_want(f'Хотите создать подкласс для "{perevod_to_rus(name.lower()).capitalize()}"? ')
        def create_podclasses(base):
            '''Создание подклассов с их атрибутами.'''

            Perent('name', (base,), {})

        create_podclasses(new_class)


    def __init__(cls, name, base, args):
        cls.attrs = cls.args.copy()
        if None in cls.attrs:
            cls.attrs.pop(None)
        cls.__init__ = Perent.obj_init

    def obj_init(self, *znach, **kwargs):
        '''Переопределение методов __init__ в пользовательских классах.'''

        znach = list(znach)
        if not kwargs:
            base = {'base':list(self.__class__.__mro__)[:-1]}
        else:
            kwargs['base'].pop(0)
            base = kwargs
        for char in base['base'][0].attrs:
            if znach:
                self.__dict__[char] = znach[0]
                znach.pop(0)
            else:
                self.__dict__[char] = None
        if len(base['base']) > 1:
            super(base['base'][0], self).__init__(*znach, **base)

    def choice_class(cls):
        '''Выбор файла с нужным классом.'''

        fail_names = os.listdir('classes')
        fail_names.remove('Perent.py')
        fail_names.remove('__pycache__')
        for i, el in enumerate(fail_names, 1):
            print(f'{i}. {perevod_to_rus(el[:-3]).capitalize()}')
        index = lambda: chek_isnum(input('Укажите номер нужного класса: '), 'Укажите номер нужного класса: ')
        i = index()
        while i not in range(1, len(fail_names)+1):
            print('Такой номер в списке отсутствует!')
            i = index()
        cls.file_name = fail_names[i-1]

    def get_cl_attributs(cls, k=0):
        '''Функия позволяющая вывести на экран

         все классы выбранного файла с их атрибутами.

         '''

        global n
        n = k + 1
        print(f'{n}. {perevod_to_rus(cls.__name__).capitalize()}'
              f' ({perevod_to_rus(cls.__base__.__name__).capitalize()}):'
              if cls.__base__ is not object
              else f'\n{n}. {perevod_to_rus(cls.__name__).capitalize()}:'
              )
        print(*['\t' + perevod_to_rus(x) for x in cls.attrs.keys()], sep='\n', end='\n')
        for name in cls.__subclasses__():
            name.get_cl_attributs(n)


    def criate_object(cls, rod_cls):
        '''Функия создания новых пользовательских экземпляров.'''

        cls.obj_name(rod_cls)
        cls.obj_atr()
        with open(f'objects/{rod_cls.__name__}.py', 'a', encoding='utf-8') as file:
            file.write(f'{cls.nameobj} = {cls.__name__}({', '.join(cls.list_atr)})\n')

    def obj_name(cls, rod_cls):
        '''Выбор имени нового экземпляра.'''

        text = f'Введите имя объекта для класса {perevod_to_rus(cls.__name__).capitalize()}: '
        while True:
            cls.nameobj = chek_nal_bookv(input(text), text)
            obj_modul = import_module(f'objects.{rod_cls.__name__}')
            obj_dir = dir(obj_modul)
            if cls.nameobj in obj_dir:
                print('Объект с таким именем существует!')
            else:
                sys.modules.pop(f'objects.{rod_cls.__name__}')
                break

    def obj_atr(cls):
        '''Присвоение значений атрибутам в экземплярах.'''

        cls.list_atr = []
        for i in cls.__mro__[:-1]:
            for j in i.attrs:
                znach = input(f'Введите значение для "{perevod_to_rus(j)}". '
                              f'\nДля пропуска нажмите Enter: ')
                if not znach or znach.isspace():
                    znach = 'None'
                else:
                    znach = znach.replace('"', "'")
                    znach = '"'+znach+'"'
                cls.list_atr.append(znach)

    def getter(cls, rod_cls):
        '''Функция показывает атрибуты выбранного объекта,

        при его наличии.

        '''

        class_modul = import_module(f'classes.{rod_cls.__name__}')
        obj_modul = import_module(f'objects.{rod_cls.__name__}')
        spisok_obj = []
        for i in dir(obj_modul):
            if i not in dir(class_modul):
                spisok_obj.append(i)
        if spisok_obj:
            while True:
                for i in range(len(spisok_obj)):
                    print(f'{i + 1}. {perevod_to_rus(spisok_obj[i])}')
                j = chek_isnum(input('Выберете объект: '), 'Выберете объект: ')
                if j-1 in range(len(spisok_obj)):
                    break
                else:
                    print('Такого объекта не существует!')
            print(f'\n{perevod_to_rus(spisok_obj[j-1])}')
            for k, v in obj_modul.__dict__[spisok_obj[j - 1]].__dict__.items():
                print(f'\t{perevod_to_rus(k)}: {v}')

        else:
            print(f'Для класса {perevod_to_rus(Perent.file_name[:-3]).capitalize()} объекты пока не созданы!')
        return spisok_obj[j - 1] if spisok_obj else ''

    def setter(cls, ch_obj):
        '''Функция переписывающая атрибуты объекта в файле.'''

        while True:
            obj = sys.modules[f'objects.{cls.__name__}'].__dict__[ch_obj]
            spisok_atrs = list(obj.__dict__.values())
            for i in range(len(spisok_atrs)):
                if spisok_atrs[i] is None:
                    spisok_atrs[i] = 'None'
                else:
                    spisok_atrs[i] = '"'+spisok_atrs[i]+'"'

            n = 0
            for k, v in obj.__dict__.items():
                n += 1
                print(f'{n}. {perevod_to_rus(k)}: {v}')

            while True:
                index = chek_isnum(input('Выберете атрибут.\nДля завершения изменений введите 0: '),
                                   'Выберете атрибут.\nДля завершения изменений введите 0: '
                                   )
                if index in range(1, len(obj.__dict__)+1):
                    break
                elif index == 0:
                    break
                else:
                    print('Такого атрибута не существует!')

            if index == 0:
                break

            znach = input(f'\nВведите новое значение для для атрибута {perevod_to_rus(list(obj.__dict__.keys())[index-1])}.'
                          f'\nДля удаления этого атрибута нажмите Enter.'
                          f'\nДля отмены изменения введите "___": '
                          )
            if not znach or znach.isspace():
                znach = 'None'
            elif znach == '___':
                znach = spisok_atrs[index-1]
            else:
                znach = znach.replace('"', "'")
                znach = '"'+znach+'"'

            spisok_atrs[index-1] = znach
            spisok_atrs = ', '.join(spisok_atrs)

            with open(f'objects/{cls.__name__}.py', 'r', encoding='utf-8') as file:
                spisok = file.readlines()
            for line in spisok:
                if line.startswith(f'{ch_obj} = '):
                    spisok[spisok.index(line)] = line[:line.index('(')] + f'({spisok_atrs})\n'
            with open(f'objects/{cls.__name__}.py', 'w', encoding='utf-8') as file:
                file.writelines(spisok)
            print('\n Атрибут изменен!\n')
            sys.modules.pop(f'objects.{cls.__name__}')
            import_module(f'objects.{cls.__name__}')


    def deletter(cls, del_obj):
        '''Функция для удаления объекта из файла.'''

        with open(f'objects/{cls.__name__}.py', 'r', encoding='utf-8') as file:
            spisok = file.readlines()
        for line in spisok:
            if line.startswith(f'{del_obj} = '):
                spisok.remove(line)
        with open(f'objects/{cls.__name__}.py', 'w', encoding='utf-8') as file:
            file.writelines(spisok)

    def cleaner(cls, clear_obj):
        '''Функция для удаления атрибутов объекта из файла.'''

        with open(f'objects/{cls.__name__}.py', 'r', encoding='utf-8') as file:
            spisok = file.readlines()
        for line in spisok:
            if line.startswith(f'{clear_obj} = '):
                spisok[spisok.index(line)] = line[:line.index('(')]+'()\n'
        with open(f'objects/{cls.__name__}.py', 'w', encoding='utf-8') as file:
            file.writelines(spisok)

    def del_cls(cls):
        '''Функция для удаления файлов объектов и классов.'''

        os.remove(f'objects/{cls.__name__}.py')
        os.remove(f'classes/{cls.__name__}.py')

    def clean_cls(cls):
        '''Функция удаляющая атрибуты из файлов класса и объектов.'''

        class_modul = import_module(f'classes.{cls.__name__}')
        obj_modul = import_module(f'objects.{cls.__name__}')
        spisok_obj = []
        for i in dir(obj_modul):
            if i not in dir(class_modul):
                spisok_obj.append(i)

        with open(f'objects/{cls.__name__}.py', 'r', encoding='utf-8') as file:
            spisok = file.readlines()
        for line in spisok:
            for clear_obj in spisok_obj:
                if line.startswith(f'{clear_obj} = '):
                    spisok[spisok.index(line)] = line[:line.index('(')] + '()\n'
                break
        with open(f'objects/{cls.__name__}.py', 'w', encoding='utf-8') as file:
            file.writelines(spisok)

        with open(f'classes/{cls.__name__}.py', 'r', encoding='utf-8') as file1:
            spisok1 = file1.readlines()
        for line in spisok1:
            if ', {' in line:
                spisok1[spisok1.index(line)] = line[:line.index('{')] + '{None: None})\n'
        with open(f'classes/{cls.__name__}.py', 'w', encoding='utf-8') as file1:
            file1.writelines(spisok1)

    def change_cls(cls):
        '''Функция перезаписывающая атрибуты класса и объектов в файле.'''

        a = lambda x: [x] + [j for i in list((map(a, x.__subclasses__()))) for j in i]
        class_names = a(cls)
        while True:
            nomber = chek_isnum(input('Введите номер подкласса: '), 'Введите номер подкласса: ')
            if nomber-1 in range(len(class_names)):
                break
            else:
                print('Такого подкласса не существует!')
        class_ch = class_names[nomber-1]
        print('\nВыберите действие: ', '1. удалить атрибут', '2. изменить атрибут', '3. добавить атрибут', '0. отменить измение', sep='\n')
        while True:
            deistvie = chek_isnum(input('Введите соответствующий номер: '), 'Введите соответствующий номер: ')
            if deistvie in range(4):
                break
            else:
                print('Номер должен быть в пределах от 0 до 3!')

        obj_modul = import_module(f'objects.{cls.__name__}')
        cls_modul = import_module(f'classes.{cls.__name__}')
        spisok_obj = []
        for i in dir(obj_modul):
            if i not in dir(cls_modul):
                spisok_obj.append(i)
        spisok_obj1 = []
        for j in spisok_obj:
            if class_ch in type(obj_modul.__dict__[j]).__mro__:
                spisok_obj1.append(j)
        spisok_obj = []
        for i in spisok_obj1:
            if any(obj_modul.__dict__[i].__dict__.values()):
                spisok_obj.append(i)

        if deistvie in [1, 2]:
            if class_ch.attrs:
                for i, el in enumerate(class_ch.attrs, 1):
                    print(f'\t{i}. {perevod_to_rus(el)}')
                while True:
                    atribut = chek_isnum(input('Выберите атрибут: '), 'Выберите атрибут: ')
                    if atribut-1 in range(len(class_ch.attrs)):
                        break
                    else:
                        print('Такого атрибута не существует!')
                atribut = list(class_ch.attrs.keys())[atribut - 1]

                if deistvie == 1:
                    for i in spisok_obj:
                        spisok_atrs = obj_modul.__dict__[i].__dict__
                        spisok_atrs.pop(atribut)
                        spisok_atrs = tuple(spisok_atrs.values())
                        with open(f'objects/{cls.__name__}.py', 'r', encoding='utf-8') as file:
                            spisok = file.readlines()
                        for line in spisok:
                            if line.startswith(f'{i} = '):
                                spisok[spisok.index(line)] = line[:line.index('(')] + f'{spisok_atrs}\n'
                        with open(f'objects/{cls.__name__}.py', 'w', encoding='utf-8') as file:
                            file.writelines(spisok)
                    spisok_atrs = class_ch.attrs
                    spisok_atrs.pop(atribut)
                    if not spisok_atrs:
                        spisok_atrs = {None: None}
                    with open(f'classes/{cls.__name__}.py', 'r', encoding='utf-8') as file1:
                        spisok1 = file1.readlines()
                    for line in spisok1:
                        if line.startswith(class_ch.__name__):
                            spisok1[spisok1.index(line)] = line[:line.index('{')] + f'{spisok_atrs})\n'
                    with open(f'classes/{cls.__name__}.py', 'w', encoding='utf-8') as file1:
                        file1.writelines(spisok1)

                elif deistvie == 2:
                    allattrs = [y for x in class_ch.__mro__ if x is not object for y in list(x.attrs.keys())]
                    b = lambda x: [y for i in x.__subclasses__() for y in i.attrs.keys()] + [k for j in x.__subclasses__() for k in b(j)]
                    allattrs1 = b(class_ch)
                    allattrs.extend(allattrs1)
                    allattrs.remove(atribut)
                    while True:
                        new_attr = chek_nal_bookv(input('Введите новое название атрибута: '), 'Введите новое название атрибута: ')
                        if new_attr not in allattrs:
                            break
                        else:
                            print('Такой атрибут уже существует!')
                    spisok_atrs = list(class_ch.attrs.keys())
                    spisok_atrs[spisok_atrs.index(atribut)] = new_attr
                    spisok_atrs = dict.fromkeys(spisok_atrs, None)
                    with open(f'classes/{cls.__name__}.py', 'r', encoding='utf-8') as file1:
                        spisok1 = file1.readlines()
                    for line in spisok1:
                        if line.startswith(class_ch.__name__):
                            spisok1[spisok1.index(line)] = line[:line.index('{')] + f'{spisok_atrs})\n'
                    with open(f'classes/{cls.__name__}.py', 'w', encoding='utf-8') as file1:
                        file1.writelines(spisok1)
            else:
                print('У этого класса нет атрибутов!')

        elif deistvie == 3:
            allattrs = [y for x in class_ch.__mro__ if x is not object for y in list(x.attrs.keys())]
            if allattrs:
                n = 0
                while allattrs[n] in class_ch.attrs and n+1 < len(allattrs):
                    n +=1
                next_atr = allattrs[n]
            else:
                next_atr = None
            b = lambda x: [y for i in x.__subclasses__() for y in i.attrs.keys()] + [k for j in x.__subclasses__() for k in b(j)]
            allattrs1 = b(class_ch)
            allattrs.extend(allattrs1)
            while True:
                new_attr = chek_nal_bookv(input('Введите название нового атрибута: '),
                                          'Введите название нового атрибута: ')
                if new_attr not in allattrs:
                    break
                else:
                    print('Такой атрибут уже существует!')
            for i in spisok_obj:
                spisok_atrs = obj_modul.__dict__[i].__dict__
                if next_atr and next_atr not in class_ch.attrs:
                    index = list(spisok_atrs.keys()).index(next_atr)
                else:
                    index = len(spisok_atrs)
                spisok_atrs = list(spisok_atrs.values())
                spisok_atrs.insert(index, None)
                spisok_atrs = tuple(spisok_atrs)
                with open(f'objects/{cls.__name__}.py', 'r', encoding='utf-8') as file:
                    spisok = file.readlines()
                for line in spisok:
                    if line.startswith(f'{i} = '):
                        spisok[spisok.index(line)] = line[:line.index('(')] + f'{spisok_atrs}\n'
                with open(f'objects/{cls.__name__}.py', 'w', encoding='utf-8') as file:
                    file.writelines(spisok)

            spisok_atrs1 = class_ch.attrs
            spisok_atrs1.update({new_attr: None})
            with open(f'classes/{cls.__name__}.py', 'r', encoding='utf-8') as file1:
                spisok1 = file1.readlines()
            for line in spisok1:
                if line.startswith(class_ch.__name__):
                    spisok1[spisok1.index(line)] = line[:line.index('{')] + f'{spisok_atrs1})\n'
            with open(f'classes/{cls.__name__}.py', 'w', encoding='utf-8') as file1:
                file1.writelines(spisok1)
