# Compiler for Emmy
# Turns number of Emmy's into list of opnames
# emmy.py sends output to the Emmy Virtual Machine

import sys
import xxhash as xxh
import itertools

from . import lexicon

backup = lexicon.lex

def emmy_compile(input_code):
    global backup
    
    def rotate_values(my_dict) -> dict: # Modified version of https://www.stackoverflow.com/questions/58366635/rotate-values-of-a-dictionary 
        keys_list = list(my_dict.keys())
        values_list = list(my_dict.values())
        values_list.insert(0, values_list.pop())
        my_dict = dict(zip(keys_list, values_list))
        return my_dict
    
    lexicon.lex = backup
    
    code = hex(int(input_code)).strip('0x')
    code = [((len(code) % 2)*'0'+code)[n:n+32] for n in range(0,len(code),32)]


    commands = []

    for chunk in code:
        bytes_form = bytes.fromhex(chunk)
        byte_hash = xxh.xxh128(bytes_form)
        hex_hash = [byte_hash.hexdigest()[n:n+2] for n in range(0,len(byte_hash.hexdigest()),2)]
        commands.append(hex_hash)
    
    commands = list(itertools.chain.from_iterable(commands))
    commands_norm = []
    int_lit = False
    for command in commands:
        try:
            if not int_lit:
                x = lexicon.lex[command]
                if x == 'ils':
                    int_lit = True
                    x = lexicon.lex[command]
            else:
                if lexicon.lex[command] == 'ile':
                    int_lit = False
                    x = lexicon.lex[command]
                else:
                    x = command
        except KeyError:
            continue
        
        commands_norm.append(x)
        rotate_values(lexicon.lex)
        
    
    return ' '.join(commands_norm)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(emmy_compile(sys.argv[1]))    
