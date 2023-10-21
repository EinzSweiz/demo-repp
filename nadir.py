def main():
    yas = int(input("Please enter your legal age:\n"))
    nadir(yas)

def nadir():
    if yas<18:
        print("We are so sorry, but youre not eligible ot continue")
    else:
        print("Welcome to our website")

main()