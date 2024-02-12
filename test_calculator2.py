from calculator2 import square

# def main():
#     test_square()

# def test_square():
#     # if square(5) !=25:
#     #     print("2 squared was not 4")
#     # if square(3) !=9:
#     #     print("3 squared is not 9")
#     try:
#        assert square(-2)==4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3)==9
#     except AssertionError:
#         print("3 squared is not 9")


# if __name__=="__main__":
#     main()
def test_positive():
    assert square(3)==9
    assert square(4)==16

def test_negative():
    assert square(-2)==4
    assert square(-4)==16

