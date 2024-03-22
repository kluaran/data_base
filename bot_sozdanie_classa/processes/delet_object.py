import processes.pokazat_object as pob
import chek.translitor as tr
import sys
# Выбор объекта
def delet_object():
    t=True
    while t==True:
        name_faila=pob.name_faila()
        spisok_objectov=pob.name_objects(name_faila)
        if len(spisok_objectov) == 0:
            print('В выбранном классе нет объектов!')
            return
        name_object, nomer_objecta=pob.name_object(spisok_objectov)

        t1=True
        while t1==True:
            print(f'\nВы уверенны что хотите удалить объект {name_object}?')
            pob.pokaz_dannih(name_faila, nomer_objecta)
            if 'processes.pokaz_objecta' in sys.modules:
                del sys.modules['processes.pokaz_objecta']
            import processes.pokaz_objecta
            sogl = input('\nВведите ответ: ')
            sogl = tr.perevod(sogl)
            if sogl=='no' or sogl=='net' or sogl=='False' or sogl=='0':
                t2=True
                while t2==True:
                    contr_sogl=input('\nДля выбора другого объекта нажмите Enter, для возвращения в главное меню введите: ___\n')
                    if contr_sogl=='':
                        t2=False
                        t1=False
                    elif contr_sogl=='___':
                        return
                    else:
                        print('Некорректный ввод данных!')
            elif sogl=='yes' or sogl=='da' or sogl=='True' or sogl=='1':
                t1=False
                t=False
            else:
                print('Некорректный ответ!')
    # удаление объекта
    file_objecta=open(f'objects/{name_faila}', 'r', encoding='utf-8')
    sodejimoe=file_objecta.readlines()
    sodejimoe[2*nomer_objecta-1:2*nomer_objecta+1]=''
    file_objecta.close()
    file_objecta = open(f'objects/{name_faila}', 'w', encoding='utf-8')
    file_objecta.writelines(sodejimoe)
    file_objecta.close()
    return