Greet = input("Greetings by Staff :- ").lower().strip()

if Greet.startswith("hello"):
    print("$0")
elif Greet.startswith("h"):
    print("$20")
else:
    print("$100")