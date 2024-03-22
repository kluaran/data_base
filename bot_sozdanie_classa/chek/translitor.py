import bot_sozdanie_classa.chek.punctuation as punct
import bot_sozdanie_classa.chek.registr as reg

def perevod(arg):
    arg = reg.nigh(arg)
    arg=punct.filtr(arg)
    x=''
    for n in arg:
        x=x+n
        if n!=arg[-1]:
            x=x+' '
    arg=x
    z=''
    for y in arg:
        for t in alfovit:
            if y==t:
                z=z+alfovit[t]
            elif y==alfovit[t]:
                z=z+alfovit[t]
    arg=z
    return arg

alfovit={'а':'a',
         'б':'b',
         'в':'v',
         'г':'g',
         'д':'d',
         'е':'e',
         'ё':'yo',
         'ж':'gh',
         'з':'z',
         'и':'i',
         'й':'yi',
         'к':'k',
         'л':'l',
         'м':'m',
         'н':'n',
         'о':'o',
         'п':'p',
         'р':'r',
         'с':'s',
         'т':'t',
         'у':'u',
         'ф':'f',
         'х':'h',
         'ц':'c',
         'ч':'ch',
         'ш':'sh',
         'щ':'sh',
         'ъ':'',
         'ы':'yi',
         'ь':'',
         'э':'ye',
         'ю':'yu',
         'я':'ya',
         ' ':'_',
         '0':'0',
         '1':'1',
         '2':'2',
         '3':'3',
         '4':'4',
         '5':'5',
         '6':'6',
         '7':'7',
         '8':'8',
         '9':'9',
         'q':'q',
         'w':'w',
         'y':'y',
         'j':'j',
         'x':'x'}
