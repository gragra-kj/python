#match
name=input("Whats your name? ")

match name:
    case "Grace" | "Millena" | "Brenda":
        print("You are in St Claire")
    case "Lisa":
        print("You are in Elite Hostels")
    case "Hellen":
        print("You are in Qwetu")
    case _:
        print("Who?")


