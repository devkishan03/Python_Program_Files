password = input("enter the password:")
password2 = input("confirm the password:")

if password == password2:
    print("password matched")
elif password.lower() == password2.lower():
    print("please check the cases of confirm password")
else:
    print("confirm password will not match")
