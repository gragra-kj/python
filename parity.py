# num=int(input("Enter a number: "))
# if num %2 ==0:
#     print("Your number is even")
# else:
#     print("Your number is odd")
# def main():
#     x=int(input("Value of x: "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2==0:
#         return True
#     else:
#         return False

# main()
def main():
    x=int(input("Value of x? "))
    if multipleof_three(x):
        print("Multiple of 3")
    else:
        print("Not a multiple of three")
def multipleof_three(n):
    if n% 3==0:
        return True
    else:
        return False
main()