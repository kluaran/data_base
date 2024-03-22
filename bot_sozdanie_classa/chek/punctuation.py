
def filtr(stroka):
    str(stroka)
    l = len(stroka)
    y=''
    spisok=[]
    for x in range(l):
        if (stroka[x] == ',' and stroka[x - 1] != ',' and stroka[x - 1] != '.' and stroka[x - 1] != ' ' and x != 0) or (stroka[x] == ' ' and stroka[x - 1] != ',' and stroka[x - 1] != '.' and stroka[x - 1] != ' ' and x != 0) or (stroka[x] == '.' and stroka[x - 1] != ',' and stroka[x - 1] != '.' and stroka[x - 1] != ' ' and x != 0):
            spisok.append(y)
            y = ''
        elif (stroka[x] == ',' and (stroka[x - 1] == ',' or stroka[x - 1] == ' ' or stroka[x - 1] == '.')) or (stroka[x] == ' ' and (stroka[x - 1] == ',' or stroka[x - 1] == ' ' or stroka[x - 1] == '.')) or (stroka[x] == '.' and (stroka[x - 1] == ',' or stroka[x - 1] == ' ' or stroka[x - 1] == '.')):
            continue
        elif x == l - 1 and stroka[x] != ',' and stroka[x] != ' ' and stroka[x] != '.':
            y = y + stroka[x]
            spisok.append(y)
        elif x == 0 and (stroka[x] == ',' or stroka[x] == ' ' or stroka[x] == ' '):
            continue
        else:
            y = y + stroka[x]

    stroka=spisok
    return stroka
