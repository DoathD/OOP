from abc import ABCMeta, abstractmethod, abstractproperty
from classes import Addition, Substraction, Multiplication, Division, Div, Mod, NOD, NOK

lists1 = [Addition(), Substraction(), Multiplication(), Division(), Div(), Mod()]
lists2 = [NOK(), NOD()]
a = 50
b = 15

for i in lists1:
    print(i.get_name())
    print(f"{a} {i.get_sign()} {b} = {i.estimate(a, b)}")

for i in lists2:
    print(f"{i.get_name()} {a} and {b} is {i.estimate(a, b)}")
