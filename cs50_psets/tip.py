# 1'st approach

def main():
    dollars = dollars_to_float(input("How much was the meal? ").replace("$",""))
    percent = percent_to_float(input("What percentage would you like to tip? ").replace("%",""))
    tip = dollars * (percent/100)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return(float(d))


def percent_to_float(p):
    return(float(p))


main()

# 2'nd approach

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * (percent/100)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.replace("$","")
    return float(d)


def percent_to_float(p):
    p = p.replace("%","")
    return float(p)

main()
