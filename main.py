def sum(a, b):
    return a+b
def diff(a, b):
    return a-b
def function(a, b):
    if b>=a:
        return True
def fact(a):
    if a==0:
        return 1
    return fact(a-1)*a

def simple(a):
    list = set()
    for i in range(a):
        for j in range(2, i):
            if i%j==0:
                if i in list:
                    list.remove(i)
                break
            else:
                list.add(i)
    return list
    print(list)
simple(15)
