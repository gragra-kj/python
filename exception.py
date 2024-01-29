# try:
#     x=int(input("Whats the value of x? "));
#     #print(f"x is {x}");
# except ValueError:
#     print("X is not an integer");
# else:
#     print(f"x is {x}");
def main():
    x=get_int()
    #x=get_int("Whats x? ")
    print(f"x is {x}")
#def get_int(prompt):
def get_int():
    while True:
        try:
            x=int(input("Whats the value of x? "))
            #return int(input(prompt))
            #return int(input("Whats the value of x? "))
        except ValueError:
            print("X is not an integer")
        #except ValueError:
           # pass
        else:
            break
    return x
main()


