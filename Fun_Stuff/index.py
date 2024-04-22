import sys

def get_value(num):
    return arr[num]

arr = [1, 2, 3, 4]
tmp = 0

try:
    tmp = get_value(4)
except IndexError:
    sys.stdout.write('IndexError')
    tmp = None
except Exception as e:
    print('GeneralExcept', end='')
    tmp = None

print(tmp)
