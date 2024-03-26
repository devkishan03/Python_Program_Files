# # infinite loop
# while True:
#     print("hello")

# # break statement
# while True:
#     n = int(input("Enter number:"))
#     if n < 0:
#         print("negative number")
#     elif n > 0:
#         print("positive number")
#     else:
#         break

# #Break Example2
# count=0
# while count<10:
#     count += 1
#
#     if count>5:
#         break
#     print(count)

# # continue statement
# i = 0
# while i < 10:
#     n = int(input("enter the number:"))
#     if n % 3 == 0:
#         continue
#     else:
#         print(n)
#         i += 1

# # pass statement
# i = 0
# while i < 10:
#     n = int(input("enter the number:"))
#     if n % 3 == 0:
#         pass
#     else:
#         print(n)
#     i += 1

# else suite
i = 0
while i < 10:
    i += 1
    print(i)
    if i > 7:
        break  # toggle break and pass to check else block execute or not
        # pass
else:
    print("loop normally over")

print("after code of while and else block")
