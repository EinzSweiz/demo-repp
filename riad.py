birinci = int(input("Please enter the first number: "))
ikinci = input("please enter the symbol: ")
ucuncu = int(input("Please enter the second number: "))


def main():
    z = birinci*ucuncu
    y = birinci/ucuncu
    x = birinci+ucuncu
    t = birinci-ucuncu
    
    nadir(birinci, ikinci, ucuncu, x, y, y, t)

def nadir(birinci, ikinci, ucuncu, x, y, t, z):
    if ikinci == "*":
        print(z)
    elif ikinci == "/":
        print(y)
    elif ikinci =="+":
        print(x)
    elif ikinci == "-":
        print(t)
    else:
        print("Please the proper symbol!")

main()

print("Today is a nice day!")
    