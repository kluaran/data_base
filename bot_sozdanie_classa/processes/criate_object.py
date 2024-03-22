import bot_sozdanie_classa.processes.pokazat_class as p_cl
import  bot_sozdanie_classa.chek.translitor as tr
import sys
# Вбор основного класса
spisok_vseh_classov, adres=p_cl.vozvrat_soderj_classa()
kluchi=list(spisok_vseh_classov.keys())
name_faila=kluchi[0]
name_faila=name_faila.lower()+'.py'
vse_podclasses=list(spisok_vseh_classov.keys())
for punkt in vse_podclasses[1:]:
    vse_podclasses[vse_podclasses.index(punkt)]=punkt[0:punkt.index('(')]
# Вбор подкласса
n=True
while n == True:
    print('\nВыберите подкласс для совего объекта:')
    for i in kluchi:
        print(kluchi.index(i)+1, '. ', i, sep='')
    podclass = input('\nВведите номер или имя подкласса: ')
    try:
        nomer = int(podclass)
    except ValueError:
        podclass = tr.perevod(podclass)
        podclass=podclass.capitalize()
        if vse_podclasses.count(podclass)<1:
            print('Такого подкласса не существует!')
        else:
            n = False
    else:
        if nomer > len(vse_podclasses) or nomer < 1:
            print('Такого подкласса  не существоует!')
        else:
            podclass = vse_podclasses[nomer-1]
            n = False
# Поиск всех характеристик подкласса, включая характеристики всех родителей
Podclass=podclass.split()
Podclass=''.join(Podclass)
k=True
harrakteristiki=[]
while k==True:
    harrakteristiki+=(spisok_vseh_classov[kluchi[vse_podclasses.index(podclass)]])
    if kluchi[vse_podclasses.index(podclass)].count('(')==1:
        podclass=kluchi[vse_podclasses.index(podclass)][kluchi[vse_podclasses.index(podclass)].index('(')+1:kluchi[vse_podclasses.index(podclass)].index(')')]
    else:
        k=False
# Создание имени объекта и проверка его на совпадения
r=True
while r==True:
    name=input('\nВведите имя объекта: ')
    name=tr.perevod(name)
    if vse_podclasses.count(name)>0:
        print('Имя уже занято одним из подклассов!')
    elif name=='' or name.count('_')==len(name):
        print('Имя объекта должно содержать хотя бы одну букву или число!')
    else:
        file=open(f'objects/{name_faila}', 'r')
        # kol_strok=len(file.readlines())
        spisok_vseh_objects=[]
        for l in file.readlines():
            ind=l.find('=')
            spisok_vseh_objects.append(l[:ind])
        file.close()
        if spisok_vseh_objects.count(name)>0:
            print('Объект с таким именем уже существует!')
        else:
            r=False
# Заполнение данных объекта
l=0
spisok_dannih=[]
print(f'\nЗаполните характеристики для объекта {name}:')
while l < len(harrakteristiki):
    dannie=input(f'\nУкажите значение для поля {harrakteristiki[l]}: ')
    if dannie=='':
        print('Некорректный ввод данных!\nДля того чтобы оставь данный пункт пустым, пропишите: None\nЧтобы пропустить все оставшиеся пункты и прекратить заполнение пропишите: ___')
    elif dannie=='___':
        break
    else:
        spisok_dannih.append(dannie)
        l+=1
if spisok_dannih==[]:
    spisok_dannih.append('None')
file=open(f'objects/{name_faila}', 'a', encoding='utf-8')
file.write(f'\n{name}={Podclass}("{'", "'.join(spisok_dannih)}")\n')
file.close()
# Вывод итоговых данных
file=open(f'objects/{name_faila}', 'r', encoding='utf-8')
copiya=file.readlines()[0]
file_pokaza=open('processes/pokaz_objecta.py', 'w', encoding='utf-8')
file_pokaza.write(f'{copiya}\n')
file_pokaza.write(f'\n{name}={Podclass}("{'", "'.join(spisok_dannih)}")\n')
file_pokaza.close()
file.close()
print(f'\nСоздан объект {name}={Podclass}("{'", "'.join(spisok_dannih)}")\n')
import processes.pokaz_objecta