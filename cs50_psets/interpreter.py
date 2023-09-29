expression = input("Expression: ")

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    ans = x + z
    print(round((ans),2))
elif y == "-":
    ans = x - z
    print(round((ans),2))
elif y == "*":
    ans = x * z
    print(round((ans),2))
elif y == "/":
    ans = x / z
    print(round((ans),2))
elif y == "/" & z == 0:

    print("z will not be zero")
