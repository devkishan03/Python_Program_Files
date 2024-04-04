# prime number
n = int(input("enter the number:"))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print(n, "is prime number")
else:
    print(n, "is not a prime number")


# def prime(num):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(prime(n))
