def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    #print("# \n" * height, end="" )
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(size):
    #for each row in square
    for i in range(size):
        #print("#" * size)
        for j in range(size):
            #print brick
            print("#",end="")
        print()
main()