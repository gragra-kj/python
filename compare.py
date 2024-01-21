# x=int(input("Whats the value of x? "))
# y=int(input("Whats the value of y? "))
# if x==y:
#     print("X is equal to y")
# elif x > y:
#     print("x is greater that y")
# else:
#     print("x is less than y")
score=int(input("What did you score? "))
if score >=90 and score<= 100:
    print("You have grade A")
elif score >=80 and score<90:
    print("You have grade B")
elif score >=70 and score<80:
    print("You scored a C")
elif score >=60 and score<70:
    print("You scored a D")
else:
    print("You scored a F")
