name = input("Please enter your name: ")
while name == "":
    print("Invalid Name")
    name = input("Please enter your name")
else:
     print("Your name is: {}".format(name))

a = name[1::2]
print (a)

"""
for c in name [1:len(name):2]:
    print(c, end="")
"""