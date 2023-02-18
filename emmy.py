# For the first time in my life, I've actually had to write neat code.      #
# This is not neat code.                                                    #
# In other words, https://xkcd.com/1513/                                    #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#                                  E M M Y                                  #
#                                                                           #
# An esolang that looks similar to Unary but is actually very different.    #


import sys
import os


from . import emmy_machine
from . import emmy_compile

__versions__ = '0.1.0'
__authors__ = 'joyoforigami'


user_input = ' '

def set_input(arg):
    global user_input
    user_input = str(arg)

def rotate_values(my_dict) -> dict: # Modified version of https://www.stackoverflow.com/questions/58366635/rotate-values-of-a-dictionary 
    keys_list = list(my_dict.keys())
    values_list = list(my_dict.values())
    values_list.insert(0, values_list.pop())
    my_dict = dict(zip(keys_list, values_list))
    return my_dict



comlist = []

def run_code(input_code, user_input = '', stdout = True):
    input_code = input_code.count('Emmy ')+(input_code[len(input_code)-4:len(input_code)]=='Emmy')
    compiled_code = emmy_compile.emmy_compile(input_code)
    comlist = compiled_code.split(' ')
    output = emmy_machine.emmy_execute(compiled_code, user_input = user_input)
    
    if stdout:
        print(output)
    else:
        return output


if len(sys.argv) > 1:
    with open(os.getcwd()+sys.argv[1]) as f:
        f=f.read()
        try:
            user_input = sys.argv[2]
        except:
            user_input = ''
        
        run_code(f, user_input)
    