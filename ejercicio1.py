 
"""Dado una serie de numeros dividirlos en parejas de tal manera que el mínimo 
"""
def parejas(a):
    b=sorted(a)
    n=len(b)
    return sum([b[:n//2+1]])
