old_price=[23,3,5,6,8,4,6,7,8,9,6,5]
rs=5
def add_price(no):
    return no+5
new_price=map(add_price,old_price)
new_price1=list(map(lambda n:n+rs,old_price))
print(list(new_price1))
print(list(new_price))