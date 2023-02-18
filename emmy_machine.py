# Emmy Virtual Machine
# That's the fancy way of saying "a stack and a lexer"

import sys
from io import StringIO
from numpy import roll
import random

from . import lexicon
    

def emmy_execute(commands, user_input=''):
    
    newstdin = StringIO(user_input)
    newstdout = StringIO('')
    
    
    stack = []
    comlist = []
    
    commands = commands.split(' ')
    
    def input():
        return newstdin.getvalue()

    def print(*args):
        for arg in args:
            newstdout.write(str(arg))
    
    # lexer broken into four steps
    # 1. read a single function's hex value from list of commands inputted by the user.
    # 2. get opname of function in hex form from lexicon.
    # 3. execute function under opname
    # 4. rotate list of hex values and opnames.
    
    ippos = -1
    int_lit = [False, '']
    wl = [False,0]
    accum = 0
    
    while (ippos + 1)< len(commands):
        ippos += 1
        try:
            com = commands[ippos]
            comlist.append(com)
        except KeyError:
            continue
        if (not int_lit[0]) or com == 'ile':
            match com:
                case 'rol':
                    roll(stack, -1)
                case 'ror':
                    roll(stack, 1)
                case 'ils':
                    int_lit[1] = ''
                    int_lit[0] = True
                case 'ile':
                    int_lit[0] = False
                    try:
                        stack.append(int(int_lit[1],16))
                    except:
                        pass
                case 'icr':
                    try:
                        if len(stack) > 0:
                            stack[-1] += 1
                        else:
                            stack.append(1)
                    except:
                        stack.append(1)
                case 'dcr':
                    try:
                        if len(stack) > 0:
                            stack[-1] -= 1
                        else:
                            stack.append(-1)
                    except:
                        stack.append(-1)

                case 'wls':
                    if stack[-1]:
                        wl = [True, ippos]
                    else:
                        for j in range(len(commands)-ippos):
                            if commands[j+ippos] == 'wle':
                                ippos = j+1
                                break
                case 'wle':
                    if wl[0]:
                        if stack[-1]:
                            ippos = wl[1]
                        else:
                            wl = [False, 0]
                case 'acc':
                    accum += 1
                case 'dcc':
                    accum -= 1
                case 'ast':
                    stack.append(accum)
                case 'cst':
                    stack = []
                case 'out':
                    if len(stack) > 0:
                        if type(stack[-1]) == str:
                            print(stack.pop(-1))
                        elif type(stack[-1]) == int:
                            print(chr(stack.pop(-1)))
                    else:
                        print()
                case 'inp':
                    stack.append(input())
                case 'xor':
                    stack.append(bool(stack.pop())^bool(stack.pop()))
                case 'pls':
                    stack.append(int(stack.pop())+int(stack.pop()))
                case 'mns':
                    stack.append(int(stack.pop())-int(stack.pop()))
                case 'num':
                    print(int(stack.pop(-1)))
                case 'rnd':
                    stack.append(random.randint(0,1))
                case 'xpl':
                    for x in range(69):
                        stack.append(chr(random.randint(0,2048)))
                case 'emy':
                    stack.append('Emmy')
                case 'bob':
                    stack.append('bob')
                case 'hwd':
                    stack.append('Hello, world!')
                case 'gds':
                    stack.append('Graindstone')
                case 'nin':
                    stack.append(int(input()))
                case _:
                    pass
        else:
            int_lit[1] += com
            
        
    return newstdout.getvalue()

if __name__ == "__main__":
    print(emmy_execute('hwd out', user_input = 'hallo'))