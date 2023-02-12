# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except:
#     print("We have an error")
#
# print("code after capsule")
#
# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except: NameError as error:
#     print(error)
# else:
#     print("I am ELSE")
# finally:
#     print("Finally code")

def checker(var_1):
    if type(var_1)!= str:
        raise TypeError(f"Sorry, we can't work with {type(var_1)},"
                        f"we need class str")
    else:
        return var_1
first_var = 10
checker(first_var)

import