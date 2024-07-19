
'''Фаил запуска программы.'''

import sys
import os
from importlib import import_module
from chek.fullchek import chek_nal_bookv, chek_isnum, perevod_to_rus, do_you_want
from classes.Perent import Perent


class Main:

    __deistviya = {1:'Создать',
                 2:'Изменить',
                 3:'Очистить',
                 4:'Удалить',
                 5:'Посмотреть'
                 }
    __obj = {0:'Класс',
           1:'Объект'
           }

    def __call__(self, *args, **kwargs):
        '''Выполняет вызов объекта main().'''

        self.pokaz_deistviy()
        self.__func = {1:self.create_class,
                       2:self.change_class,
                       3:self.clear_class,
                       4:self.del_class,
                       5:self.show_class,
                       6:self.create_object,
                       7:self.change_object,
                       8:self.clear_object,
                       9:self.del_object,
                       10:self.show_object,
                       0:sys.exit
                       }
        self.vibor_deistviy()
        if 0 < self.index <= 5:
            deistvie = f'{self.__deistviya[self.index]} {self.__obj[0]}'
        elif self.index == 0:
            deistvie = 'Завершить Программу'
        else:
            deistvie = f'{self.__deistviya[self.index - 5]} {self.__obj[1]}'

        @do_you_want(f'\nХотите {deistvie}? ')
        def doing():
            '''Проверяет уверенность пользователя в выбранном действии и выполняет его.'''

            self.__func[self.index]()

        doing()


    def pokaz_deistviy(self):
        '''Показывает варианты действий.'''

        print('\nВыберите действие: ')
        for o in self.__obj:
            print(f'{self.__obj[o]}:')
            for d in self.__deistviya.items():
                print(f'\t{d[0]+o*5}. {d[1]}')
        print('Для завершения программы введите 0')

    def vibor_deistviy(self):
        '''Выбор нужного действия.'''

        while True:
            self.index = chek_isnum(input('Введите номер: '), 'Введите номер: ')
            if 0 <= self.index <=10:
                break
            else:
                print('Число должно быть в диапозоне от 0 до 10!')

    def create_class(self):
        '''Создание нового класса.'''

        Perent('name', (), {})
        print('\nКласс успешно создан!')
        input('Чтобы продолжить нажмите Enter')

    def change_class(self):
        '''Изменение атрибутов выбранного подкласса и его объектов.'''

        self.del_class(funkcia='change_cls', do1='изменить', do2='изменён')

    def clear_class(self):
        '''Удаление всех арибутов выбранного класса, его подклассов и их объектов.'''

        self.del_class(funkcia='clean_cls', do1='очистить', do2='очищен')

    def del_class(self, funkcia='del_cls', do1='удалить', do2='удалён'):
        '''Удаление выбранного класса и его объектов.'''

        answer = self.show_class(f'Вы уверенны что хотите {do1} класс')
        if answer:
            while True:
                if answer in ['da', 'yes']:
                    vipolnenie = Perent.__dict__[funkcia]
                    vipolnenie(self.class_name)
                    print(f'\nКласс успешно {do2}!')
                    input('Чтобы продолжить нажмите Enter')
                    break
                elif answer in ['net', 'no', 'not']:
                    break
                else:
                    print('Ваш ответ не понятен!')
                    answer = chek_nal_bookv(
                        input(f'Вы уверенны что хотите {do1} класс {perevod_to_rus(self.class_name.__name__).capitalize()}? '),
                        f'Вы уверенны что хотите {do1} класс {perevod_to_rus(self.class_name.__name__).capitalize()}? '
                        )
            if f'classes.{self.class_name.__name__}' in sys.modules:
                sys.modules.pop(f'classes.{self.class_name.__name__}')
            if f'objects.{self.class_name.__name__}' in sys.modules:
                sys.modules.pop(f'objects.{self.class_name.__name__}')

    def show_class(self, deystvie='\nЧтобы продолжить нажмите Enter'):
        '''Показ существующего класса.'''

        directoria = os.listdir('classes')
        directoria.remove('Perent.py')
        directoria.remove('__pycache__')
        if directoria:
            Perent.choice_class(Perent)
            self.class_name = import_module(f'classes.{Perent.file_name[:-3]}').__dict__[f'{Perent.file_name[:-3]}']
            self.class_name.get_cl_attributs()
            if deystvie == '\nЧтобы продолжить нажмите Enter':
                sys.modules.pop(f'classes.{self.class_name.__name__}')
                input(f'{deystvie}')
            elif deystvie == 'Введите номер подкласса: ':
                return chek_isnum(input(f'{deystvie}'), f'{deystvie}')
            else:
                return chek_nal_bookv(input(f'{deystvie} {perevod_to_rus(self.class_name.__name__).capitalize()}? '),
                                      f'{deystvie} {perevod_to_rus(self.class_name.__name__).capitalize()}? '
                                      )
        else:
            print('Ни одного класса пока не создано!')
            return ''

    def create_object(self):
        '''Создание нового объекта'''

        while True:
            self.index1 = self.show_class('Введите номер подкласса: ')
            if not self.index1 and self.index1!=0:
                break
            spisok_podcls = lambda x: [x] + [j for i in list((map(spisok_podcls, x.__subclasses__()))) for j in i]
            spisok = spisok_podcls(self.class_name)
            if self.index1-1 in range(len(spisok)):
                podclass = spisok[self.index1-1]
                podclass.criate_object(self.class_name)
                print('\nОбъект успешно создан!')
                sys.modules.pop(f'classes.{self.class_name.__name__}')
                input('Чтобы продолжить нажмите Enter')
                break
            else:
                print('Такого подкласса не существует!')
                sys.modules.pop(f'classes.{self.class_name.__name__}')
                break

    def change_object(self):
        '''Функция для изменения объекта.'''

        self.del_object(funkcia='setter', do1='изменить', do2='изменён')

    def clear_object(self):
        '''Функция для отчистки объекта.'''

        self.del_object(funkcia='cleaner', do1='очистить', do2='очищен')

    def del_object(self, funkcia='deletter', do1='удалить', do2='удалён'):
        '''Функция для удаления пользовательского объекта.'''

        answer = self.show_object(f'Вы уверенны что хотите {do1} объект')
        if answer:
            while True:
                if answer in ['da', 'yes']:
                    vipolnenie = Perent.__dict__[funkcia]
                    vipolnenie(self.class_name, self.obj_name)
                    print(f'\nОбъект успешно {do2}!')
                    input('Чтобы продолжить нажмите Enter')
                    break
                elif answer in ['net', 'no', 'not']:
                    break
                else:
                    print('Ваш ответ не понятен!')
                    answer = chek_nal_bookv(input(f'Вы уверенны что хотите {do1} объект "{perevod_to_rus(self.obj_name)}"? '),
                                            f'Вы уверенны что хотите {do1} объект "{perevod_to_rus(self.obj_name)}"? '
                                            )
            if f'objects.{self.class_name.__name__}' in sys.modules:
                sys.modules.pop(f'objects.{self.class_name.__name__}')
                sys.modules.pop(f'classes.{self.class_name.__name__}')

    def show_object(self, deystvie='\nЧтобы продолжить нажмите Enter'):
        '''Функия для показа выбранного объекта.'''

        directoria = os.listdir('classes')
        directoria.remove('Perent.py')
        directoria.remove('__pycache__')
        if directoria:
            Perent.choice_class(Perent)
            self.class_name = import_module(f'classes.{Perent.file_name[:-3]}').__dict__[Perent.file_name[:-3]]
            self.obj_name = self.class_name.getter(self.class_name)

            if deystvie == '\nЧтобы продолжить нажмите Enter':
                sys.modules.pop(f'objects.{self.class_name.__name__}')
                sys.modules.pop(f'classes.{self.class_name.__name__}')
                input(f'{deystvie}')
            else:
                if self.obj_name:
                    return chek_nal_bookv(input(f'{deystvie} "{perevod_to_rus(self.obj_name)}"? '),
                                          f'{deystvie} "{perevod_to_rus(self.obj_name)}"? '
                                          )
                else:
                    sys.modules.pop(f'objects.{self.class_name.__name__}')
                    sys.modules.pop(f'classes.{self.class_name.__name__}')
                    return ''
        else:
            print('Классы и объекты пока не созданы!')
            return ''


while True:
    main = Main()
    main()


