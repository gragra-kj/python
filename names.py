# name=[]
# for _ in range(3):
#     name.append(input("Whats your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}")

# name=input("Whats your name? ")
# # file=open("names.txt" ,"a")
# # file.write(f"{name}\n")
# # file.close()
# with open ("names.txt","a") as file:
#     file.write(f"{name}\n")
with open("names.txt","r") as file:
    for line in file:
       print("hello,", line.rstrip())