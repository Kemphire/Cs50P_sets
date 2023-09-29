x = input("What's x? ")
y = input("What's y? ")

z = x + y
print(z)               # As you mihgt be womderin wtf is happening why it's just concantanating the number's
                       # rather them adding them as usual.
                       # this shit is happening because whenever python takes input without knowing what data type of input it is taking it will always
                       # suppose it to be string no matter what user entered maybe it's string or bool or anythin it will always treat the input as string

                       # to fix this we have to explicitely signify what we are taking as a input.
                       # for example if we have to take input as int.
                       # then we have to add int before input function and close whole input in paranthesis after the int.

x = int(input("What's x? "))   # Now it will take input as a int rather than string.
y = int(input("What's y? "))

z = x + y
print(z)

# Another appoach

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)                # We can nest function inside a function to get output
                            # the function which is in paranthesis will be executed first and the return value will be passed to outer function.
                            # this appoach is more readabe and succient then the previous one.

# One more appoach

print(int(input("What's x? ")) + int(input("What's y? ")))

# This code looks more succient and compact but it's not the best option because
# here pytho needs too many exceution first it will open first paranthesis then other and finally then return values after performing operation and passing values to print function.
# theres also so much probablity of mistakes and lack of readability.


# Float's - any real number having decimals in it called as float generally in computer science.

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

# Rounding float to nearest digit

# round(number[, ndigits])         - official documentation of round()

# the arguement inside parnathesis are the parameter of round function
# here number means that it only takes number as compulsary arguement and nothing else.
# because there's no arstrick before number which symbolises than anythin in general.

# Here [] square brackets sumbolises optional.
# that it's upto us that we want to enter those parameter inside the square braces or not
# if not it will by default round the number to nearest two digit.

# ndigits after comma represents to how many digit we want to round the number.
# for example to 5th place, 100th place or anything.

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)

# Rounding to specific digits.

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round((x / y),3)

print(z)

# Rounding to specific digits using f string only.

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.4f}")                # It will round it to 4th place after decimal


x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.9f}")                 # it wil round it to 9th place after decimal

# Using f string to resulting integers according to the international number system.

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x - y
print(f"{z:,}")               # it will just format string to american style
                              # a.k.a add comma after every three digits.

# function for square of number

def main():                                # This will create our main function where we input our number.
    x = int(input("What's x? "))           # and furthermore adding a function square(x) will be defining in coming lines
    print("Squared x is,", square(x))

def square(n):                             # in square() function n is its arguement which only can be integer.
    return n*n

main()

# 2nd approach

def main():                                # This will create our main function where we input our number.
    x = int(input("What's x? "))           # and furthermore adding a function square(x) will be defining in coming lines
    print("Squared x is,", square(x))

def square(n):                             # in square() function n is its arguement which only can be integer.
    return n ** 2                          # ** operator raises n to it's second power

main()

# 3rd approach (using pow() instead of '**' or '*' operator)

def main():                                # This will create our main function where we input our number.
    x = int(input("What's x? "))           # and furthermore adding a function square(x) will be defining in coming lines
    print("Squared x is,", square(x))

def square(n):                             # in square() function n is its arguement which only can be integer.
    return pow(n,2)

main()

