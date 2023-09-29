tweet = input("Input: ")                 # Taking the input from user for the string to convert.
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]       # List of letter's i.e. vowels to be ommitted form every inputed string.

for i in vowels:                         # Creating a loop to iterate over vowels
    if i in tweet:                       # And further nestign conditonal to check wheather any vowels lies in the inputed string or not
        tweet = tweet.replace(i, "")     # if yes then omitt the vowel. and assign it back to tweet variable.
    else:
        None

print("Output:",tweet)                             # print the formatted string.