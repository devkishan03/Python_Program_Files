item_name = input("enter item name:")
price = input("enter price:")
n = 25 - len(price)
item = item_name.ljust(n, ".") + price
print(item)
print(len(item))


dots="."*(25-len(item_name+price))
item2=item_name+dots+price
print(item2)
print(len(item2))
