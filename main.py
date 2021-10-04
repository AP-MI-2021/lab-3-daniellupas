from math import *
def get_largest_prime_below(n):
    '''
    Returneaza cel mai mare numar prim, mai mic decat parametrul n
    :param n: numar intreg
    :return: Returneaza numarul prim
    '''
    for i in range(n-1, 1, -1):
        check=1
        for j in range(2, int(sqrt(i))+1):
            if i%j==0:
                check=0
        if check == 1:
            return i


def get_base_2(n):
    x = int(x)
    lista=[]
    s=''
    while x:
        lista.append(n%2)
        n=n/2
    for i in range(len(lista)-1,-1,-1):
        s=s+str(lista[i])
    return s


def is_palindrome(n):
    y=int(n)
    while y:
        rasturnat=y%10+rasturnat*10
        y=y/10

    if rasturnat==n:
         print("da")
    else:
        print("nu")


x=int(input("Dadad"))
is_palindrome(x)
print("dad")