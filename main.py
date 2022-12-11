#
#
# try:
#
#     a = int(input("a= "))
#     op = input("op: ")
#     b = int(input("b= "))
#
#     if op == "+":
#         print (a+b)
#
#     elif op == "-":
#         print (a-b)
#
#     elif op == "*":
#         print (a*b)
#
#     elif op == "/":
#         print (a/b)
#
#     elif op == "**":
#         print(a ** b)
#
#     elif op == "//":
#         print(a // b)
#
#     elif op == "%":
#         print(a % b)
#     else:
#         print ("incorrect")
#
#
# except ZeroDivisionError:
#     print("∞")
# except ValueError:
#     print ("incorrect!")
#
#





try:
    num = int(input("6 signed num.: "))

    a = num // 100000
    b = ((num - 100000) // 10000)
    c = (((num - a * 100000) - b * 10000) // 1000)
    d = (((((num - a * 100000) - b * 10000)) - c * 1000) // 100)
    e = ((((((num - a * 100000) - b * 10000)) - c * 1000) - d * 100) // 10)
    f = ((((((num - a * 100000) - b * 10000)) - c * 1000) - d * 100) - e * 10)

    abc = a + b + c
    deff = d + e + f

    if (deff - abc == 0):
        print("Happy number!")

    elif (num<100000, num>999999):
        print ("not 6-signed number")
    else:
        print("unhappy(")

except ValueError:
    print ("NAPİSHİ NUMBER!")

