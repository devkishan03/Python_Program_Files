# factors of a number
n = int(input("enter the number:"))
print("factors of", n, "will be:", end=' ')
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=',')
