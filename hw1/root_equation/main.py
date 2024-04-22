def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if a != 0:
        if c >= 0:
            x = (c ** 2 - b) / a
            if x % 1 == 0:
                print(int(x))
            else:
                print("NO SOLUTIONS")
        else:
            print("NO SOLUTIONS")
    else:
        if b == c ** 2:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTIONS")


main()
