def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if( 2 <= len(s) <= 6):
        return False
    else:
        return True





main()