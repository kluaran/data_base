import bot_sozdanie_classa.processes.pokazat_class as p_cl
import  bot_sozdanie_classa.chek.translitor as tr
import sys
# Выбор основного класса
def name_faila():
    spisok_vseh_classov, adres=p_cl.vozvrat_soderj_classa()
    kluchi=list(spisok_vseh_classov.keys())
    name_faila=kluchi[0]
    name_faila=name_faila.lower()+'.py'
    return name_faila
# Получение списка объектов
def name_objects(name_faila):
    fail_objecta=open(f'objects/{name_faila}', 'r', encoding='utf-8')
    spisok_objectov=[]
    for stroki in fail_objecta.readlines()[2::2]:
        spisok_objectov.append(stroki[:stroki.find('=')])
    fail_objecta.close()
    return spisok_objectov
# Выбор объекта
def name_object(spisok_objectov):
    t=True
    while t==True:
        print('\nВыберете объект: ')
        for nomer in spisok_objectov:
            print(spisok_objectov.index(nomer)+1, '. ', nomer, sep='')
        name_objecta=input('\nВведите номер или имя объекта: ')
        try:
            nomer_objecta=int(name_objecta)
        except ValueError:
            name_objecta=tr.perevod(name_objecta)
            if spisok_objectov.count(name_objecta)==0:
                print('Такого объекта не существует!')
            else:
                t=False
        else:
            if nomer_objecta<=0 or nomer_objecta>len(spisok_objectov):
                print('Такого объекта не существует!')
            else:
                name_objecta=spisok_objectov[nomer_objecta-1]
                t=False
    nomer_stroki=spisok_objectov.index(name_objecta)+1
    return name_objecta, nomer_stroki
# Показ данных об объекте
def pokaz_dannih(name_faila, nomer_stroki):
    file_objecta=open(f'objects/{name_faila}', 'r', encoding='utf-8')
    nastroika=file_objecta.readlines()[0]
    file_objecta.close()
    file_objecta = open(f'objects/{name_faila}', 'r', encoding='utf-8')
    obj = file_objecta.readlines()[2*nomer_stroki]
    file_objecta.close()
    file_pokaza=open('processes/pokaz_objecta.py', 'w', encoding='utf-8')
    file_pokaza.write(f'{nastroika}\n\n{obj}')
    file_pokaza.close()
    return
# Запуск процесса
def start():
    name_fail=name_faila()
    spisok_objectov=name_objects(name_fail)
    if len(spisok_objectov)==0:
        print('В выбранном классе нет объектов!')
        return
    name_objecta, nomer_stroki=name_object(spisok_objectov)
    pokaz_dannih(name_fail, nomer_stroki)
    print('\n', name_objecta, sep='')
    if 'processes.pokaz_objecta' in sys.modules:
        del sys.modules['processes.pokaz_objecta']
    import processes.pokaz_objecta