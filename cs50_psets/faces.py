def main():
    emoj = input("What's your emotion? ").replace(":(","🙁").replace(":)","🙂")
    convert(emoj)


def convert(emot):
    print(emot)


main()