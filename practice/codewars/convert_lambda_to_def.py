"""
Convert Lambda To Def
in this kata, you will be given a string with a lambda function in it. Your task is to convert that lambda function to a def function, with the exact same variables, the exact same name, and the exact same function it does.

The function, like a normal def function should be returned on a separate line.

The output should be returned as a string.

Examples
given an input of:

"func = lambda a: a * 1"
The output expected would be:


def func(a):
   return a * 1

the code would be like so:

convert_lambda_to_def("func = lambda a: a * 1")
# the output should == "def func(a):\n    return a * 1"
you need to put 4 four spaces before the return part of your output.

variable numbers of spaces, positional/keyword arguments, or zero arguments will not be tested.

double parameters will not be tested

Happy Coding!
"""

from icecream import ic
import re

def convert_lambda_to_def(string):
    x = re.match(r'(.+) = lambda (.+): (.+)', string)
    return f'def {x.groups()[0]}({x.groups()[1]}):\n    return {x.groups()[2]}'


print(convert_lambda_to_def("func = lambda a: a * 2")) # "def func(a):\n    return a * 2"
print(convert_lambda_to_def("somes = lambda s: s + 1")) # "def somes(s):\n    return s + 1"
print(convert_lambda_to_def("act = lambda h: h + ' ' + 'i'")) # "def act(h):\n    return h + ' ' + 'i'"
print(convert_lambda_to_def("a = lambda lambda_c: lambda_c.split(':')")) # "def a(lambda_c):\n    return lambda_c.split(':')"
