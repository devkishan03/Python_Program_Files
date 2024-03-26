# count the numbers
# sum of digits
# reversing the number
# chek if the number is pelendrom
n = int(input("enter the number:"))
num = n
count = 0
sum = 0
reverse = ''
pelendrom = False
while n > 0:
    r = n % 10
    n = n // 10
    count += 1
    sum += r
    reverse += str(r)
print("number ", num, " is: ", count, " digit number")
print("Sum of digits will: ", sum)
print("Reverse of a number will:", reverse)
reverse = int(reverse)
if num == reverse:
    pelendrom = True
print("Is the number will pelendrom:", pelendrom)
