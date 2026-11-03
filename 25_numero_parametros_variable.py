"""
def sumatorio(x,y,z=0,w=0):
    return x+y+z+w

print(sumatorio(6,5))
print(sumatorio(6,5,4))
print(sumatorio(6,5,4,9))
"""
def sumatorio(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

print(sumatorio(4,1))
print(sumatorio(4,1,9,10,3,8))