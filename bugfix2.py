import sys
import os
from simple_colors import *
import requests


def code_segment(code):
    columns, rows = os.get_terminal_size(0)
    #code="print sum(ord(c) for c in 'Happy new year to you!\nNanda Bye Bye\nSee You"
    lines=code.split('\n')
    print()
    for line in lines:
        line+=(columns-(len(line)%columns))*(" ")
        print("\033[0;30;47m"+line+"\033[0m",end='')
    print()
    print()




def qna_printer(a):
    #a=["You could also use the dictionary's get() method as well to avoid the exceptions. This could also be used to give a default path rather than None as shown below.",1,'>>> d = {"a":1, "b":2}\n>>> x = d.get("A",None)\n>>> print x\nNone',0]
    """
    q=["In my python program I am getting this error:",1,"KeyError: 'variablename'",0,"From this code:",1,"path = meta_entry['path'].strip('/'),",0,"Can anyone please explain why this is happening?",1]

    print(yellow('\nQuestion:','italic'))

    i=1

    while(i<len(q)):
        if(q[i]==1):
            print(q[i-1])
        else:
            code_segment(q[i-1])
        i+=2
    """
    print(green('\nTop Solution:\n','italic'))

    i=1

    while(i<len(a)):
        if(a[i]=='1'):
            print(a[i-1])
        
        elif(a[i]=='2'):
            print(u"\n\n\u001b[35;1mExecute this command:\n" )
            print(u"\u001b[37;1m"+a[i-1])
        else:
            code_segment(a[i-1])
            
        i+=2    

def main():
    file_name=sys.argv[-1]
    cmd="python3 "+file_name+" 2>error.txt"
    os.system(cmd)

    lines = []
    with open('error.txt') as f:
        lines = f.readlines()
    print(lines,'\n')
    
    error=lines[-1]
    
    if(error.split(':')[0].lower()=="modulenotfounderror"):
        param = error.split("'")[1]
        url="http://18.216.239.56/module_error/"+param	
    else:
        url="http://18.216.239.56/stackoverflow_error/"+error
    response = requests.get(url)
    data = response.json()['data']
    
    if(len(lines)==0):
        return ''

    print(red('\nERROR FOUND!', 'bold'))
    l=''
    for line in lines:
        l+=line
    print(l)
    print()
    os.system('rm error.txt')


    columns, rows = os.get_terminal_size(0)
    col=columns-len('BUG FIX DISCUSSION')
    spc= col//2
    h=spc*(' ')+'BUG FIX DISCUSSION'+(columns-spc)*(' ')
    print(cyan(h, 'bold'))
    
    qna_printer(data)

    print()

if __name__ == '__main__':
    main()

