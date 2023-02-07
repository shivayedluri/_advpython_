l=[5,6,7,9,34,77,76,]
def demo_fun(n):
    if n>=50:
        return True
    else:
        return False
    data=list(filter(demo_fun,l))
    print(data)