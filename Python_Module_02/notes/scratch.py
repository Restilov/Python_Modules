import sys
sys.path.append('../ex1')
from ft_raise_exception import input_temperature

try:
    input_temperature('abc')
except ValueError as e:
    print(e)
    print(type(e))
    print(e.args)