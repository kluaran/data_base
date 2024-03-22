import bot_sozdanie_classa.chek.translitor as tr
import os

def vozvrat_soderj_classa():
    i=True
    while i==True:
        print('\nВыберете класс:')
        spisok_failov=os.listdir('classes')
        if '__pycache__' in spisok_failov:
            del spisok_failov[spisok_failov.index('__pycache__')]
        for j in spisok_failov:
            print(spisok_failov.index(j)+1, '. ', j, sep='')
        name = input('\nВведите номер или имя класса: ')
        try:
            nomer=int(name)
        except ValueError:
            name = tr.perevod(name)
            adres=f'classes/{name}.py'
            if not os.path.exists(adres):
                print('Такого класса не существует!')
            else:
                i=False
        else:
            if nomer>len(spisok_failov) or nomer<1:
                print('Такого класса  не существоует!')
            else:
                adres = f'classes/{spisok_failov[nomer - 1]}'
                i=False

    fail=open(f'{adres}', 'r')
    soder_classa= {}
    stroki=fail.readlines()
    kol_strok=len(stroki)
    n=0
    while n < kol_strok:
        if stroki[n]=='\n':
            k=0
            while k<3:
                n+=1
                if n>=kol_strok:
                    break
                elif stroki[n]=='\n':
                    k+=1
                    n+=1
        else:
            if stroki[n].count('class') > 0:
                class_name=stroki[n][6:-2]
                soder_classa[class_name]=[]
            else:
                stroki[n]=stroki[n][1:-8]
                soder_classa[class_name].append(stroki[n])
            n+=1
    fail.close()
    return soder_classa, adres

def pokaz_class(soder_classa):
    for i in soder_classa:
        print('class ', i, ':', sep='')
        for j in soder_classa[i]:
            print(j)
        print('')