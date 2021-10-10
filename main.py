from math import sqrt


def prime(n):
    '''
    verificam daca un numar nu e prim
    :param n: termenul pe care il verificam
    :return: valoarea de adevar
    '''
    cont=0
    if n<2:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
           cont= cont+1

    if cont >0 :
        return True
    else:
        return False


def test_prime():
    '''

    :return:
    '''
    assert prime(12)==True
    assert prime(13)==False
    assert prime(1)==True


def check_list(lst):
    '''
    verificam daca toate elementele dintr-o lista data sunt neprime
    :param lst: lista data
    :return: valoarea de adevar
    '''

    for i in lst:
        if not prime(i):
            return False
            break
    return True



def get_longest_all_not_prime(lst):
    '''
    creem o lista noua in care punem cea mai lunga subsecventa care contine numere neprime
    :param lst: lista veche
    :return: lista noua
    '''
    rezultat = []
    for i in range(len(lst)):
        for j in range(i, len(lst) + 1):
            if check_list(lst[i:j+1]) == True and len(lst[i:j+1]) > len(rezultat):
                rezultat=lst[i:j+1]
    return rezultat

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([2, 3, 4, 4]) == [4, 4]
    assert get_longest_all_not_prime([0, 0, 0]) == [0, 0, 0]
    assert get_longest_all_not_prime([2, 2]) == []
def printMenu():
    print("1.Citim numerele")
    print("2.Afisam secventa de numere neprime")
    print("3.Verifica daca media numerelor nu depaseste o valoare citita")
    print("4.Iesi din program")


def citireLista():
    '''
    citim elementele dintr-o lista
    :return:
    '''
    lst = []
    n = int(input("Citim elementele listei:  "))
    for i in range(n):
        lst.append(int(input("l[" + str(i) + "]=")))
    return lst
def average1(lst):
    '''
    calculam media elementelor dintr-o lista
    :param lst: lista data
    :return: media numerelor
    '''
    return sum(lst)/ len(lst)
def get_longest_average_below(lst,average):
    '''
    afisam cea mai lunga subsecventa cu propietatea ca media numerelor e mai mica decat o medie data
    :param lst: lista data
    :param average: media fata de care trebuie sa fie mai mica
    :return: lista ceruta
    '''
    rezultat = []

    for i in range(len(lst)):
        for j in range(i, len(lst) + 1):

            if average1(lst[i:j+1]) < average and len(lst[i:j+1]) > len(rezultat):

                rezultat=lst[i:j+1]

    return rezultat
def main():
    test_prime()
    lst = []

    while True:
        printMenu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_all_not_prime(l))
        elif optiune == "3":
            average = float(input("Introdu media maxima: "))

            print(get_longest_average_below(l, average))
        elif optiune == "4":
            break


main()