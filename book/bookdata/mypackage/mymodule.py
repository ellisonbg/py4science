import math
myconstant = math.exp(-math.pi)

def myfunc(x):
    'scale x by myconstant e^-pi'
    return myconstant * x

if __name__=='__main__':
    x = 2.0
    print('testing with x=%f, myfunc=%f'%(x, myfunc(x)))

