def get_name():
    name = input("Please enter your name: ")
    while name == "":
        print("Invalid Name")
        name = input("Please enter your name")
    else:
        print("Your name is: {}".format(name))
    return name

def print_loop(name):
    for c in name[1:len(name):2]:
        print(c, end="")

def main():
    name = get_name()

    print_loop(name)


main()